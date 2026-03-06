def main():
    while True:
        name = input("Enter student name (or type 'Exit' to quit): ")
        
        if name == "Exit":
            break
            
        try:
            mark1 = float(input("Enter mark for subject 1: "))
            mark2 = float(input("Enter mark for subject 2: "))
            mark3 = float(input("Enter mark for subject 3: "))
            
            average = (mark1 + mark2 + mark3) / 3
            
            if average >= 75:
                grade = "A"
            elif 60 <= average < 75:
                grade = "B"
            elif 40 <= average < 60:
                grade = "C"
            else:
                grade = "Fail"
            
            print("-" * 30)
            print(f"Name   : {name}")
            print(f"Average: {average:.1f}")
            print(f"Grade  : {grade}")
            print("-" * 30)
                
        except ValueError:
            print("Error: Please enter valid numerical marks.")
            print("-" * 30)

if __name__ == "__main__":
    main()
