# Budget Calculator Script

# Ask for total monthly budget
budget = float(input("Enter your total monthly budget: "))

# Ask for expenses until done
expenses = []
while True:
    expense_input = input("Enter an expense (or 'done' to finish): ")
    if expense_input.lower() == "done":
        break
    try:
        expense = float(expense_input)
        expenses.append(expense)
    except ValueError:
        print("Please enter a valid number or 'done'.")

# Calculate total expenses
total_expenses = sum(expenses)

# Calculate remaining balance
remaining_balance = budget - total_expenses

# Display remaining balance
print(f"Your remaining balance is: {remaining_balance:.2f}")

# Check for low funds warning
if remaining_balance < 500:
    print("Warning: Low Funds")
