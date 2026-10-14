def main():
    temperatures = [18, 32, 25, 40, 29, 15]
    threshold = 25
    qualifying_temp_count = 0
    qualifying_temp_sum = 0
    
    for temperature in temperatures:
        if temperature > threshold:
            qualifying_temp_count += 1
            qualifying_temp_sum += temperature
    
    print("Student's mark summary-")
    print(f"Number of temperature's  greater than {threshold} are {qualifying_temp_count}.")
    print(f"Sum of temperature's  greater than to {threshold} are {qualifying_temp_sum}.")


if __name__ == "__main__":
    main()