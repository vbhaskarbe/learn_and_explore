
even_store=[]
odd_store = []
even_count, odd_count =[0,0]
user_input = int(input("Enter a number up to user choice to get even and odd numbers's:- "))
for i in range(1, user_input+1):
    if i%2 == 0:
        even_store.append(i)
        even_count +=1
    else:
        odd_store.append(i)
        odd_count +=1
        
print(even_store)
print(odd_store)