from inventory import add_product, view_products, update_stock, delete_product
from billing import generate_bill

def menu():
    while True:

        print("\n--- Grocery Store Management ---")
        print("1 Add Product")
        print("2 View Products")
        print("3 Update Stock")
        print("4 Delete Product")
        print("5 Generate Bill")
        print("6 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            update_stock()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            generate_bill()

        elif choice == "6":
            break

        else:
            print("Invalid choice")

menu()