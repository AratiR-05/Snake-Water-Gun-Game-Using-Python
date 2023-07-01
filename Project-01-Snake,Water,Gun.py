import random
#Game - Snake, Water or Gun
def gamewin(comp,you):
# if two values are equal, declare a tie!
    if comp==you:
        return None
# check for all possibilities when computer chose 's'        
    elif comp =='s':
        if you =='w':
            return False
        elif you =='g':
            return True  
# check for all possibilities when computer chose 'w'        
    elif comp =='w':
        if you =='g':
            return False
        elif you =='s':
            return True             
# check for all possibilities when computer chose 'g'        
    elif comp =='g':
        if you =='s':
            return False
        elif you =='w':
            return True
#Computer Turn : 
randno = random.randint(1,3)
if randno ==1:
    comp ="s"
elif randno ==2:
    comp ="w"
elif randno ==3:
    comp ="g"    

you = input("Your Turn: Snake(s), Water(w), or Gun(g)?")  
a = gamewin(comp, you)
print(f"Computer Chose {comp}") 
print(f"You Chose {you}")

if a==None:
    print("The Game is Tie!")
elif a:
    print("You Win")  
else:
    print("You Lose!")   

