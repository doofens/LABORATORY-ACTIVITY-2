print("This program will compute the student average")
print(" ")
print(" ")
print("Enter your scores.")
print(" ")
first = float(input("Enter your prelims scores    :"))
second = float(input("Enter your midterm scores    :"))
third = float(input("Enter your semifinal scores  :"))
fourth = float(input("Enter your final scores      :"))

average = (first + second + third + fourth)/4
print(" ")
print("Your average grade is {}".format(average))
print(" ")
if average>=75:
    print("Passed")
elif average<75:
    print("Failed")
else:
    print("Invalid!")

if average>=99 and average<=100:
    print("Your Grade is A")
elif average>=90 and average<98:
    print("Your Grade is B")
elif average>=80 and average<89:
    print("Your Grade is C")
elif average>=71 and average<79:
    print("Your Grade is D")
elif average>=61 and average<70:
    print("Your Grade is E")
elif average<=60:
    print("Your Grade is F")
else:
    print("Invalid Input!")