# 1.Cube Number Test... Print out all cubed numbers up to the total value 1000.
# Meaning that if the cubed number is over 1000 break the loop.

for cube_num in range(1, 1000):
    if cube_num**3 > 1000:
        break
    print(cube_num**3)


# 2.Get first prime numbers up to 100

for prime_num in range(2, 101):
    for i in range(2, 101):
        if prime_num % i == 0:
            break
    if prime_num == i:
        print(prime_num)

#3 Take in a users input for their age, if they are younger than 18 print kids, 
# if they're 18 to 65 print adults, else print seniors

user_age = int(input("Enter your age "))

if user_age < 18:
    print("kids")
elif user_age <= 65:
    print("adults")
else:
    print("seniors")