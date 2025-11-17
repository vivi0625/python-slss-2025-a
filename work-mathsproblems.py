# Math Programs
# Author: Vivian Liang
# Nov 14 2025

# Question 1 - age in 2049 program
# ask the user their age
current_age = int(input("How old are you?"))

# calculate the age after 31 years
future_age = current_age + 31
# tell the user their age after 31 years
print(f"After 31 years, you'll be {future_age}")


# Question 2 - olympic judging
NUM_VOTES = 5
# ask the users for their scores
print("Enter your score from 0-10, half point are allowed.")

#ask the question
judge_1 = float(input("Judge 1 score: "))
judge_2 = float(input("Judge 2 score: "))
judge_3 = float(input("Judge 3 score: "))
judge_4 = float(input("Judge 4 score: "))
judge_5 = float(input("Judge 5 score: "))

# calculate the average
average_score = (judge_1 + judge_2 + judge_3 + judge_4 + judge_5) / 5
print(f"The average score is {average_score}")

# Question 3 - McDonald's program
burger = input("Welcome to McDonalds! Would you like a burger for $5?")

if burger == "yes":
    burger_cost = 5
    print("Sure, I will include it in your order!")
if burger == "no":
    burger_cost = 0
    print("Sure, I will not include it in your order.")

#ask fries
fries = input("Would you like to add fries for $3?")
if fries == "yes":
    fries_cost = 3
    print("Of course, I will include it in your order!")
if fries == "no":
    burger_cost = 0
    print("Ok,I will not include it in your order!")

# calculate total money
total_cost = burger_cost + fries_cost

# calculate tax
total_tax = total_cost * 0.14

# print final
final_cost = total_cost + total_tax
print(f"Your final cost for this order is {final_cost}")
