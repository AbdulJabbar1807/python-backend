import re

def in_expensive_products(items,price):
    count = 0
    total_price = 0
    item_list = []
    for item in items:
        if item["price"] < price:
            item_list.append(item["name"])
            total_price += item["price"]
            count += 1
    
    return (count,total_price,item_list)   

def get_expensive_products(items,price):
    count = 0
    total_price = 0
    item_list = []
    for item in items:
        if item["price"] > price:
            item_list.append(item["name"])
            total_price += item["price"]
            count += 1
    return (count,total_price,item_list)  

def display_summary(products,price,choice):
    if choice == 'E':
        exp_count,exp_total_price,exp_product_list = get_expensive_products(products,price)
        if not exp_product_list:
                print("No product with MRP more than 1000 in inventory.")
        else:
            print("Inventory summary-")
            print(f"Matched product: {exp_count}")
            print(f"Expensive Product's list: {exp_product_list}")
            print(f"Total price: {exp_total_price}")
    else:
        inexp_count,inexp_total_price,inexp_product_list = in_expensive_products(products,price)
        if not inexp_product_list:
                print(f"There is no item in the list.")
        else:
            print("Inventory summary-")
            print(f"Matched product: {inexp_count}")
            print(f"Inexpensive Product's list: {inexp_product_list}")
            print(f"Total price: {inexp_total_price}")        
 
def customer_choice():
    while True:
        product_type = input("Do you want expensive item's(E) or inexpensive item's(I) (choose E/I): ").strip().upper()
        if product_type not in ("E","I"):
            pass
        else:
            return product_type
        break
        
            
def get_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 1000:
                print(f"Minimum selling price is {1000}!")
                continue
            elif num > 10000:
                print(f"The maximum selling price is'nt more than {10000}.")
                continue
            else:
                return num
        except ValueError:
            print("Invalid input!")
            continue
    
def main():
    products = [{"name":"Keyboard","price":1200},
            {"name":"Mouse","price":800},
            {"name":"Monitor","price":8000},
            {"name":"USB Cable","price":500},
            {"name":"Speaker","price":4500}]
    price = get_number("Enter the price: ")
    choice = customer_choice()
    display_summary(products,price,choice)
    
if __name__ == "__main__":
    main()      
