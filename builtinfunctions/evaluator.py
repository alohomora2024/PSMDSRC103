# Propositional Logic Evaluator for Discrete Math for 2-3 variables
print("Propositional Logic Evaluator for Discrete Math")

# Get the number of variables from the user
variables = int(input("How many variables? "))
total_combinations = 2 ** variables

combinations_list = []

# Generate the combinations
for i in range(total_combinations):
    bin_equivalent = bin(i)[2:]  # Convert the number to binary string
    while len(bin_equivalent) < variables:  # Pad the binary string with leading zeros
        bin_equivalent = "0" + bin_equivalent
    combinations_list.append(tuple(int(val) for val in bin_equivalent))  
    # This will generate a list with values [(0,0),(0,1),(1,0),(1,1)]
    # For two variables

# Main program - Get the propositional logic expression from the user
expression = input("Enter the propositional logic expression: ")
"""
Note: Only the letters A, B, and C are allowed to be used.
Sample input: not(A and B) or (A and C)
All input must be small cases
"""
if variables == 2:
    print("A B f") 
    for A, B in combinations_list:
        evaluated_expression = eval(expression)
        print(A, B, evaluated_expression)
elif variables == 3:
    print("A B C f") 
    for A, B, C in combinations_list:
        evaluated_expression = eval(expression)
        print(A, B, C, evaluated_expression)