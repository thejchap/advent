r"""
--- Day 8: Matchsticks ---
Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.

It is common in many programming languages to provide a way to escape special characters in strings. For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.

However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.

For example:

"" is 2 characters of code (the two double quotes), but the string contains zero characters.
"abc" is 5 characters of code, but 3 characters in the string data.
"aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
"\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.
Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are \\ (which represents a single backslash), \" (which represents a lone double-quote character), and \x plus two hexadecimal characters (which represents a single character with that ASCII code).

Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?

For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.

Your puzzle answer was 1371.

--- Part Two ---
Now, let's go the other way. In addition to finding the number of characters of code, you should now encode each code representation as a new string and find the number of characters of the new encoded representation, including the surrounding double quotes.

For example:

"" encodes to "\"\"", an increase from 2 characters to 6.
"abc" encodes to "\"abc\"", an increase from 5 characters to 9.
"aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
"\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.
Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal. For example, for the strings above, the total encoded length (6 + 9 + 16 + 11 = 42) minus the characters in the original code representation (23, just like in the first part of this puzzle) is 42 - 23 = 19.

Your puzzle answer was 2117.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your Advent calendar and try another puzzle.

If you still want to see it, you can get your puzzle input.

You can also [Share] this puzzle.
"""

from advent.tools import *


def _parse(line):
    val_count = i = 0

    while i < len(line):
        if i >= len(line):
            break

        match line[i : i + 2]:
            case r"\x":
                i += 4
                val_count += 1
            case r"\"" | r"\\":
                i += 2
                val_count += 1
            case _:
                i += 1
                val_count += 1

    return val_count


def _encode(line):
    encoded = ['"']
    for tok in line:
        match tok:
            case '"' | "\\" | r"\x":
                encoded.append(f"\{tok}")
            case _:
                encoded.append(tok)
    encoded.append('"')
    return "".join(encoded)


def _pt1(lines):
    total_code_count = total_val_count = 0
    for line in lines:
        val_count = _parse(line[1:-1])
        total_code_count += len(line)
        total_val_count += val_count
    return total_code_count - total_val_count


def _pt2(lines):
    new_code_count = old_code_count = 0
    for line in lines:
        encoded = _encode(line)
        new_code_count += len(encoded)
        old_code_count += len(line)
    return new_code_count - old_code_count


TEST = r"""""
"abc"
"aaa\"aaa"
"\x27"
"""
ANSWERS = [12, 1371, 19, 2117]


def main():
    return afs.input_lines(tests=[TEST], parts=[_pt1, _pt2], run_input=True)
