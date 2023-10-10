#GUI test
#tkinter
import tkinter as tk
from tkinter import ttk
#gameboard
import gameboard

class BoardPacker():
    #variables
    icon11 = '_'
    icon12 = '_'
    icon13 = '_'
    icon21 = '_'
    icon22 = '_'
    icon23 = '_'
    icon31 = '_'
    icon32 = '_'
    icon33 = '_'
    turn = 'Player 1 Turn'
    play = False


    def __init__(self):
        #initilize gameboard class variable
        self.board = gameboard.BoardClass()
        
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
        self.createConnectcombobox()

        #create board
        if self.play == True:
            self.createBoard1_1(self.icon11)
            self.createBoard1_2(self.icon12)
            self.createBoard1_3(self.icon13)
            self.createBoard2_1(self.icon21)
            self.createBoard2_2(self.icon22)
            self.createBoard2_3(self.icon23)
            self.createBoard3_1(self.icon31)
            self.createBoard3_2(self.icon32)
            self.createBoard3_3(self.icon33)
        #turn label
        self.createTurnLabel(self.turn)
        #run
        self.runUI()

    def canvasSetup(self):
        #initialize canvas
        self.master = tk.Tk()
        #Title
        self.master.title('TIC TAC TOE')
        #window size
        self.master.geometry('400x600')
        
    def initTKVariables(self):
        self.port = tk.IntVar()
        self.IPaddress = tk.StringVar()
        self.options = tk.StringVar()

    def refreshUI(self):
        self.master.update()

    def runUI(self):
        #event handler
        self.master.mainloop()

    #widget functions
    #Port
    def createPortLabel(self):
        self.portLabel = tk.Label(self.master, text="Please enter port #", font=("Arial", 16), fg="black", bg="white")
        self.portLabel.pack()
    def createPortEntry(self):
        self.portEntry = tk.Entry(self.master, textvariable= self.port)
        self.portEntry.pack()
    #IP address
    def createIPaddressLabel(self):
        self.IPaddressLabel = tk.Label(self.master, text="Please enter IP address", font=("Arial", 16), fg="black", bg="white")
        self.IPaddressLabel.pack()
    def createIPaddressEntry(self):
        self.IPaddressEntry = tk.Entry(self.master, textvariable= self.IPaddress)
        self.IPaddressEntry.pack()
    #Conection using port and IP address
    def createConnectButton(self):
        self.connectButton = tk.Button(self.master, text='Connect', command= self.attemptConnection).pack()
    
    #attempt connection again
    def createConnectcombobox(self):
        options = ['Yes','No']
        self.options.set('Reconenct?')
        self.optionsCombobox = ttk.Combobox(self.master, textvariable=self.options, values= options).pack()
    
    #label for player turn
    def createTurnLabel(self, turn):
        self.turnLabel = tk.Label(self.master, text= turn, font=("Arial", 16), fg="black", bg="white")
        self.turnLabel.pack()
    #create 3X3 board for Tic Tac Toe
    #(1,1)
    def createBoard1_1(self,icon11):
        self.board11 = tk.Button(self.master, text= icon11, command= self.drawIcon)
        self.board11.place(x=125,y=200)
    #(1,2)
    def createBoard1_2(self,icon12):
        self.board12 = tk.Button(self.master, text= icon12, command= self.drawIcon)
        self.board12.place(x=175,y=200)
    #(1,3)
    def createBoard1_3(self,icon13):
        self.board13 = tk.Button(self.master, text= icon13, command= self.drawIcon)
        self.board13.place(x=225,y=200)
    #(2,1)
    def createBoard2_1(self,icon21):
        self.board21 = tk.Button(self.master, text= icon21, command= self.drawIcon)
        self.board21.place(x=125,y=250)
    #(2,2)
    def createBoard2_2(self,icon22):
        self.board22 = tk.Button(self.master, text= icon22, command= self.drawIcon)
        self.board22.place(x=175,y=250)
    #(2,3)
    def createBoard2_3(self,icon23):
        self.board23 = tk.Button(self.master, text= icon23, command= self.drawIcon)
        self.board23.place(x=225,y=250)
    #(3,1)
    def createBoard3_1(self,icon31):
        self.board31 = tk.Button(self.master, text= icon31, command= self.drawIcon)
        self.board31.place(x=125,y=300)
    #(3,2)
    def createBoard3_2(self,icon32):
        self.board32 = tk.Button(self.master, text= icon32, command= self.drawIcon)
        self.board32.place(x=175,y=300)
    #(3,3)
    def createBoard3_3(self,icon33):
        self.board33 = tk.Button(self.master, text= icon33, command= self.drawIcon)
        self.board33.place(x=225,y=300)


    #attempt connections to sockets
    def attemptConnection(self):
        pass
    #change the icon of the button after a move is placed
    def drawIcon(self):
        pass

if __name__ == '__main__':
    ticTac = BoardPacker()
    