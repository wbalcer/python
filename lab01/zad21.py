x = input("x ")
x = int(x)

jednostki = x % 10
dziesiatki = (x // 10) % 10
setki = (x // 100) % 10

print(f"Jednostki: {jednostki}")
print(f"Dziesiątki: {dziesiatki}")
print(f"Setki: {setki}")