import random
bigstring = "1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*"
password = ""
length = int(input("enter the length of the password\n"))
for i in range(length):
    password = random.choice(bigstring) + password


print(password)