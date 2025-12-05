def count(filename):
    pos = 50          
    count_zero = 0

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            if direction == 'L':
                pos = (pos - distance) % 100
            else:  # direction == 'R'
                pos = (pos + distance) % 100

            if pos == 0:
                count_zero += 1

    return count_zero

# count every time the dial hits 0 during any individual click of a rotation, not just when a rotation finishes

def count_zero_positions_method_B(filename):
    pos = 50          # starting dial position
    zero_count = 0    # count of times dial points at 0

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])

            step = -1 if direction == 'L' else 1

            # simulate each click
            for _ in range(distance):
                pos = (pos + step) % 100
                if pos == 0:
                    zero_count += 1

    return zero_count

print(count_zero_positions_method_B("input1.txt"))