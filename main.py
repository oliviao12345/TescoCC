from datetime import datetime, timedelta

# Get the transaction date from the user
transaction_date_str = input("Enter the transaction date (YYYY-MM-DD): ")

try:
    # Convert the transaction date string to a datetime object
    transaction_date = datetime.strptime(transaction_date_str, "%Y-%m-%d")

    # Get the current date
    current_date = datetime.now()

    # Check if the year entered by the user is the same as the year in the current date
    if transaction_date.year != current_date.year:
        print("Please enter the current year")
    else:
        # Calculate the payment due date
        if transaction_date.day < 21:
            # Transaction date is before the 21st, payment due date is the 9th of the next month
            if transaction_date.month == 12:
                due_date = datetime(transaction_date.year + 1, 1, 9)
            else:
                due_date = datetime(transaction_date.year, transaction_date.month + 1, 9)
        else:
            # Transaction date is on or after the 21st, payment due date is the 9th of the month after the next
            if transaction_date.month == 11:
                due_date = datetime(transaction_date.year + 1, 1, 9)
            elif transaction_date.month == 12:
                due_date = datetime(transaction_date.year + 1, 2, 9)
            else:
                due_date = datetime(transaction_date.year, transaction_date.month + 2, 9)

        # Calculate the number of days until due date
        days_until_due = (due_date - current_date).days

        # Print the payment due date and number of days until due
        print("Payment due date:", due_date.strftime("%Y-%m-%d"))
        print("Days until due:", days_until_due)

except ValueError:
    print("Please enter a valid date!")
