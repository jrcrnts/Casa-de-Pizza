import random
import json
import os

DATA_FILE = "membership_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def generate_card_number():
    return "CDP-" + str(random.randint(100000, 999999))

def register_member(members):
    name = input("Enter full name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    card_number = generate_card_number()
    while card_number in members:
        card_number = generate_card_number()

    members[card_number] = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Points": 0
    }

    print(f"\n✅ Member registered successfully!")
    print(f"🎫 Membership Card Number: {card_number}")
    return members

def view_members(members):
    if not members:
        print("❌ No members found.")
        return
    print("\n📋 Casa de Pizza Members:")
    for card, info in members.items():
        print(f"\nCard #: {card}")
        for key, value in info.items():
            print(f"  {key}: {value}")

def main():
    members = load_data()

    while True:
        print("\n=== Casa de Pizza Membership System ===")
        print("1. Register New Member")
        print("2. View All Members")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            members = register_member(members)
            save_data(members)
        elif choice == "2":
            view_members(members)
        elif choice == "3":
            save_data(members)
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
