#function tp print board
def printboard(x):
    print("{}|{}|{}".format(x[1],x[2],x[3]))
    print("_|_|_")
    print("{}|{}|{}".format(x[4],x[5],x[6]))
    print("_|_|_")
    print("{}|{}|{}".format(x[7],x[8],x[9]))

    
#Function to check whether any player wins
def checkwin(x):
    return x[1]==x[2]==x[3]!=' ' or x[4]==x[5]==x[6]!=' ' or x[7]==x[8]==x[9]!=' '\
           or x[1]==x[4]==x[7]!=' ' or x[5]==x[2]==x[8]!=' ' or x[9]==x[6]==x[3]!=' '\
           or x[1]==x[5]==x[9]!=' ' or x[7]==x[5]==x[3]!=' '

        
#function to ask repeat game again
def ask():
    var=input("Do u want to continue y/n: ")
    if var=='y' or var=='Y':
        tictac()

        
#main tictactoe code      
def tictac():
    print('Indices are from 1 to 9 from top to bottom')
    iterate=0
    x=[]
    for i in range(0,10):
        x.append(' ')
    printboard(x)
    p_1=input('what are u(player1) want to start with? Hint:enter X or O :')
    while (p_1 !='x' and p_1 !='X' and p_1 !='o' and p_1 !='O'):
         p_1=input('Invalid! enter again ')
    if p_1=='X' or p_1=='x':
        p_2='O'
    else:
        p_2='X'
    win=False
    iterate+=1
    while not win and iterate!=10:
        if iterate%2==1:
            index1=int(input('player1:where u want to enter? '))
            while index1<1 or index1>9 :
                index1=int(input("Invalid index! enter again: "))
            while x[index1]!=' ' :
                index1=int(input("Invalid! enter again: "))
            x[index1]=p_1
            printboard(x)
            if checkwin(x):
                win=True
                print ("congrats! player1 wins")
                ask()
        else:
            index2=int(input('player2:where u want to enter? '))
            while index2<1 or index2>9 :
                index2=int(input("Invalid index! enter again: "))            
            while x[index2]!=' ' :
                index2=int(input("Invalid! enter again: "))
            x[index2]=p_2
            printboard(x)
            if checkwin(x):
                win=True
                print ("congrats! player2 wins")
                ask()
        iterate+=1
    if (iterate==10 and win==False):
        print("match draws!")
        ask()
        
        
#call to tictac function
tictac()
