def compute(operation, num1, num2=1):
    """
    Performs a basic arithmetic operation on two numbers.

    Args:
        operation (str): The operation to perform ("add", "multiply", "subtract").
        num1 (int or float): The first number.
        num2 (int or float, optional): The second number. Defaults to 1.

    Returns:
        int or float: The result of the operation.
        str: "Invalid operation" if the operation is not recognized.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    else:
        return "Invalid operation"

# 1. compute("add", 5, 10)
print(compute("add", 5, 10))

# 2. compute("multiply", num1=3, num2=4)
print(compute("multiply", num1=3, num2=4))

# 3. compute("subtract", 20) (use default)
print(compute("subtract", 20))

# 4. Try an invalid operation
print(compute("divide", 10, 2))
