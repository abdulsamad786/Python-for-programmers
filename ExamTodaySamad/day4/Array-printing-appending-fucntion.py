#!/usr/bin/env python

"""Calling the same function but printing the array in one line"""


def printListIteratively(s):
    final_string_in_one_line = ""
    for x in s:
        final_string_in_one_line = final_string_in_one_line + x + " "
    print final_string_in_one_line


def main():
    printListIteratively(["I", "am", "Abdul", "Samad"])

if __name__ == "__main__":
        main()


