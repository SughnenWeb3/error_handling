# ===== TASK 4: Bank Account Withdrawal System =====
# Create TWO custom exceptions:
# - InsufficientFundsError: raised when withdrawal amount exceeds balance
# - InvalidTransactionError: raised when amount is negative or zero
# 
# The function should:
# - Accept prompt, current balance, and minimum balance (for overdraft protection)
# - Validate withdrawal amount is a valid number (raise ValueError if not)
# - Check if amount is positive (raise InvalidTransactionError if not)
# - Check if withdrawal would bring balance below minimum (raise InsufficientFundsError if so)
# - Return the withdrawal amount if valid
# - Keep asking until valid input

print("=== Task 1: Bank Account Withdrawal System ===")
print("Current Balance: $1000.00")
print("Minimum Balance: $100.00\n")

class InsufficientFundsError(Exception):
        pass
class InvalidTransactionError(Exception):
        pass
def process_withdrawal(prompt, balance, min_balance):
   

    # Write your code here.
    # Define InsufficientFundsError class
    # Define InvalidTransactionError class
    # Validate withdrawal rules
    # Handle all exceptions with appropriate messages
    #

    print("=== Task 4: Bank Account Withdrawal System ===")
print("Current Balance: $1000.00")
print("Minimum Balance: $100.00\n")


class InsufficientFundsError(Exception):
    pass

class InvalidTransactionError(Exception):
    pass


def process_withdrawal(prompt, balance, min_balance):
    withdraw = input(prompt).strip()

    
    try:
        amount = float(withdraw)
    except ValueError:
        raise ValueError("Input must be a number.") 

    
    if amount <= 0 and amount <50:
        raise InvalidTransactionError("Amount must be between .")

    
    if balance - amount < min_balance:
        raise InsufficientFundsError(
            f"Cannot withdraw {amount}. Balance would drop below minimum ({min_balance})."
        )

    return amount



balance = 1000.00
min_balance = 100.00

while True:  
    try:
        amount = process_withdrawal("Enter withdrawal amount: $", balance, min_balance)
    except ValueError as value_error:
        print("Error occured", value_error)
        continue
    except InvalidTransactionError as transaction_Error:
        print("Invalid transaction error ", transaction_Error)
        continue
    except InsufficientFundsError as Insufficient_funds:
        print("Error occured", Insufficient_funds)
        continue
    else:
        
        balance -= amount
        print(f"Withdrawal successful: ${amount}")
        print(f"New balance: ${balance}")
        break



amount = process_withdrawal("Enter withdrawal amount: $", 1000.00, 100.00)
print(f"Withdrawal successful: ${amount}")
print(f"New balance: ${1000.00 - float(amount)}")
print()

