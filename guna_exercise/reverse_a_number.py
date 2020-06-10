
"""function is a block of code which is executed only when it is called
    "def" keyword is used to define a function
"""

def reverse(number):
    rev = 0
    while number>0:
        a = number%10
        rev = rev*10+a
        number = number//10 #// floor division 
    print(rev)
        
reverse(109)#function calling 