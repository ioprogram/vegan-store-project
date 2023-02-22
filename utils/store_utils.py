import pandas as pd
from pandas import DataFrame
from tabulate import tabulate as tab

from models.product import Product
from models.sell import Sell

store_file_path = "resources/store_records.csv"
sell_file_path = "resources/sells_records.csv"


def get_stored_products():
    """
    Get all existing product in the store
    :return: tuple of products
    """
    with open(store_file_path, "r") as store_file:
        df = pd.read_csv(store_file)
        print(tab(df, headers="keys"))


def add_new_product(product: Product):
    """
    Add a new product or update the quantity if exists
    :param product:
    :return: boolean
    """
    df = pd.read_csv(store_file_path)
    result = False
    try:
        check_exists = _check_if_product_exist(df, product.name)
        # Check if another product with same name exists
        if check_exists is not None:
            # Update the quantity index
            df.loc[check_exists, df.keys().tolist()[1]] = int(
                df.loc[check_exists, df.keys().tolist()[1]]) + int(product.quantity)
        else:
            # Add a new row
            df = pd.concat([df, pd.DataFrame(data=[product.__dict__()])], ignore_index=True)

        df.to_csv(store_file_path, index=False)
        result = True
    except Exception as ex:
        print("Errore nell'aggiunta del prodotto!", ex)
    finally:
        return result


def remove_product(product: Product):
    """
    Remove a product from csv file
    :param product: product to remove
    :return: Product
    """
    result = None
    df = pd.read_csv(store_file_path)

    try:
        check_exists = _check_if_product_exist(df, product.name)
        if check_exists is not None:
            available_quantity = int(df.loc[check_exists, df.keys().tolist()[1]])
            # Check if the requested quantity is available
            if available_quantity >= int(product.quantity):
                df.loc[check_exists, df.keys().tolist()[1]] = int(
                    df.loc[check_exists, df.keys().tolist()[1]]) - int(product.quantity)
                df.to_csv(store_file_path, index=False)
                # Rec sell transition
                _record_sell(product)
                result = product
            else:
                print(f"Quantità richiesta per il prodotto {product.name} non erogabile!")
                print(f"Quantità per il prodotto {product.name} a disposizione {available_quantity}")
        else:
            print(f"Prodotto {product.name} non trovato!")
    except Exception as ex:
        print("Errore durante la fase di vendita del prodotto!", ex)
    finally:
        return result


def _record_sell(product: Product):
    """
    Record a sell action
    :param product: product to sell
    :return: boolean
    """
    result = False
    try:
        df_product = pd.read_csv(store_file_path)
        # Get the product
        product_idx = _check_if_product_exist(df_product, product.name)
        # Map product to sell
        sell = _get_sell_from_product(df_product, product_idx, product.quantity)
        df_sell = pd.read_csv(sell_file_path)
        # Add a new row
        df_sell = pd.concat([df_sell, pd.DataFrame(data=[sell.__dict__()])], ignore_index=True)
        df_sell.to_csv(sell_file_path, index=False)
        result = True
    except Exception as ex:
        print("Errore durante la registrazione della transazione", ex)
    finally:
        return result


def get_incomes():
    """
    Get income
    :return: tuple(revenues, sales)
    """
    df_sell = pd.read_csv(sell_file_path)
    return df_sell['sell_price'].sum(), df_sell['single_revenue'].sum()


def _check_if_product_exist(df: DataFrame, name: str):
    """
    Search in Dataframe if a product exist
    :param df:
    :param name:
    :return:
    """
    list_product_idx = df.index[df['name'] == name].tolist()
    if len(list_product_idx) != 0:
        return list_product_idx[0]
    else:
        return None


def _get_sell_from_product(df_product: DataFrame, product_idx, quantity_sell):
    """
    Map Product to Sell
    :param df_product: product
    :param product_idx: id to search
    :return: Sell class
    """
    name = df_product.loc[product_idx, df_product.keys().tolist()[0]]
    buy_price = df_product.loc[product_idx, df_product.keys().tolist()[2]]
    sell_price = df_product.loc[product_idx, df_product.keys().tolist()[3]]

    return Sell(name=name, quantity=quantity_sell, buy_price=buy_price,
                sell_price=sell_price, single_revenue=quantity_sell * (sell_price - buy_price))
