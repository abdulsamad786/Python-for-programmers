#!/usr/bin/env python
"""
Ex2)
Create a new directory name "Ex2". Create a new python file named "CreateAnArray.py". Call the function named AppendTheString created in the previous exercise. Append two strings from the pervious Samples Strings.    

Sample String Input 1: I am going to
Sample String Input 2: Lahore

Result: I am going to Lahore.
                                                                                                      
                                                                                                      HINT: Import the Module from pervious Ex1.

"""

from Ex1.string_addition import * 

"""I have learnt that in order to import something
from another function or module itself, the preceeding module
must be present in the same directory/folder. Otherwise python will
not import it"""



def calling_function():
    """ This function is calling thefunction from the previous
    module"""
    calling = AppendTheString('I am going to',' Lahore.') 
    print calling

def main():
    """ this is main function which is calling calling_function"""
    calling_function()

if __name__ == '__main__':
    main()

