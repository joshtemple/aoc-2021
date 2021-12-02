x = 0
a = 0
z = 0

with open("input.txt") as file:
    for line in file.readlines():
        direction, distance = line.split(" ")
        distance = int(distance)
        if direction == "up":
            a -= distance
            print("aim", a)
        elif direction == "down":
            a += distance
            print("aim", a)
        elif direction == "forward":
            x += distance
            print("horizontal", x)
            z += a * distance
            print("depth", x)
        else:
            raise ValueError(f"Unexpected direction {direction}")

print(x, z, sep=", ")
print(x * z)
