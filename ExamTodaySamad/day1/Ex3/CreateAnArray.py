#!/usr/bin/env python

"""
Create a new directory name "Ex3" copy "Ex1" in this folder. Create a new python file named "CreateAnArray.py". Call the function named AppendTheString created in the previous exercise. Append two strings from the pervious Samples Strings.                                                                   

Sample String Input 1: I am going to
Sample String Input 2: Lahore

Result: I am going to Lahore. 

HINT: Import the Module from pervious Ex1.
"""

from Ex1.string_addition import *
""" What I have done is that I have imported the whole Ex1 dir in Ex3 dir."""
"""Created a '__init__.py' using touch in linux.  """

def calling_function():
    """ In this function I am calling function AppendTheString(s1,s2), passing values to them"""
    calling = AppendTheString('I am going to',' Lahore')
    print calling

def main():
    calling_function()

if __name__ == '__main__':
    main()
