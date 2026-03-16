from database import load_products, save_products

def generate_bill():
    products = load_products()

    pid = int(input("Enter Product ID: "))
    qty = int(input("Enter Quantity: "))

    for p in products:
        if p["id"] == pid:
            if p["quantity"] >= qty:

                total = p["price"] * qty
                p["quantity"] -= qty

                save_products(products)

                print("Total Bill:", total)
                return
            else:
                print("Not enough stock")
                return

    print("Product not found")