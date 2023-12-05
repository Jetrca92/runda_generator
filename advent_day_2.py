import re

number_words =["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def read_input():
    with open("input.txt") as t:
        lines = t.readlines()
        total = 0
        for line in lines:
            digits = []
            words = []
            
            for char in line:
                if char.isdigit():
                    digits.append(char)
            for word in number_words:
                if word in line:
                    words.append(word)
            
            print(digits, words)
        print(total)

if __name__ == "__main__":
    read_input()