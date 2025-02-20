import os

RECORD_LENGTH = 30  # Fixed record length for consistency

def donor():
    print("Option one selected!")
    
    with open('organs.txt', 'ab') as f:
        organ_name = input('Enter organ name: ').ljust(15)  # Ensuring fixed length
        blood_group = input('Enter blood group: ').ljust(5)
        age = input('Enter age: ').ljust(10)

        record = f"{organ_name}{blood_group}{age}\n"
        f.write(record.encode())

    print("Organ added to the record successfully")


def receiver():
    print("Option two selected!")

    if not os.path.exists('organs.txt'):
        print("No organ records found.")
        return

    size = os.path.getsize('organs.txt')
    n = size // RECORD_LENGTH

    organ_to_search = input('Enter organ to search: ').ljust(15).encode()
    blood_group_to_search = input('Enter blood group to search: ').ljust(5).encode()

    found = False
    updated_records = []

    with open('organs.txt', 'rb') as f:
        for _ in range(n):
            record = f.read(RECORD_LENGTH)
            if organ_to_search in record and blood_group_to_search in record and not found:
                found = True
                print("Organ is ready for donation")
            else:
                updated_records.append(record)

    if found:
        with open('organs.txt', 'wb') as f:
            for record in updated_records:
                f.write(record)
    else:
        print("Organ not found")


def search():
    print("Option three selected!")

    if not os.path.exists('organs.txt'):
        print("No organ records found.")
        return

    size = os.path.getsize('organs.txt')
    n = size // RECORD_LENGTH

    organ_name = input('Enter organ name to search: ').ljust(15)
    blood_group = input('Enter blood group to search: ').ljust(5)
    search_key = (organ_name + blood_group).encode()

    found = False

    with open('organs.txt', 'rb') as f:
        for i in range(n):
            record = f.read(RECORD_LENGTH)
            if search_key in record:
                print(f"Record found at position: {i + 1}")
                found = True
                break

    if not found:
        print("Record not found")


def main():
    print("Select an option:")
    print("1. Donor")
    print("2. Receiver")
    print("3. Search")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        donor()
    elif choice == '2':
        receiver()
    elif choice == '3':
        search()
    else:
        print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
