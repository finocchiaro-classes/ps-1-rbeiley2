# define function
def heart_rate (age, goal):
    max_HR = 220 - age
    print ("Your maximum heart rate is:", str(max_HR))
    if (goal == 'S'):
        targMinHR = 0.8 * max_HR
        print ("Your target heart rate is between", str(targMinHR), "and", str(max_HR))
    elif (goal == 'E'):
        targMinHR = 0.6 * max_HR
        targMaxHR = 0.8 * max_HR
        print ("Your target heart rate is between", str(targMinHR), "and", str(targMaxHR))
        
# ask user for their inputs
user_age = int(input("What is your age? "))
user_goal = input ("Is your goal speed (S) or endurance (E)? ")

# call function
heart_rate (user_age, user_goal)
