x = 0
z = 0

with open("input.txt") as file:
    for line in file.readlines():
        direction, distance = line.split(" ")
        distance = int(distance)
        if direction == "up":
            z -= distance
        elif direction == "down":
            z += distance
        elif direction == "forward":
            x += distance
        else:
            raise ValueError(f"Unexpected direction {direction}")

print(x, z, sep=", ")
print(x * z)
