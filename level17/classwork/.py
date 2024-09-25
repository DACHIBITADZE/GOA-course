import random
#vprintavt tamashis dafas(cxrils)
board = ['-' , '-' , '-',
         '-' , '-' ,'-',
         '-' , '-' , '-' ]
currentplayer = "X"
winner = None
gamerunning = True
#avigiget motamashis input
def printBoard(board):
 print(board[0] + " | " + board[1] + " | " + board[2])
 print("---------")
 print(board[3] + " | " + board[4] + " | " + board[5])
 print("---------")
 print(board[3] + " | " + board[4] + " | " + board[5])

#shevamocmot mogebuli da fre
def playerinput(board):
    inp = int(input("ENTER NUMBER 1-9: "))
    if inp >=1 and inp <=9 and board[inp-1] == '-':
      board[inp-1] = currentplayer
    else:
       print("TRY AGAIN, ENTER NUMBER 1-9 :")

def checkhorizontail(board):
   global winner 
   if board[0] == board[2] and board[1] != "_":
      winner = board[0]
      return True
   elif board[3] == board[4] == board[5] and board[3] != "_":
      winner = board[3]
      return True
   elif board[6] == board[7] == board[8] and board[6] != "_":
      winner = board[0]
      return True
      
      
   
   





def  checkdiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
       winner= board[0]
       return True
    elif board[2] == board[4] ==board[6] and board[2] != '-':
       winner =board[2]
       return True
    
    
    
    
 
 
 
 
 
def checkrow(board):
   if board[0] == board[3] == board[6] and board[0] != '-':
     winner= board[0]
     return  True
   elif board[1]  == board[4] == board[7] and  board[1] != '_' :
     winner= board[1]
     return True
   elif board[2] == board[5] == board[8] and board[2] !='-':
    winner = board[2]
    return True
   



def checktie(board) :
   global gameRunning
   if '-' not in board :
     printBoard(board)
     print("IT S A TIE!")
     gameRunning = False
 #shevcvalot motamashe
def switchplayer ():
   global currentplayer
   if currentplayer == "X" :
    currentplayer = "O"
   else:
     currentplayer="X"
#shevamowmot mogebuli da fre kidev ertxel
def checkwin():
  global gameRunning
if checkdiag (board) or checkhorizontail(board) or checkrow(board) :
     print (f'the winner is {winner}')
     gameRunning= False


#boti
def computer(board) :
 while currentplayer == 'O' :
     position = random.randint(0,8)
     if board [position] == '-' :
       board [position]  =  'O'


while gamerunning:
   printBoard(board)
   playerinput(board)
   checkwin()
   checktie(board)
   switchplayer()
   computer(board)
   checktie(board)
   checkwin()
 





