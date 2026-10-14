def sales_transaction_analyzer(transactions,threshold_amount):
    count = 0
    total = 0
    names = []
    
    for transaction in transactions:
        if transaction["status"] == "completed" and transaction["amount"] >= threshold_amount:
            names.append(transaction["product"])
            count += 1
            total += transaction["amount"]
            
    return (count,total,names)

def display_result(transactions,threshold_amount):
    match_transaction_count,match_transaction_total,match_transaction_names = sales_transaction_analyzer(transactions,threshold_amount) 

    print("Sales summary:")
    print(f"Total number match with amount greater than or equal to {threshold_amount} are {match_transaction_count}.")
    print(f"Names list of product match with amount greater than or equal to {threshold_amount} are {match_transaction_names}.")
    print(f"Total of sum of match transaction completed greater than or equal to {threshold_amount} are {match_transaction_total}.")
    
def main():
    transactions = [
    {"product": "Keyboard", "amount": 1200, "status": "completed"},
    {"product": "Mouse", "amount": 800, "status": "pending"},
    {"product": "Monitor", "amount": 8000, "status": "completed"},
    {"product": "USB Cable", "amount": 500, "status": "completed"},
    {"product": "Speaker", "amount": 4500, "status": "failed"},
    {"product": "Webcam", "amount": 2500, "status": "completed"},
    ]   
    threshold_amount = 1000
    display_result(transactions,threshold_amount)

if __name__ == "__main__":
    main()