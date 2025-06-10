no1 = int(input("Enter Number1:"))
no2 = int(input("Enter Number2:"))

print("1:Add")
print("2:Sub")
print("3:Mul")
print("4:Div")

choice = int(input("Enter your Choice:"))

if choice == 1:
    print("Add:", no1 + no2)
elif choice == 2:
    print("Sub:", no1 - no2)
elif choice == 3:
    print("Mul:", no1 * no2)
elif choice == 4:
    print("Div:", no1 / no2)
else:
    print("Error!Invalid choice...")
