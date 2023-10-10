#gameboard
#gameboard.py
'''The gameboard class contains all functions that modify the gameboard and game statistics.

This module contains a class that each player will use to modify their own gameboard while playing the game
This contains funcitons to update the count of games played, statistics,
reset the game board after a game is completed,
determine is a user inputted move is valid or not,
update the board with a valid user move,
and determine if there is a winning move on the board or if it is full.

Grid uses a coordiante system (list nested in list)
   0   1   2  x
0 [_],[_],[_]
1 [_],[_],[_]
2 [_],[_],[_]
y
'''
from copy import deepcopy
import copy

#include tkinter from the standard library
import tkinter as tk
#impor the ttk names from tkinter
from tkinter import ttk

class BoardClass():
    #constructor, define attributes
    def __init__(self) -> None:
        self.gameboard = [['_','_','_'],['_','_','_'],['_','_','_']]
        self.Newgameboard = [['_','_','_'],['_','_','_'],['_','_','_']]
        self.username = '' #players username
        self.opponent = ''#opponents username
        self.lastPlayed = '' #username of last move
        self.numWins = 0 #Number of wins
        self.numLosses = 0 #Number of losses
        self.numTies = 0 #Number of ties
        self.gamesPlayed = 0 #Number of games played
        self.newboard = copy.deepcopy(self.gameboard) #original board

    #functions
    def updateGamesPlayed(self):
        self.gamesPlayed += 1
    def updateWins(self):
        self.numWins +=1
    def updateTies(self):
        self.numTies +=1    
    def updateLosses(self):
        self.numLosses +=1

    def resetGameBoard(self):
        return copy.deepcopy(self.newboard)

    def updateGameBoard(self,move,icon):
        x = int(move.split(',')[0])
        y = int(move.split(',')[1])
        self.gameboard[x][y] = icon

        #prints the board
        '''
        for i in self.gameboard:
            print(f'{i}')
        print()
        '''

    #Check for win and update win count
    def isWinner(self, icon):
        #horizontal/vertical win
        for i in range(3):
            #horizontal
            if self.gameboard[i][0] == self.gameboard[i][1] == self.gameboard[i][2] == icon:
                return True
            #vertical
            if self.gameboard[0][i] == self.gameboard[1][i] == self.gameboard[2][i] == icon:
                return True
        #diagonals
        if self.gameboard[0][0] == self.gameboard[1][1] == self.gameboard[2][2] == icon:
            return True
        if self.gameboard[0][2] == self.gameboard[1][1] == self.gameboard[2][0] == icon:
            return True

    #Check is the board is full
    def boardIsFull(self):
        openSpots = 0
        for i in range(0,3):
            for j in range(0,3):
                if self.gameboard[i][j] == '_':
                    openSpots += 1
        if openSpots == 0:
            return True #the board is full
        else:
            return False #the board is still open
            #Await a new move

    def printStats(self):
        statistics = f'Username: {self.username}\nOpponent: {self.opponent}\nLast played: {self.lastPlayed}\nNumber of games played: {self.gamesPlayed}\nNumber of wins: {self.numWins}\nNumber of ties: {self.numTies}\nNumber of losses: {self.numLosses}'
        return statistics