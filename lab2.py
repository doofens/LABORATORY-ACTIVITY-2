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

