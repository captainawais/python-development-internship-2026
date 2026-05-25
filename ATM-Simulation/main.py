# =========================================================
# ADVANCED ATM SIMULATION SYSTEM
# =========================================================

# Initial Account Data
balance = 5000
pin = "1234"

transaction_history = []


# =========================================================
# DISPLAY HEADER
# =========================================================
def display_header():

    print("\n" + "=" * 55)
    print("            ADVANCED ATM SIMULATION")
    print("=" * 55)


# =========================================================
# LOGIN SYSTEM
# =========================================================
def login():

    attempts = 3

    while attempts > 0:

        entered_pin = input("\nEnter your 4-digit PIN: ")

        if entered_pin == pin:

            print("\n✅ Login Successful!")
            return True

        else:

            attempts -= 1

            print(f"❌ Incorrect PIN! Attempts left: {attempts}")

    print("\n🚫 Too many failed attempts.")
    return False


# =========================================================
# SHOW MENU
# =========================================================
def show_menu():

    print("\nSelect an Option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")


# =========================================================
# CHECK BALANCE
# =========================================================
def check_balance():

    print(f"\n💰 Current Balance: Rs. {balance}")


# =========================================================
# DEPOSIT MONEY
# =========================================================
def deposit_money():

    global balance

    try:

        amount = float(input("\nEnter deposit amount: "))

        if amount <= 0:
            print("Invalid amount.")
            return

        balance += amount

        transaction_history.append(
            f"Deposited Rs. {amount}"
        )

        print(f"✅ Rs. {amount} deposited successfully!")

    except ValueError:
        print("Please enter a valid amount.")


# =========================================================
# WITHDRAW MONEY
# =========================================================
def withdraw_money():

    global balance

    try:

        amount = float(input("\nEnter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")
            return

        if amount > balance:

            print("❌ Insufficient balance!")
            return

        balance -= amount

        transaction_history.append(
            f"Withdrawn Rs. {amount}"
        )

        print(f"✅ Rs. {amount} withdrawn successfully!")

    except ValueError:
        print("Please enter a valid amount.")


# =========================================================
# TRANSACTION HISTORY
# =========================================================
def show_transaction_history():

    print("\n" + "-" * 55)
    print("              TRANSACTION HISTORY")
    print("-" * 55)

    if not transaction_history:

        print("No transactions available.")

    else:

        for index, transaction in enumerate(
            transaction_history,
            start=1
        ):
            print(f"{index}. {transaction}")

    print("-" * 55)


# =========================================================
# MAIN APPLICATION
# =========================================================
def main():

    display_header()

    if not login():
        return

    while True:

        show_menu()

        choice = input("\nEnter your choice: ")

        # CHECK BALANCE
        if choice == "1":
            check_balance()

        # DEPOSIT
        elif choice == "2":
            deposit_money()

        # WITHDRAW
        elif choice == "3":
            withdraw_money()

        # TRANSACTION HISTORY
        elif choice == "4":
            show_transaction_history()

        # EXIT
        elif choice == "5":

            print("\n👋 Thank you for using our ATM.")
            break

        else:
            print("Invalid option. Please try again.")


# =========================================================
# RUN APPLICATION
# =========================================================
if __name__ == "__main__":
    main()