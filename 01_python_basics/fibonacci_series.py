n = int(input("How many terms do you want? "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    next_term = a + b
    a = b
    b = next_term
