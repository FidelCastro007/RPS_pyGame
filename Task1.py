# write a program to perform operations like sub, mul, div using function prototypes

def Arithemetic_except_add(a,b):
    results ={
    'Subtraction (A - B)': a - b,
    'Multiplication (A * B)': a * b,
    'Division (A / B)': a / b if b != 0 else None, 
    'Modulus (A % B)': a % b if b != 0 else None, 
    'Floor Division (A // B)': a // b if b != 0 else None,
    'Exponentiation (A ** B)': a ** b
    }

    return results

# Type1 without arg & without return (Runtime vals)
def Type1_Arithemetic_except_add ():
    a = int(input("Enter the value A:"))
    b = int(input("Enter the value B:"))

    results = Arithemetic_except_add(a,b)
    for operation,result in results.items():
        print(operation + ":" + str(result) )

Type1_Arithemetic_except_add()

# Type2 with arg & without return (Runtime vals)
def Type2_Arithemetic_except_add (a,b):

    results = Arithemetic_except_add(a,b)
    for operation,result in results.items():
        print(operation + ":" + str(result) )


a = int(input("\nEnter the value A:"))
b = int(input("Enter the value B:"))
Type2_Arithemetic_except_add(a,b)


# Type3 without arg & with return (Runtime vals)
def Type3_Arithemetic_except_add ():
    a = int(input("\nEnter the value A:"))
    b = int(input("Enter the value B:"))

    results = Arithemetic_except_add(a,b)
    return results

results  = Type3_Arithemetic_except_add()
for operation,result in results.items():
    print(operation + ":" + str(result) )


# Type4 with arg & with return (Runtime vals)
def Type4_Arithemetic_except_add (a,b):

    results = Arithemetic_except_add(a,b)
    return results

a = int(input("\nEnter the value A:"))
b = int(input("Enter the value B:"))
results = Type4_Arithemetic_except_add(a,b)
for operation,result in results.items():
    print(operation + ":" + str(result) )

""" def perform_operations(a, b):
    c_Sub = a - b
    c_Mul = a * b
    c_Div = a / b if b != 0 else None  # Avoid division by zero
    c_Mod = a % b if b != 0 else None
    c_floor = a // b if b != 0 else None
    c_Exp = a ** b
    
    results = [c_Sub, c_Mul, c_Div, c_Mod, c_floor, c_Exp]
    return results

def recursive_operations(a, b, depth):
    if a <= 0 or depth == 0:
        return perform_operations(a, b)
    else:
        print(f"Current values: A = {a}, B = {b}, Depth = {depth}")
        results = perform_operations(a, b)
        print(f"Results: {results}")
        # Recursively call with updated values
        return recursive_operations(a - b, b, depth - 1)

# Example usage
a = int(input("Enter the value A: "))
b = int(input("Enter the value B: "))
depth = int(input("Enter the recursion depth: "))

final_results = recursive_operations(a, b, depth)
print(f"Final Results after recursion: {final_results}") """


""" def Type1_Arithmetic_except_add():
    a = int(input("Enter the value A: "))
    b = int(input("Enter the value B: "))
    
    # Store results in a dictionary with operation names as keys
    results = {
        'Subtraction (A - B)': a - b,
        'Multiplication (A * B)': a * b,
        'Division (A / B)': a / b if b != 0 else None, 
        'Modulus (A % B)': a % b if b != 0 else None, 
        'Floor Division (A // B)': a // b if b != 0 else None,
        'Exponentiation (A ** B)': a ** b
    }
    
    # Print all operation names and values in a loop
    for operation, result in results.items():
        print(f"{operation}: {result}")

Type1_Arithmetic_except_add() """
