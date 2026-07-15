class InvalidQuantityError(Exception):
    pass

try:
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        raise InvalidQuantityError("Quantity must be greater than zero.")

    total = price * quantity
    print("Total amount payable:", total)

    if total > 100000:
        print("Manager approval is required.")

except ValueError:
    print("Invalid input. Please enter numeric values.")

except InvalidQuantityError as e:
    print(e)

finally:
    print("Order processing finished.")
