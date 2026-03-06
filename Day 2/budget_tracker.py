def main():
    print("--- Monthly Budget Tracker ---")
    
    try:
        # Ask for total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))
        
        # Ask for expenses until 'done'
        expenses = []
        while True:
            user_input = input("Enter expense (or type 'done' to finish): ")
            if user_input.lower() == 'done':
                break
            try:
                expense = float(user_input)
                expenses.append(expense)
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")
            
        # Subtract expenses from total budget
        total_expenses = sum(expenses)
        remaining_balance = total_budget - total_expenses
        
        # Display remaining balance
        print("\n--- Summary ---")
        print(f"Total Budget:    LKR {total_budget:,.2f}")
        print(f"Total Expenses:  LKR {total_expenses:,.2f}")
        print(f"Remaining:       LKR {remaining_balance:,.2f}")
        
        # Check for low funds
        if remaining_balance < 500:
            print("Warning: Low Funds")
        
    except ValueError:
        print("Error: Please enter valid numeric values for budget and expenses.")

if __name__ == "__main__":
    main()
