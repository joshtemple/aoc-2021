prev = 1000000
increases = 0
window = []
with open("input.txt") as file:
    for i, line in enumerate(file.readlines()):
        depth = int(line.strip())
        window.append(depth)
        window_depth = sum(window)

        if i > 1:
            print(window, end=" ")
            print(window_depth, end=" ")

            if window_depth > prev:
                increases += 1
                print("increased")
                _ = window.pop(0)
            else:
                print("decreased")
                _ = window.pop(0)

            prev = window_depth

print(increases)
