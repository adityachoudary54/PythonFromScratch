import random
lst=['s','w','g']
comp_points=player_points=0
i=0
while i<10:
    comp_ch=random.choice(lst)
    player_ch=input("Enter your choice(s/w/g)->").strip().lower()
    if player_ch=='s':
        if comp_ch=='w':
            print("You win this round. {} rounds more to go".format(10-(i+1)))
            player_points+=1
        elif comp_ch=='g':
            print("You lose this round. {} rounds more to go".format(10-(i+1)))
            comp_points+=1
        else:
            print("Its a draw. {} rounds more to go".format(10-(i+1)))
    elif player_ch=='w':
        if comp_ch=='g':
            print("You win this round. {} rounds more to go".format(10-(i+1)))
            player_points+=1
        elif comp_ch=='s':
            print("You lose this round. {} rounds more to go".format(10-(i+1)))
            comp_points+=1
        else:
            print("Its a draw. {} rounds more to go".format(10-(i+1)))
    elif player_ch=='g':
        if comp_ch=='s':
            print("You win this round. {} rounds more to go".format(10-(i+1)))
            player_points+=1
        elif comp_ch=='w':
            print("You lose this round. {} rounds more to go".format(10-(i+1)))
            comp_points+=1
        else:
            print("Its a draw. {} rounds more to go".format(10-(i+1)))
    else:
        print("invalid choice cose again")
        continue
    i+=1
if player_points>comp_points:
    print("You have won by {}".format(player_points-comp_points))
elif player_points<comp_points:
    print("You are a loser man you suck!!!")
else:
    print("Its a draw. Good game.")
