def main():
    expenses = [250, 800, 1200, 450, 2000, 700]
    threshold = 750
    count = 0
    total = 0
    
    for expense in expenses:
        if expense >= threshold:
            count += 1
            total += expense
    
    print("Expense analyzer summary-")
    print(f"Number of expenses made above or equal to {threshold} are {count}.")
    print(f"Total amount sum spend for the expenses above or equal to {threshold} is {total}.")
    
if __name__ == "__main__":
    main()