import re

words_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def map_digit_sequence(sequence):
    if sequence.isdigit():
        return sequence
    else:
        return words_mapping[sequence]
    
def read_input():
    with open("input.txt") as t:
        lines = t.readlines()
        total = 0
        regex = "one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9"
        for line in lines:
            digit_sequences = re.findall(regex, line, flags=re.IGNORECASE)
            number_1 = map_digit_sequence(digit_sequences[0])
            number_2 = map_digit_sequence(digit_sequences[-1])
            number = number_1 + number_2
            total += int(number)
            print(number)
        print(total)

if __name__ == "__main__":
    read_input()