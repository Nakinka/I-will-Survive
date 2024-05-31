
from hash_table import HashTable


def main():
    ht = HashTable()
    while True:
        print("\nHash Table Operations:")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Print Table")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            ht.create(key, value)
        elif choice == '2':
            key = input("Enter key: ")
            result = ht.read(key)
            if result:
                print(f"Value for key {key}: {result}")
            else:
                print(f"No value found for key {key}")
        elif choice == '3':
            key = input("Enter key: ")
            value = input("Enter new value: ")
            ht.update(key, value)
        elif choice == '4':
            key = input("Enter key: ")
            ht.delete(key)
        elif choice == '5':
            ht.print_table()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    

"""
(key1, ['23', '24'])
(key6, ['34'])
Index 4:
(key2, ['56'])
(key7, ['79'])
"""