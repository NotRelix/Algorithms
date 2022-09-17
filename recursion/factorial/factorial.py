# Factorial

def fact(x):
    if x == 1:                          # Base Case
        return x
    else:
        return x * fact(x - 1)          # Recursive Case

print(fact(5))                          # 120
