import random
from datas import data
from art import logo
from art import vs


person_a=random.choice(data)
person_b=random.choice(data)
def person_choice():
    global person_a, person_b
    while person_a==person_b:
        person_b=random.choice(data)
        return person_b
name_a=person_a["name"]
name_b=person_b["name"] 
person_choice()

def print_choice():
    print(logo)
    print("WHO HAS MORE FOLLOWERS?")   
    print(f"OPTION A: {name_a} : {person_a['description']}")
    print(vs)
    print(f"OPTION B: {name_b} : {person_b['description']}")

score=0
in_game=True
print_choice()    

while in_game==True:
    choice=input("'A' OR 'B': ").lower()
    if(choice=='a'):
        if(person_a["follower_count"]>person_b["follower_count"]):
            score+=1
            print(f"\n{name_a} has more followers than {name_b} and your score is {score}!")
            person_b=random.choice(data)
            name_b=person_b["name"]
            person_choice() #this is used here so that the new name won't be equal to the previously won name
            print_choice()
        else:
            print(f" You lose!! {name_b} has more followers than {name_a} and your score is {score}\n")
            in_game=False

    elif(choice=='b'):
        if(person_b["follower_count"]>person_a["follower_count"]):
            score+=1
            print(f"\n{name_b} has more followers than {name_a} and your score is {score}!")
            person_a=person_b
            person_b=random.choice(data)
            person_choice()
            print_choice()
        else:
            print(f" You lose!! {name_a} has more followers than {name_b} and your score is {score}\n")
            in_game=False