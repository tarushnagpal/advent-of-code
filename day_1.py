freqs = []
with open('files/day_1_input.txt') as f:
    freqs = [int(freq.strip()) for freq in f]

# Part 1
total = 0
for i in freqs:
    total += i
print("Part 1: " + str(total))

# Part 2
freq = 0
viewed = set()
while True:
    for f in freqs:
        freq += f
        if freq in viewed:
            print("Part 2: " + str(freq))
            exit()
        else:
            viewed.add(freq)

