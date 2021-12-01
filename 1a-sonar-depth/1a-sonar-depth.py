prev = 1000000
increases = 0
with open("input.txt") as file:
    for line in file.readlines():
        depth = int(line.strip())
        print(depth, end=" ")
        if depth > prev:
            increases += 1
            print("increased")
        else:
            print("decreased")
        prev = depth

print(increases)
