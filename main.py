# Vegan Store for final project for ProfessionAI
import utils.navigation_utils as nu
import utils.store_utils as su
from models.product import Product

if __name__ == '__main__':
    cmd = None
    other = None

    while cmd != "chiudi":

        try:
            cmd = input("Inserisci un comando (digita aiuto per l'elenco dei comandi): ")

            if cmd == "vendita":
                sells_list = list()
                while other != "no":
                    # sell rec
                    prod_name = input("Nome del prodotto: ")
                    prod_qty = int(input("Quantità del prodotto: "))
                    sells_list.append(su.remove_product(Product(name=prod_name, quantity=prod_qty)))
                    other = input("Devi aggiungere altro? (sì\\no): ")
                print("Vendita registrata:\n")
                for prod in sells_list:
                    print(f"{prod.quantity}x{prod.name}")
            elif cmd == "profitti":
                # show sales
                income_tuple = su.get_incomes()
                print(f"Fatturato totale: {income_tuple[0]} Ricavo totale: {income_tuple[1]}")
            elif cmd == "aggiungi":
                # add a product
                prod_name = input("Nome del prodotto: ")
                prod_qty = int(input("Quantità del prodotto: "))
                prod_buy_price = float(input("Prezzo di acquisto: "))
                prod_sell_price = float(input("Prezzo di vendita: "))

                new_product = Product(name=prod_name, quantity=prod_qty, sell_price=prod_sell_price,
                                      buy_price=prod_buy_price)
                su.add_new_product(new_product)
                print(f"Aggiunto {prod_qty}x{prod_name}")
            elif cmd == "elenca":
                # list all products
                su.get_stored_products()
            elif cmd == "aiuto":
                # help
                nu.print_all_commands()
            else:
                pass
        except ValueError as ex:
            print("Il valore non è numerico!", ex)
        except Exception as ex:
            print("Errore di esecuzione!", ex)
