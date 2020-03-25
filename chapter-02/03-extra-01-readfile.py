"""
Take a text file, creating (and printing) a nonsensical sentence from the nth word on each of the first 10 lines, where n is the line number.
"""

with open("03-extra-01-data.txt") as f:
        read_lines = f.readlines()
        for index, line in enumerate(read_lines):
            for i, word in enumerate(line.split()):
                if i == index:
                    print(word, end=' ')