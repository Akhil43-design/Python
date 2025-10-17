import pandas as pd
import numpy as np

# --- Initial Data ---
data = {
    "Account_No": [101, 102, 103],
    "Name": ["Akhil", "Ravi", "Teja"],
    "Password": ["akhil123", "ravi123", "teja123"],
    "Balance": [5000, 7000, 9000]
}

transactions = []  # To store transaction history
df = pd.DataFrame(data)


# ---- User (Customer) Menu ----
def user_menu(name):
    global df, transactions
    while True:
        print(f"\nWelcome {name}! Choose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Send Money")
        print("5. View Transactions")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            balance = df.loc[df['Name'] == name, 'Balance'].values[0]
            print(f"💰 Your current balance: ₹{balance}")

        elif choice == "2":
            amt = float(input("Enter deposit amount: "))
            df.loc[df['Name'] == name, 'Balance'] += amt
            transactions.append(f"{name} deposited ₹{amt}")
            print("✅ Deposit successful!")

        elif choice == "3":
            amt = float(input("Enter withdrawal amount: "))
            bal = df.loc[df['Name'] == name, 'Balance'].values[0]
            if amt <= bal:
                df.loc[df['Name'] == name, 'Balance'] -= amt
                transactions.append(f"{name} withdrew ₹{amt}")
                print("✅ Withdrawal successful!")
            else:
                print("❌ Insufficient balance!")

        elif choice == "4":
            receiver = input("Enter receiver name: ")
            if receiver not in df['Name'].values:
                print("❌ Receiver not found!")
                continue
            amt = float(input("Enter amount to send: "))
            sender_bal = df.loc[df['Name'] == name, 'Balance'].values[0]
            if amt <= sender_bal:
                df.loc[df['Name'] == name, 'Balance'] -= amt
                df.loc[df['Name'] == receiver, 'Balance'] += amt
                transactions.append(f"{name} sent ₹{amt} to {receiver}")
                print("✅ Money sent successfully!")
            else:
                print("❌ Not enough balance!")

        elif choice == "5":
            print("\n📜 Transaction History:")
            found = False
            for t in transactions:
                if name in t:
                    print("-", t)
                    found = True
            if not found:
                print("No transactions yet!")

        elif choice == "6":
            print("Logging out...\n")
            break

        else:
            print("❌ Invalid choice! Try again.")


# ---- Admin (Manager) Menu ----
def admin_menu():
    global df
    while True:
        print("\n🏦 Manager Menu:")
        print("1. View All Customers")
        print("2. Add New Customer")
        print("3. Remove Customer")
        print("4. View Bank Summary")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n📋 All Customers Data:")
            print(df[['Account_No', 'Name', 'Balance']])

        elif choice == "2":
            try:
                acc = int(input("Enter new account number: "))
                name = input("Enter customer name: ")
                pwd = input("Set password for customer: ")
                bal = float(input("Enter initial balance: "))

                if name in df['Name'].values:
                    print("❌ Customer already exists!")
                else:
                    new_row = pd.DataFrame([[acc, name, pwd, bal]], columns=df.columns)
                    df = pd.concat([df, new_row], ignore_index=True)
                    print("✅ Customer added successfully!")

            except ValueError:
                print("❌ Invalid input! Please enter correct data.")

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            if name in df['Name'].values:
                df = df[df['Name'] != name]
                print("✅ Customer removed successfully!")
            else:
                print("❌ Customer not found!")

        elif choice == "4":
            print("\n📊 Bank Summary:")
            print(f"Total Customers: {len(df)}")
            print(f"Total Bank Balance: ₹{np.sum(df['Balance'])}")
            print(f"Average Balance per Customer: ₹{np.mean(df['Balance']):.2f}")

        elif choice == "5":
            print("Logging out...\n")
            break

        else:
            print("❌ Invalid choice! Try again.")


# ---- Main Program ----
while True:
    print("\n========== Welcome to SmartBank ==========")
    print("1. Customer Login")
    print("2. Manager Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        if name in df['Name'].values:
            stored_pwd = df.loc[df['Name'] == name, 'Password'].values[0]
            if password == stored_pwd:
                user_menu(name)
            else:
  
            print("❌ Incorrect password!")
        else:
            print("❌ Customer not found!")

    elif choice == "2":
        pwd = input("Enter Manager Password: ")
        if pwd == "admin123":
            admin_menu()
        else:
            print("❌ Wrong password!")

    elif choice == "3":
        print("👋 Thank you for using SmartBank! Have a great day!")
        break

    else:
        print("❌ Invalid choice! Try again.")
        
