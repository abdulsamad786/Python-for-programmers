#!/usr/bin/env python

"""
1)Create a function named AppendTheString that takes in two strings as an argument and returns a new string that joins the two string passed in as an argument. Please print the returned string in main.

Sample String Input 1: I am going to
Sample String Input 2: Lahore
                                                                                                      
                                                                                                      Result: I am going to Lahore.
"""

def AppendTheString(s1,s2): 
    """Appending/concatenating two strings s1 and s2"""
    return s1+s2

def ArrayofString(s1,s2):
	my_array= [s1,s2]	
	return my_array 
	


def main():
    returned_array =  ArrayofString("I am","Samad")
    print returned_array[0]
    print returned_array[1]


    """Calling AppendTheString(s1,s2), passing values to them """
    """s3 = AppendTheString('I am going to',' Lahore.') 
    print s3"""

if __name__ == "__main__":
    main()
