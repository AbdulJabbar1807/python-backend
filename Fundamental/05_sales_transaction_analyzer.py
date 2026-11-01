def sales_transaction_analyzer(transactions,threshold_amount):
    count = 0
    total = 0
    names = []
    transaction_info = []
    
    for transaction in transactions:
        if transaction["status"] == "completed" and transaction["amount"] >= threshold_amount:
            names.append(transaction["product"])
            transaction_info.append(transaction)
            count += 1
            total += transaction["amount"]
            
    return (count,total,names,transaction_info)

def display_result(transactions,threshold_amount):
    matched_count,matched_total,matched_names,transaction_info= sales_transaction_analyzer(transactions,threshold_amount) 

    print("Your qualifying transactions are")
    print(f"-----------------------------------------------------------")
    if matched_names == []:
        print(f"There is no qualifying item in the list for ${threshold_amount}.")
    else:
        for transaction in transactions:
            if transaction["product"] and transaction["amount"] and transaction["status"] in (matched_names and transaction_info):
                print(f"> {transaction["product"]} - ${transaction["amount"]}")
        print(f"Matching transactions: {matched_count}")
        print(f"Total transaction amount: ${matched_total}")
    
def main():
    transactions = [
    {"product": "Keyboard", "amount": 1200, "status": "completed"},
    {"product": "Mouse", "amount": 800, "status": "pending"},
    {"product": "Monitor", "amount": 8000, "status": "completed"},
    {"product": "USB Cable", "amount": 500, "status": "completed"},
    {"product": "Speaker", "amount": 4500, "status": "failed"},
    {"product": "Webcam", "amount": 2500, "status": "completed"},
    ]   
    threshold_amount = int(input("Enter the threshold amount for your transaction: $"))
    display_result(transactions,threshold_amount)

if __name__ == "__main__":
    main()