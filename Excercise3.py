# no_of_guesses=9
# print no. of guesses left
n=18
i=0
while i<9:
    t=int(input("Enter a guess no.->"))
    if t==18:
        print("You have won and number of guesses it took is:{}".format(i+1))
    elif t<18 and (9-(i+1))>0:
        print("Guess higher, you have {} chances left".format(9-(i+1)))
    elif t>18 and (9-(i+1))>0:
        print("Guess lower, you have {} chances left".format(9-(i+1)))
    i+=1
if i==9:
    print("Game Over You lost")
