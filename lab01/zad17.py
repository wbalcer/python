a = int(input("a "))
b = int(input("b "))
c = int(input("c "))

output = a

if b >= c:
    if output < b:
        output = b
elif output < c:
    output = c

print(output)