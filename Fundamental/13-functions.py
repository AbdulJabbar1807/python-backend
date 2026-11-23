def details(firstname,lastname,age):
    user = {}
    user={"firstname":firstname,
        "lastname":lastname,
        "age":age}
    
    return user
def main():
    firstname = input("Enter your firstname: ")
    lastname = input("Enter your lastname: ")
    age = int(input("Enter your age: "))
    
    person_detail = details(firstname,lastname,age)
    print(person_detail)
    
if __name__ == "__main__":
    main()    
    