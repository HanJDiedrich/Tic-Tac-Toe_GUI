#player1, the client X
'''This player1 file contains the player1UIPacker() class which controls the UI for player 1 in Tic Tac Toe.

Upon creating the UI and adding the necessary widgets, the class contains functions to send, receive, and check moves inputed by the user
by button presses. Functions to refresh and enable the board are included to create a smooth flowing user interface and tells the user when
and where they can select their move.

'''
import socket
import gameboard
from copy import deepcopy
import copy
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

class player1UIPacker():
    #variables
    turn = 'Player 1 Turn'
    #initilize gameboard
    board = gameboard.BoardClass()
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #board symbols
    icon11 = '_'
    icon12 = '_'
    icon13 = '_'
    icon21 = '_'
    icon22 = '_'
    icon23 = '_'
    icon31 = '_'
    icon32 = '_'
    icon33 = '_'
    game_statistics = "__________"

    def __init__(self):
        #initilize gameboard class variable
        self.board = gameboard.BoardClass()
        #create socket object
        
        #create canvas
        self.canvasSetup()
        #init vars
        self.initTKVariables()

        #add widgets
        #port
        self.createPortLabel()
        self.createPortEntry()
        #ipAddress
        self.createIPaddressLabel()
        self.createIPaddressEntry()
        #connect
        self.createConnectButton()
        self.createConnectedLabel()
        #input username
        self.createUsernameLabel()
        self.createUsernameEntry()
        self.createUsernameButton()
        #create board
        self.createBoard1_1(self.icon11)
        self.createBoard1_2(self.icon12)
        self.createBoard1_3(self.icon13)
        self.createBoard2_1(self.icon21)
        self.createBoard2_2(self.icon22)
        self.createBoard2_3(self.icon23)
        self.createBoard3_1(self.icon31)
        self.createBoard3_2(self.icon32)
        self.createBoard3_3(self.icon33)
        #whos turn it is
        self.createTurnLabel(self.turn)
        #statistics
        self.createStatsLabel(self.game_statistics)
        #run
        self.runUI()
    #UI basics
    def canvasSetup(self):
        #initialize canvas
        self.master = tk.Tk()
        #Title
        self.master.title('TIC TAC TOE-Player 1 (X)')
        #window size
        self.master.geometry('400x800')
        
    def initTKVariables(self):
        self.port = tk.IntVar()
        self.IPaddress = tk.StringVar()
        self.options = tk.StringVar()
        self.username = tk.StringVar()
    #refreshes the UI
    def refreshUI(self):
        self.master.update()
    #runs the UI
    def runUI(self):
        #event handler
        self.master.mainloop()

    #widget functions
    #Port
    def createPortLabel(self):
        self.portLabel = tk.Label(self.master, text="Please enter server port #", font=("Arial", 16), fg="black", bg="white")
        self.portLabel.pack()
    def createPortEntry(self):
        self.portEntry = tk.Entry(self.master, textvariable= self.port)
        self.portEntry.insert(0,500)
        self.portEntry.pack()
    #IP address
    def createIPaddressLabel(self):
        self.IPaddressLabel = tk.Label(self.master, text="Please enter server IP address", font=("Arial", 16), fg="black", bg="white")
        self.IPaddressLabel.pack()
    def createIPaddressEntry(self):
        self.IPaddressEntry = tk.Entry(self.master, textvariable= self.IPaddress)
        self.IPaddressEntry.insert(0,'127.0.0.1')
        self.IPaddressEntry.pack()
    #Conection using port and IP address
    def createConnectButton(self):
        self.connectButton = tk.Button(self.master, text='Connect', command=lambda: self.attemptConnection(self.portEntry.get(),self.IPaddressEntry.get()))
        self.connectButton.pack()
        self.connectButton.config(state='normal')
    #label for connection confirmation
    def createConnectedLabel(self):
        self.connectedLabel = tk.Label(self.master, text= 'Connected to Player 2',state='disabled', font=("Arial", 16), fg="black", bg="white")
        self.connectedLabel.pack()
    #enter username
    def createUsernameLabel(self):
        self.usernameLabel = tk.Label(self.master, text="Enter Username", font=("Arial", 16), fg="black", bg="white")
        self.usernameLabel.pack()
        self.usernameLabel.config(state= 'disabled')
    def createUsernameEntry(self):
        self.usernameEntry = tk.Entry(self.master, textvariable= self.username)
        self.usernameEntry.insert(0,'default')
        self.usernameEntry.pack()
        self.usernameEntry.config(state='disabled')
    def createUsernameButton(self):
        self.usernameButton = tk.Button(self.master, text='Send username', command=lambda: self.sendUsername(self.usernameEntry.get()))
        self.usernameButton.pack()
        self.usernameButton.config(state='disabled')

    #WHOS TURN is it currently
    def createTurnLabel(self,turn):
        self.turnLabel = tk.Label(self.master, text=turn, font=("Arial", 16), fg="black", bg="white")
        self.turnLabel.place(x='50',y='450')
        #self.turnLabel.config(text = Player 1 Turn)
        #self.turnLabel.config(text = Player 2 Turn)
    #stats
    def createStatsLabel(self,stats):
        self.statsLabel = tk.Label(self.master, text=stats, font=("Arial", 16), fg="black", bg="white")
        self.statsLabel.place(x='50',y='500')
    #create 3X3 board for Tic Tac Toe
    #(1,1)
    def createBoard1_1(self,icon11):
        self.board11 = tk.Button(self.master, text= icon11, command= self.press11)
        self.board11.place(x=125,y=300)
        self.board11.config(state='disabled')
    #(1,2)
    def createBoard1_2(self,icon12):
        self.board12 = tk.Button(self.master, text= icon12, command= self.press12)
        self.board12.place(x=175,y=300)
        self.board12.config(state='disabled')
    #(1,3)
    def createBoard1_3(self,icon13):
        self.board13 = tk.Button(self.master, text= icon13, command= self.press13)
        self.board13.place(x=225,y=300)
        self.board13.config(state='disabled')
    #(2,1)
    def createBoard2_1(self,icon21):
        self.board21 = tk.Button(self.master, text= icon21, command= self.press21)
        self.board21.place(x=125,y=350)
        self.board21.config(state='disabled')
    #(2,2)
    def createBoard2_2(self,icon22):
        self.board22 = tk.Button(self.master, text= icon22, command= self.press22)
        self.board22.place(x=175,y=350)
        self.board22.config(state='disabled')
    #(2,3)
    def createBoard2_3(self,icon23):
        self.board23 = tk.Button(self.master, text= icon23, command= self.press23)
        self.board23.place(x=225,y=350)
        self.board23.config(state='disabled')
    #(3,1)
    def createBoard3_1(self,icon31):
        self.board31 = tk.Button(self.master, text= icon31, command= self.press31)
        self.board31.place(x=125,y=400)
        self.board31.config(state='disabled')
    #(3,2)
    def createBoard3_2(self,icon32):
        self.board32 = tk.Button(self.master, text= icon32, command= self.press32)
        self.board32.place(x=175,y=400)
        self.board32.config(state='disabled')
    #(3,3)
    def createBoard3_3(self,icon33):
        self.board33 = tk.Button(self.master, text= icon33, command= self.press33)
        self.board33.place(x=225,y=400)
        self.board33.config(state='disabled')
    #send move via socket
    def sendMove(self,coords):
        self.c.send(coords.encode('ascii'))
    
    #check if it a win tie or loss
    def gameover(self,playerIcon):
        win = self.board.isWinner(playerIcon)
        tie = self.board.boardIsFull()
        #if the game is over
        if win == True:
            return 'Win'
        elif tie == True:
            return 'Tie'
        else:
            #continue playing
            self.enableBoard()
            return False
    #check if you want to play again
    def playagainActions(self,playerIcon,gameEnd):
        self.board.updateGamesPlayed()
        if gameEnd == 'Win':
            if playerIcon == 'X':
                #you win
                self.board.updateWins()
                self.board.lastPlayed = self.board.username
                playagain = messagebox.askquestion("Player 1 You win! Play again?")
                if playagain == "yes":
                    #reset the boards
                    self.board.gameboard = self.board.resetGameBoard()
                    self.placeIcon('0,0','_')
                    self.placeIcon('0,1','_')
                    self.placeIcon('0,2','_')
                    self.placeIcon('1,0','_')
                    self.placeIcon('1,1','_')
                    self.placeIcon('1,2','_')
                    self.placeIcon('2,0','_')
                    self.placeIcon('2,1','_')
                    self.placeIcon('2,2','_')
                    #send that you will play again
                    self.c.send(b'y')
                    #activate board for your turn
                    self.enableBoard()
                else:
                    #send that you will not play again
                    self.c.send(b'n')
                    #print game stats
                    self.printStatistics()
            elif playerIcon == 'O':
                #you loose
                self.board.updateLosses()
                self.board.lastPlayed = 'Player 1'
                playagain = messagebox.askquestion("Player 1 You loose! Play again?")
                if playagain == "yes":
                    #reset the boards
                    self.board.gameboard = self.board.resetGameBoard()
                    self.placeIcon('0,0','_')
                    self.placeIcon('0,1','_')
                    self.placeIcon('0,2','_')
                    self.placeIcon('1,0','_')
                    self.placeIcon('1,1','_')
                    self.placeIcon('1,2','_')
                    self.placeIcon('2,0','_')
                    self.placeIcon('2,1','_')
                    self.placeIcon('2,2','_')
                    #send that you will play again
                    self.c.send(b'y')
                    #activate board for your turn
                    self.enableBoard()
                else:
                    #send that you will not play again
                    self.c.send(b'n')
                    #print game stats
                    self.printStatistics()
        elif gameEnd == 'Tie':
            self.board.updateTies()
            self.board.lastPlayed = self.board.username
            playagain = messagebox.askquestion("Tie game! Play again?")
            if playagain == "yes":
                #reset the boards
                self.board.gameboard = self.board.resetGameBoard()
                self.placeIcon('0,0','_')
                self.placeIcon('0,1','_')
                self.placeIcon('0,2','_')
                self.placeIcon('1,0','_')
                self.placeIcon('1,1','_')
                self.placeIcon('1,2','_')
                self.placeIcon('2,0','_')
                self.placeIcon('2,1','_')
                self.placeIcon('2,2','_')
                #send that you will play again
                self.c.send(b'y')
                #activate board for your turn
                self.enableBoard()
            else:
                #send that you will not play again
                self.c.send(b'n')
                #print game stats
                self.printStatistics()

    #decide if to recieve move or end game
    def recieveMove(self,playerIcon):
        #receive the move
        self.turnLabel.config(text = 'Player 2 Turn')
        self.refreshUI()
        theirMove = self.c.recv(1024).decode('ascii')
        self.board.updateGameBoard(theirMove,'O')
        self.placeIcon(theirMove,'O')
        #check if move is a winner or not
        self.checkGameOver('O')
    #check game end on each move
    def checkGameOver(self,icon):
        if self.gameover(icon) == 'Win':
            self.playagainActions(icon,'Win')
        elif self.gameover(icon) == 'Tie':
            self.playagainActions('X','Tie')  
        else: #wait for opponent
            if icon == 'X':
                self.recieveMove('O')
            if icon == 'O':
                self.enableBoard()
                self.turnLabel.config(text = 'Player 1 Turn')
                self.refreshUI()
    #button presses
    def press11(self):
        currentIcon = self.board11.cget("text")
        if currentIcon == 'X' or currentIcon == 'O':
            messagebox.showinfo("","Invalid move\n\nTry again")
        else:
            icon = 'X'
            move = '0,0'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'X')
            #send move
            self.sendMove(move)
            self.disableBoard()
            #check if gameover and then to receive
            self.checkGameOver(icon)
    def press12(self):
        currentIcon = self.board12.cget("text")
        if currentIcon == 'X' or currentIcon == 'O':
            messagebox.showinfo("","Invalid move\n\nTry again")
        else:
            icon = 'X'
            move = '0,1'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'X')
            #send move
            self.sendMove(move)
            self.disableBoard()
            #check if gameover and then to receive
            self.checkGameOver(icon)
    def press13(self):
        currentIcon = self.board13.cget("text")
        if currentIcon == 'X' or currentIcon == 'O':
            messagebox.showinfo("","Invalid move\n\nTry again")
        else:
            icon = 'X'
            move = '0,2'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'X')
            #send move
            self.sendMove(move)
            self.disableBoard()
            #check if gameover and then to receive
            self.checkGameOver(icon)
    def press21(self):
        currentIcon = self.board21.cget("text")
        if currentIcon == 'X' or currentIcon == 'O':
            messagebox.showinfo("","Invalid move\n\nTry again")
        else:
            icon = 'X'
            move = '1,0'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'X')
            #send move
            self.sendMove(move)
            self.disableBoard()
            #check if gameover and then to receive
            self.checkGameOver(icon)
    def press22(self):
        currentIcon = self.board22.cget("text")
        if currentIcon == 'X' or currentIcon == 'O':
            messagebox.showinfo("","Invalid move\n\nTry again")
        else:
            icon = 'X'
            move = '1,1'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'X')
            #send move
            self.sendMove(move)
            self.disableBoard()
            #check if gameover and then to receive
            self.checkGameOver(icon)  
    def press23(self):
        currentIcon = self.board23.cget("text")
        if currentIcon == 'X' or currentIcon == 'O':
            messagebox.showinfo("","Invalid move\n\nTry again")
        else:
            icon = 'X'
            move = '1,2'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'X')
            #send move
            self.sendMove(move)
            self.disableBoard()
            #check if gameover and then to receive
            self.checkGameOver(icon)  
    def press31(self):
        currentIcon = self.board31.cget("text")
        if currentIcon == 'X' or currentIcon == 'O':
            messagebox.showinfo("","Invalid move\n\nTry again")
        else:
            icon = 'X'
            move = '2,0'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'X')
            #send move
            self.sendMove(move)
            self.disableBoard()
            #check if gameover and then to receive
            self.checkGameOver(icon)
    def press32(self):
        currentIcon = self.board32.cget("text")
        if currentIcon == 'X' or currentIcon == 'O':
            messagebox.showinfo("","Invalid move\n\nTry again")
        else:
            icon = 'X'
            move = '2,1'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'X')
            #send move
            self.sendMove(move)
            self.disableBoard()
            #check if gameover and then to receive
            self.checkGameOver(icon)
    def press33(self):
        currentIcon = self.board33.cget("text")
        if currentIcon == 'X' or currentIcon == 'O':
            messagebox.showinfo("","Invalid move\n\nTry again")
        else:
            icon = 'X'
            move = '2,2'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'X')
            #send move
            self.sendMove(move)
            self.disableBoard()
            #check if gameover and then to receive
            self.checkGameOver(icon)

    #place icon on the right spot
    def placeIcon(self,move,icon):
        if move == '0,0':
            self.board11.config(text= icon)
        if move == '0,1':
            self.board12.config(text= icon)
        if move == '0,2':
            self.board13.config(text= icon)
        if move == '1,0':
            self.board21.config(text= icon)
        if move == '1,1':
            self.board22.config(text= icon)
        if move == '1,2':
            self.board23.config(text= icon)
        if move == '2,0':
            self.board31.config(text= icon)
        if move == '2,1':
            self.board32.config(text= icon)
        if move == '2,2':
            self.board33.config(text= icon)
        self.refreshUI()
    #ask user if they want to play again

    #attempt connections to sockets
    def attemptConnection(self,port,IPaddress):
        connectedCondition = False
        #attempt server connection
        try:
            serverPort = int(port)
            serverAddress = IPaddress
            self.c.connect((serverAddress,serverPort))
            #print('Connected to Player 2\n')
            connectedCondition = True
            self.update_visibility(connectedCondition)
        except ValueError:
            self.handleError("Invalid port #")
        except socket.error as e:
            self.handleError("Invalid IP address")
    #error handling if port/ip is wrong
    def handleError(self,errorMessage):
        response = messagebox.askquestion("Error", errorMessage + "\n\nDo you want to try again?")
        if response == "yes":
            self.portEntry.delete(0, tk.END)
            self.IPaddressEntry.delete(0, tk.END)
        else:
            self.master.quit()

    #send username
    def sendUsername(self,username):
        myUsername = username
        self.c.send(myUsername.encode('ascii'))
        self.board.username = myUsername
        '''
        #receive opponents name
        self.board.opponent = self.c.recv(1024).decode('ascii')
        self.usernameButton.config(state='disabled')
        '''
        self.enableBoard()
    #update statistics
    def printStatistics(self):
        self.board.opponent = 'Player 2'
        self.statsLabel.config(text= self.board.printStats())
        self.refreshUI()

    #update label visibility
    def update_visibility(self,connectedCondition):
        if connectedCondition:
            self.connectButton.config(state='disabled')
            self.connectedLabel.config(state='normal')
            self.usernameEntry.config(state='normal')
            self.usernameLabel.config(state='normal')
            self.usernameButton.config(state='normal')
        else:
            self.connectedLabel.config(state='disabled')
    #enable the board
    def enableBoard(self):
        self.board11.config(state='normal')
        self.board12.config(state='normal')
        self.board13.config(state='normal')
        self.board21.config(state='normal')
        self.board22.config(state='normal')
        self.board23.config(state='normal')
        self.board31.config(state='normal')
        self.board32.config(state='normal')
        self.board33.config(state='normal')   
    #disable the board
    def disableBoard(self):
        self.board11.config(state='disable')
        self.board12.config(state='disable')
        self.board13.config(state='disable')
        self.board21.config(state='disable')
        self.board22.config(state='disable')
        self.board23.config(state='disable')
        self.board31.config(state='disable')
        self.board32.config(state='disable')
        self.board33.config(state='disable')  
#main loop
if __name__ == '__main__':
    player1 = player1UIPacker()
