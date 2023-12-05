def read_input():
    with open("input.txt") as t:
        lines = t.readlines()
        total = 0
        for line in lines:
            numbers = []
            for char in line:
                if char.isdigit():
                    numbers.append(char)
            number = numbers[0] + numbers[-1]
            total += int(number)
        print(total)

if __name__ == "__main__":
    read_input()