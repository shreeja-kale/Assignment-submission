#Question 1
#Use IF ELSE and ELIF to write a program in python for your Report Cards.
numerical_grade = int(input("What grade did the student earn? "))
if numerical_grade > 80:
	letter = "A"
elif numerical_grade > 70:
	letter = "B"
elif numerical_grade > 60:
	letter = "C"
elif numerical_grade > 50:
	letter = "D"
else:
	letter = "F"
print(letter)
print("Question 1 ended")
#Question 2
#Use For Loop to Print Prime Numbers in between 1 to 1000
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
print("Question 2 ended")
#Question 3
#Write a program for printing the tables from 1,10 using Nested For Loop
for i in range(1, 10):
    print ("i =", i, ":",)
    for j in range(1, 10):
        print ("{:2d}".format(i * j)),
    print
     print("Question 3 ended")
#Question 4
#Write a program to Print X Prime Numbers using While Loop starting from 0, and take the INput of X from
#the user
start = 11
end = 25

for i in range(start, end):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)
 # print("Question 4 ended")