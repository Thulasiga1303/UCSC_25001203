# Grade Calculator Script

while True:
    # Ask for student's name
    name = input("Enter student's name (or 'Exit' to quit): ")
    
    if name.lower() == "exit":
        print("Exiting the program.")
        break
    
    # Ask for 3 subject marks
    mark1 = float(input("Enter mark for subject 1: "))
    mark2 = float(input("Enter mark for subject 2: "))
    mark3 = float(input("Enter mark for subject 3: "))
    
    # Calculate the average
    average = (mark1 + mark2 + mark3) / 3
    
    # Determine the grade
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"
    
    # Display the result
    print("------------------------------")
    print(f"Name   : {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade  : {grade}")
    print("------------------------------")
    print()  # Add a blank line for better readability
