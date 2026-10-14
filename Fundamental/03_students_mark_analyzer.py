def main():
    marks = [45, 82, 91, 67, 88, 30]
    threshold = 80
    qualifying_students_count = 0
    qualifying_students_total = 0
    
    for mark in marks:
        if mark >= threshold:
            count += 1
            total += mark
    
    print("Student's mark summary-")
    print(f"Number of student's whose marks are greater than or equal to {threshold} are {qualifying_students_count}.")
    print(f"Total marks of student's with greater than or equal to {threshold} are {qualifying_students_total}.")


if __name__ == "__main__":
    main()