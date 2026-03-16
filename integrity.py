data = input("Enter data packet: ")

if data == data[::-1]:
    print("Data is intact (Palindrome)")
else:
    print("Data integrity check failed")