from random import randint
import art
import game_data

#vars of the name, followers, description,country and score. 
name =""
follower1 =""
follower2 =""
description =""
country=""
score=0
#Print the Logo higher lower
print(art.logo)

#while loop untill the user worng!
while True:
    #vars for random int
    random_num1 = randint(0,51)
    random_num2 = randint(0,51)

    #For loop to initialize the Vers with the dictionary values for the Compare A statement
    for key,value in game_data.data[random_num1].items():

        if key == 'name':
            name = value
        elif key == 'follower_count':
            follower1 = value
        elif key == 'description':
            description = value
        elif key == 'country':
            country = value             
    #print compare A statement     
    print(f"Compare A: {name}, {description}, from {country}.")

    #print the logo VS
    print(art.vs)

    #For loop to initialize the Vers with the dictionary values for the Against B statement
    for key,value in game_data.data[random_num2].items():

        if key == 'name':
            name = value
        elif key == 'follower_count':
            follower2 = value
        elif key == 'description':
            description = value
        elif key == 'country':
            country = value 
    #print Against B statement     
    print(f"Against B: {name}, {description}, from {country}.")

    #input for who have more followers
    user_choose = input(f"Who has more followers? Type 'A' or 'B': ").upper()
    if(user_choose == 'A'):
        if(follower1 >= follower2):
            score+=1
            print(f"\n\nYou're right! current score: {score}")
        elif(follower2 > follower1):
            print(f"Sorry, that's worng. Final score: {score}")
            break
    elif(user_choose == 'B'):
        if(follower2 >= follower1):
            score+=1
            print(f"\n\nYou're right! current score: {score}")
        elif(follower1 > follower2):
            print(f"Sorry, that's worng. Final score: {score}")
            break