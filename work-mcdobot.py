# Work - McDoBoot
# Author: Vivian
# 6 October

# It asks if you want fries with your meal.
fries = input("Hello! Would you like fries with your meal?")

if fries.lower() == "yes":
    print("Sure! I will include fries in your meal.")
elif fries.lower() == "no":
    print("No problem!")
else:
    print("Not a valid choice.")


#It should accept  Yes/yes  or  No/no  as inputs, and reply
#appropriately depending on the answer.
#If the user inputs anything else, it should repeat back their answer
#and say that it does not understand.
