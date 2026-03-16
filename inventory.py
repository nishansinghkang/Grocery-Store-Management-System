from database import load_products, save_products

def add_product():
    products = load_products()

    pid = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    product = {
        "id": pid,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)
    save_products(products)

    print("Product added successfully!")

def view_products():
    products = load_products()

    if not products:
        print("No products available")
        return

    for p in products:
        print(p["id"], p["name"], p["price"], p["quantity"])

def update_stock():
    products = load_products()

    pid = int(input("Enter Product ID: "))

    for p in products:
        if p["id"] == pid:
            new_qty = int(input("Enter new quantity: "))
            p["quantity"] = new_qty
            save_products(products)
            print("Stock updated!")
            return

    print("Product not found")

def delete_product():
    products = load_products()

    pid = int(input("Enter Product ID to delete: "))

    products = [p for p in products if p["id"] != pid]

    save_products(products)
    print("Product deleted!")