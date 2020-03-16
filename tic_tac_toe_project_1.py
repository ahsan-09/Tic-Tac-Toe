from os import system
import random
system('cls')
def display_board(l):
    print(l[7],'|',l[8],'|',l[9])
    print('---------')
    print(l[4],'|',l[5],'|',l[6])
    print('---------')
    print(l[1],'|',l[2],'|',l[3])

def choose_person():
    flip=random.randint(0,1)
    if flip==0:
        return('player 1')
    else:
        return('player 2')

def play_game():
    choice=input("player 1: Do you want to be X or O ? ")
    a=1
    while a==1 :
        if (choice.upper()=='X')or(choice.upper()=='O'): 
            a=2
        else:
            print("You have entered an invalid option.")
            choice=input("player 1: Do you want to be X or O ? ")
        
    if choice.upper()=='X':
        other_choice='O'
    else:
        other_choice='X'
    first_player=choose_person()
    if (first_player=='player 1')or(first_player=='player 2'):
        print(f'{first_player} will go first')
    k=0
    want=input("Are you ready to play? Yes or No. ")
    if want.upper()=='YES' or want.upper()=='NO':
        pass
    else:
        print("You have entered an invalid input. Game is going to restart")
    player_1_list=[]
    player_2_list=[]
    loop_list=[]
    if want.upper()=='YES':
        while (len(loop_list)<9):
            if (first_player=='player 1')or (k==1):
                player_1=int(input('choose your position player 1 :(1-9)  '))
                player_1_list.append(player_1) 
                loop_list.append(player_1) 
                p1,p2=duplicate_check(player_1_list,player_2_list)  
                if(len(p1)==1)or(len(p2)==1):
                    print("You have entered same number again. Game will terminate now!")
                    break 
                l[player_1]=choice.upper()
                system('cls')
                display_board(l)
                if check():
                    a = 1 / 0
            if len(loop_list)!=9:
                k=1
                player_2=int(input("choose your position player 2 :(1-9)  "))
                player_2_list.append(player_2)
                loop_list.append(player_2)
                l[player_2]=other_choice.upper()
                p1,p2=duplicate_check(player_1_list,player_2_list)  
                if(len(p1)==1)or(len(p2)==1):
                    print("You have entered same number again. Game will terminate now!")
                    break
                system('cls')
                display_board(l)
                if check():
                    a = 1 / 0
    if(len(loop_list)==9):
        print("\n Match is drawn")

def duplicate_check(l1,l2):
    repeated_p1 = []
    repeated_p2 =[] 
    for i in range(0,len(l1)): 
        k = i + 1
        for j in range(k,len(l1)): 
            if l1[i] == l1[j] and l1[i] not in repeated_p1: 
                repeated_p1.append(l1[i]) 
    for i in range(0,len(l2)): 
        k = i + 1
        for j in range(k,len(l2)): 
            if l2[i] == l2[j] and l2[i] not in repeated_p2: 
                repeated_p2.append(l2[i]) 
    return(repeated_p1,repeated_p2)

def play_again():
    global l
    play_again=input("Do you want to play again? Yes or No : ")
    if play_again.upper()=='YES' or play_again.upper()=='NO':
        pass
    else:
        print("You have entered an invalid input. Game will terminate ")
    if play_again.upper()=='YES':
        system('cls')
        l=['x',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        display_board(l)
        try:
            play_game()
        except:
            pass
        return(True)
    return(False)

def check():
    if (l[1]=='X' and l[2]=='X' and l[3]=='X')or(l[1]=='O' and l[2]=='O' and l[3]=='O'):
        print('congratulations you have won the game!')
        return(True)
    elif (l[4]=='X' and l[5]=='X' and l[6]=='X')or(l[4]=='O' and l[5]=='O' and l[6]=='O'):
        print('congratulations you have won the game!')
        return(True)
    
    elif (l[7]=='X' and l[8]=='X' and l[9]=='X')or(l[7]=='O' and l[8]=='O' and l[9]=='O'):
        print('congratulations you have won the game!')
        return(True)

    elif (l[1]=='X' and l[4]=='X' and l[7]=='X')or(l[1]=='O' and l[4]=='O' and l[7]=='O'):
        print('congratulations you have won the game!')
        return(True)
    
    elif (l[5]=='X' and l[2]=='X' and l[8]=='X')or(l[5]=='O' and l[2]=='O' and l[8]=='O'):
        print('congratulations you have won the game!')
        return(True)
      
    elif (l[3]=='X' and l[6]=='X' and l[9]=='X')or(l[3]=='O' and l[6]=='O' and l[9]=='O'):
        print('congratulations you have won the game!')
        return(True)
    
    elif (l[5]=='X' and l[3]=='X' and l[7]=='X')or(l[5]=='O' and l[3]=='O' and l[7]=='O'):
        print('congratulations you have won the game!')
        return(True)

    elif (l[5]=='X' and l[1]=='X' and l[9]=='X')or(l[5]=='O' and l[1]=='O' and l[9]=='O'):
        print('congratulations you have won the game!')
        return(True)
l=['x',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(l)
try:
    play_game()
except:
    pass
a='True'
while(a):
    a=play_again()
    