import os

inventory_file = r"C:\Users\luzon\Documents\2ND SEM\CODES\productlist.txt"
sales_file = r"C:\Users\luzon\Documents\2ND SEM\CODES\sales.txt"

if not os.path.exists(inventory_file):
    open(inventory_file, 'a').close()

if not os.path.exists(sales_file):
    open(sales_file, 'a').close()

def process_sale():
    product_i = input("Enter product ID to sell: ").strip()
    quantity_sold = input("Enter quantity to sell: ").strip()
    
    if not quantity_sold.isdigit():
        print("Invalid quantity!")
        return
    
    quantity_sold = int(quantity_sold)
    
    updated_inventory = []
    found = False 
    product_name = ""
    price = 0
    stock = 0
    
    with open(inventory_file, "r") as file:
        products = file.readlines()
        
    for product in products:
        data = product.strip().split(", ")
        if data[0] == product_i:
            found = True
            product_name = data[1]
            stock = int(data[2])
            price = float(data[3])
            
            if quantity_sold > stock:
                print("Not enough stock!")
                return
            
            stock -= quantity_sold
            updated_product = f"{product_i}, {product_name}, {stock}, {price}\n"
            updated_inventory.append(updated_product)
        else:
            updated_inventory.append(product)

    if found:
        with open(inventory_file, "w") as file:
            file.writelines(updated_inventory)
        
        total_price = quantity_sold * price
        with open(sales_file, "a") as file:
            file.write(f"{product_i}, {product_name}, {quantity_sold}, {total_price}\n")
        print("Sale processed successfully")
    else:
        print("Product not found")

def view_sales():
    try:
        with open(sales_file, "r") as file:
            sales = file.readlines() 
            
            if not sales:
                print("No sales found")
                return
            
            print("\n===== Sales List =====")
            for sale in sales:
                data = sale.strip().split(", ")
                print(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}")
    except FileNotFoundError:
        print("Sales file not found! Make sure the file exists.")
        
def menu():
    while True:
        print("\n===== Sales Processing System =====")
        print("1. Process Sale")
        print("2. View Sales")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            process_sale()
        elif choice == "2":
            view_sales()
        elif choice == "3":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()

