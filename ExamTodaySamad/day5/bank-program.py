#!/usr/bin/env python

"""
Create a python program that asks user's name, password, deposit,
and saves in a file

"""


def arrayToString(s):
    final_string_in_one = ""
    for x in s:
        final_string_in_one += x + " "   
    return final_string_in_one

def username():
   fname = raw_input("Please enter your First name: ")
   lname = raw_input("Please enter your Last name: ")
   password= raw_input("Please enter your password: ")
   myarray= [fname, lname, password]
   return myarray 

def stringtofile( value , filename):
    fo = open(filename + ".txt" , "wb") 
    fo.write(value)
    fo.close()
    
    
def main():
    userinfo = username()
    print userinfo
    string_rtn = arrayToString( userinfo )
    print string_rtn
    stringtofile(string_rtn, userinfo[0])

if __name__ == "__main__":
    main()
