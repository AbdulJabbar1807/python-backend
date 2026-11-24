def calculate_grade(assignment):
    total = 0
    for homework in assignment.values():
        total += homework
    finalgrade = round(total/len(assignment),2)
    return finalgrade
