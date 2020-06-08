user_input = int(input("enter a number: "))
fact = 1
if user_input == 0:
    print(f'factorial of {user_input} is 0')
elif user_input == 1:
    print(f'factorial of {user_input} is 1')
    
else:
    for i in range(2, user_input+1):
        fact = fact*i
    print(f'factorial of {user_input} is :', fact)