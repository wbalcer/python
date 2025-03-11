import math

def draw_and_calculate(shape, size):
    if shape == "circle":
        radius = size
        for y in range(-radius, radius + 1):
            for x in range(-radius, radius + 1):
                if x ** 2 + y ** 2 <= radius ** 2:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        area = math.pi * radius ** 2
    
    elif shape == "square":
        side = size
        for _ in range(side):
            print("* " * side)
        area = side ** 2
    
    else:
        print("Nieobsługiwany kształt")
        return None
    
    return area

print("Pole koła:", draw_and_calculate("circle", 5))
print("Pole kwadratu:", draw_and_calculate("square", 5))
