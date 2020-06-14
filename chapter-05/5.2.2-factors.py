"""
Ask the user to enter integers, separated by spaces. From this input, create a dictionary whose keys are the factors for each number, and the values are lists containing those of the users' integers that are multiples of those factors.
"""


def calculateFactors(num):
    factors = []
    for i in range (1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

uniqueFactors = []
result = {}

integerInput = input('Enter integers separated by spaces...\n')
   
integers = integerInput.split()

for integer in integers:
    # print(f"{integer}")
    integer = int(integer)
    factors = calculateFactors(integer)
    for factor in factors:
        if factor not in uniqueFactors:
            uniqueFactors.append(factor)

for integer in integers:
    integer = int(integer)
    for factor in uniqueFactors:
            if factor % integer == 0:
                if result.get(factor):
                    result[factor].append(integer)
                else:
                    result[factor] = [integer]

print(result)