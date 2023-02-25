# Vegan Store for final project for ProfessionAI
import utils.navigation_utils as nu
import utils.store_utils as su
from models.product import Product

if __name__ == '__main__':
    cmd = None
    other_sell = None
    other_buy = None

    while cmd != "chiudi":

        try:
            cmd = input("Inserisci un comando (digita aiuto per l'elenco dei comandi): ")

            if cmd.casefold() == "vendita":
                sells_list = list()
                while other_sell != "no":
                    # sell rec
                    prod_name = input("Nome del prodotto: ")
                    prod_qty = int(input("Quantità del prodotto: "))
                    sells_list.append(su.remove_product(Product(name=prod_name, quantity=prod_qty)))
                    other_sell = input("Devi aggiungere altro? (sì\\no): ")
                print("Vendita registrata:\n")
                other_sell = None
                for prod in sells_list:
                    print(f"{prod.quantity}x{prod.name}")
            elif cmd.casefold() == "profitti":
                # show sales
                income_tuple = su.get_incomes()
                print(f"Fatturato totale: {income_tuple[0]} Ricavo totale: {income_tuple[1]}")
            elif cmd.casefold() == "aggiungi":
                buy_list = list()
                while other_buy != 'no':
                    # add a product
                    prod_name = input("Nome del prodotto: ")
                    prod_qty = int(input("Quantità del prodotto: "))
                    prod_buy_price = float(input("Prezzo di acquisto: "))
                    prod_sell_price = float(input("Prezzo di vendita: "))

                    new_product = Product(name=prod_name, quantity=prod_qty, sell_price=prod_sell_price,
                                          buy_price=prod_buy_price)
                    su.add_new_product(new_product)
                    buy_list.append(new_product)
                    other_buy = input("Devi aggiungere altro? (sì\\no): ")
                other_buy = None
                for nprod in buy_list:
                    print(f"Aggiunto {nprod.quantity}x{nprod.name}")

            elif cmd.casefold() == "elenca":
                # list all products
                su.get_stored_products()
            elif cmd.casefold() == "aiuto":
                # help
                nu.print_all_commands()
            else:
                pass
        except ValueError as ex:
            print("Il valore non è numerico!", ex)
        except Exception as ex:
            print("Errore di esecuzione!", ex)
