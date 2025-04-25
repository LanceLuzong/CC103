file_path = r"C:\Users\luzon\Documents\2ND SEM\CODES\Abs.tx"

def add_products():
    prouct_id = input("Enter product ID: ")
    product_name = input("Enter product name: ")
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")
    
    with open(file_path, "a") as file:
        file.write(f"{prouct_id}, {product_name}, {quantity}, {price}\n")
    
    print("Product added successfully")

def view_products():
    try:
        with open(file_path, "r") as file:
            products = file.readlines()  
            
            if not products:
                print("No products found")
                return
            print("\n===== Product List =====")
            for product in products:
                data = product.strip().split(", ")
                print(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}")
    except FileNotFoundError:
        print("file not found! Make sure the file exists.")

def edit_product():
    product_id = input("Enter the product ID to edit: ")
    found = False
    products = []

    
    with open(file_path, "r") as file:
            products = file.readlines()

    for products in products:
        data = products.strip().split(", ")
        if data[0] == product_id:
            found = True
            print(f"Current data {data}")
            
            new_product_name = input("Enter new product name: ") or data[1]
            new_quantity = input("Enter new quantity: ") or data[2]
            new_price = input("Enter new price: ") or data[3]

        
            updated_product = f"{product_id}, {new_product_name}, {new_quantity}, {new_price}\n"
        else:
            updated_product.append(products)
    if found:
        with open(file_path, "w") as file:
            file.writelines(updated_product)
        print("Product updated successfully")
    else:
        print("Product not found")
    


def delete_product():
     
     product_id = input("Enter the product ID to delete: ")
     updated_products = []
     found = False
     
     with open(file_path, "r") as file:
         products = file.readlines()
         for product in products:
             data = product.strip().split(", ")
             if data[0] == product_id:
                 found = True
                 print(f"Deleting product: {data}")
             else:
                 updated_products.append(product)
     if found:
            with open(file_path, "w") as file:
                file.writelines(updated_products)
            print("Product deleted successfully")
     else:
            print("Product not found")
def main():
    while True:
        print("\n===== Product Management System =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Edit Product")
        print("4. Delete Product")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_products()
        elif choice == "2":
            view_products()
        elif choice == "3":
            edit_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again")
if main == "__main__":
    main()
