def binary_search(contacts_no, num):
    left = 0
    right = len(contacts_no) - 1
    while left <= right:
        mid = (left + right) // 2
        if contacts_no[mid] == num:
            key = contacts_no[mid]
            print(f"Key:{key}")
            print(f"Your Phone Number {key} location is at: {mid}")
            return
        elif contacts_no[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    print("Contact Not found")


contacts = []
contacts.append("0341-2491020")
contacts.append("03332-24566728")
contacts.append("03335-2456672")
contacts.append("03355-5456677")

binary_search(contacts, "03335-2456672")
