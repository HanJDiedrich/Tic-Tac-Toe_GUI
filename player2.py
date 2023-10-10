#Player 2, the host
#player2 'O' or 'o'
#server
'''This player1 file contains the player2UIPacker() class which controls the UI for player w in Tic Tac Toe.

Upon creating the UI and adding the necessary widgets, the class contains functions to send, receive, and check moves inputed by the user
by button presses. Functions to refresh and enable the board are included to create a smooth flowing user interface and tells the user when
and where they can select their move. It is the secondary class to player1UIPacker, and waits for the socket connection from player1 to either
play again or quit.
'''

import socket
import gameboard
from copy import deepcopy
import copy
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

class player2UIPacker():
    #variables
    turn = 'Player 1 Turn'
    #initilize gameboard
    board = gameboard.BoardClass()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
        clientSocket = None
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
        self.createOpponentLabel()
        #input username
        '''
        self.createUsernameLabel()
        self.createUsernameEntry()
        self.createUsernameButton()
        '''
        #create 3x3 board
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

    def canvasSetup(self):
        #initialize canvas
        self.master = tk.Tk()
        #Title
        self.master.title('TIC TAC TOE-Player 2 (O)')
        #window size
        self.master.geometry('400x800')
        
    def initTKVariables(self):
        self.port = tk.IntVar()
        self.IPaddress = tk.StringVar()
        self.options = tk.StringVar()
        self.username = tk.StringVar()

    def refreshUI(self):
        self.master.update()

    def runUI(self):
        #event handler
        self.master.mainloop()

    #widget functions
    #Port
    def createPortLabel(self):
        self.portLabel = tk.Label(self.master, text="Please create server port #", font=("Arial", 16), fg="black", bg="white")
        self.portLabel.pack()
    def createPortEntry(self):
        self.portEntry = tk.Entry(self.master, textvariable= self.port)
        self.portEntry.insert(0,500)
        self.portEntry.pack()
    #IP address
    def createIPaddressLabel(self):
        self.IPaddressLabel = tk.Label(self.master, text="Please create server IP address", font=("Arial", 16), fg="black", bg="white")
        self.IPaddressLabel.pack()
    def createIPaddressEntry(self):
        self.IPaddressEntry = tk.Entry(self.master, textvariable= self.IPaddress)
        self.IPaddressEntry.insert(0,'127.0.0.1')
        self.IPaddressEntry.pack()
    #enter username
    '''
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
    '''
    #Conection using port and IP address
    def createConnectButton(self):
        self.connectButton = tk.Button(self.master, text='Initialize Server', command=lambda: self.initializeServer(self.portEntry.get(),self.IPaddressEntry.get()))
        self.connectButton.pack()
        self.connectButton.config(state='normal')
    #label for connection confirmation
    def createConnectedLabel(self):
        self.connectedLabel = tk.Label(self.master, text= 'Connected to Player 1', font=("Arial", 16), fg="black", bg="white")
        self.connectedLabel.pack()
    def createOpponentLabel(self):
        self.opponentLabel = tk.Label(self.master, text= 'Your opponent is:', font=("Arial", 16), fg="black", bg="white")
        self.opponentLabel.pack()
    #WHOS TURN is it currently
    def createTurnLabel(self,turn):
        self.turnLabel = tk.Label(self.master, text=turn, font=("Arial", 16), fg="black", bg="white")
        self.turnLabel.place(x='50',y='450')
        #self.turnLabel.config(text = Player 1 Turn)
        #self.turnLabel.config(text = Player 2 Turn)
    #statistics label
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
    #attempt connections to sockets
    def initializeServer(self,port,IPaddress):
        #create socket object
        PORT = int(port) #5000
        HOST = IPaddress #127.0.0.1
        self.s.bind((HOST,PORT))
        self.s.listen(1)
        #connect to cleint
        self.clientSocket,clientAddress = self.s.accept()
        #disable initialize button
        self.connectButton.config(state='disabled')
        #recieves username
        self.board.opponent = self.clientSocket.recv(1024).decode('ascii')
        self.opponentLabel.config(text= 'Your opponent is: '+self.board.opponent)
        '''
        #now input your username
        self.usernameLabel.config(state='normal')
        self.usernameEntry.config(state='normal')
        self.usernameButton.config(state='normal')
        self.clientSocket.send(self.board.username.encode('ascii'))
        #self.usernameButton.config(state='disabled')
        '''
        self.refreshUI()
        #recieve the first move from the opponent
        self.recieveMove('X')
    '''
    #send username 
    def sendUsername(self,username):
        self.board.username = username
        self.s.send(username.encode('ascii'))
        self.usernameButton.config(state='disabled')
    '''
    #send move via socket
    def sendMove(self,coords):
        self.clientSocket.send(coords.encode('ascii'))
    #check if game is over
    def gameover(self,playerIcon):
        win = self.board.isWinner(playerIcon)
        tie = self.board.boardIsFull()
        #if the game is over
        if win == True:
            return 'Win'
        elif tie == True:
            return 'Tie'
        else:
            self.enableBoard()
    #recieve a move
    def recieveMove(self,playerIcon):
        #receive the move
        self.turnLabel.config(text = 'Player 1 Turn')
        self.refreshUI()
        move = self.clientSocket.recv(1024).decode('ascii')
        self.board.updateGameBoard(move,'X')
        self.placeIcon(move,'X')
        #check if gameover and then to receive
        self.checkGameOver('X')

    #check game end on each move
    def checkGameOver(self,icon):
        if self.gameover(icon) == 'Win':
            self.playagainActions(icon,'Win')
        elif self.gameover(icon) == 'Tie':
            self.playagainActions('X','Tie')  
        else: #wait for opponent
            if icon == 'O':
                self.recieveMove('O')
            if icon == 'X':
                self.enableBoard()
                self.turnLabel.config(text = 'Player 2 Turn')
                self.refreshUI()
    #playagain
    def playagainActions(self,playerIcon,gameEnd):
        self.board.updateGamesPlayed()
        if gameEnd == 'Win':
            if playerIcon == 'O':
                self.board.updateWins()
                self.board.lastPlayed = self.board.username
            else:
                self.board.updateLosses()
                self.board.lastPlayed = self.board.opponent
        elif gameEnd == 'Tie':
            self.board.updateTies()
            self.board.lastPlayed = self.board.opponent
        #wait for y or n to play again
        confirmation = self.clientSocket.recv(1024).decode('ascii')
        if confirmation == 'y':
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
            self.recieveMove('na')
        else:
            self.printStatistics()
    #update statistics
    def printStatistics(self):
        self.board.username = 'Player 2'
        self.statsLabel.config(text= self.board.printStats())
        self.refreshUI()
    #button presses
    def press11(self):
        currentIcon = self.board11.cget("text")
        if currentIcon == 'X' or currentIcon == 'O':
            messagebox.showinfo("","Invalid move\n\nTry again")
        else:
            icon = 'O'
            move = '0,0'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'O')
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
            icon = 'O'
            move = '0,1'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'O')
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
            icon = 'O'
            move = '0,2'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'0')
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
            icon = 'O'
            move = '1,0'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'O')
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
            icon = 'O'
            move = '1,1'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'O')
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
            icon = 'O'
            move = '1,2'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'O')
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
            icon = 'O'
            move = '2,0'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'O')
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
            icon = 'O'
            move = '2,1'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'O')
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
            icon = 'O'
            move = '2,2'
            self.placeIcon(move,icon)
            self.board.updateGameBoard(move,'O')
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
    #filler
    def drawIcon(self):
        pass
#main loop
if __name__ == '__main__':
    player1 = player2UIPacker()