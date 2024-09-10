import random
print("welcome to the password generator")
letter=int(input("how many letters would you like in your password\n"))
symbol=int(input("how many symbols would you like\n"))
number=int(input("how many numbers would you like\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password=[]
for x in range(1,letter+1):
   l= random.choice(letters)
   password.append(l)

for y in range(1,number+1):
    n=random.choice(numbers)
    password.append(n)

for z in range (1,symbol+1):
    s=random.choice(symbols)
    password.append(s)
#print(password)
random.shuffle(password)
#print(password)
str=""
for x in password:
    str += x
print(f"your password is : {str}")

