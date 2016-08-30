#!/usr/bin/env python      

"""Create a program that has a function that takes in a list
of strings and creates multiple new files named as a string present 
in the list

For example the input passed to the function should create three
"""
x = 0
def listOfStrings(s):
    for x in s:
        fo = open( x + ".txt" ,"wb")
        fo.close()

def main():
    strfile = listOfStrings(["Zain","Hamza","Ather"])
    print strfile


if __name__ == "__main__":
    main()




