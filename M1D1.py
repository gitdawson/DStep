people = []

while True:
    new_dict = {'firstname': input('Enter first name: '), 
                'lastname': input('Enter last name: '), 
                'age': int(input('Enter age: ')), 
                'salary': int(input('Enter salary: '))}
    
    people.append(new_dict)
    
    age = new_dict['age']
    
    if age >= 18 and age <= 65:
        print("Get to work!")
    elif age > 65:
        print("Enjoy Retirement!")
    else:
        print("You are very young!")
    
    continue_input = input("Would you like to add another person? (yes/no): ")
    if continue_input.lower() != 'yes':
        break

print("\nAll entries:")
for person in people:
    print(person)
