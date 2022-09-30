"""
Objective
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format

The first line contains an integer, , denoting the number of entries in the phone book.
Each of the  subsequent lines describes an entry in the form of  space-separated values on a single line. The first value is a friend's name, and the second value is an -digit phone number.

After the  lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters and are first names only.


Output Format

On a new line for each query, print Not found if the name has no corresponding entry in the phone book; otherwise, print the full name and phoneNumber in the format name=phoneNumber.

"""

# SUBMITION: 

class PhoneList:
    def __init__(self):
        self.list = {}
    
    def newphone(self, new: str):
        new = new.split()
        self.list[new[0]] = new[1]
    
    def getphone(self, name: str):
        try:
            return f"{name}={self.list[name]}"
        except:
            return "Not found"
        

list1 = PhoneList()

for _ in range(int(input())):
    list1.newphone(input())

while True:
    try:
        print(list1.getphone(input()))
    except: 
        break
