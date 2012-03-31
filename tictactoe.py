#!/penis
# -*- encoding: utf-8 -*-

import os
import sys
import time

"""
+-----------------+
|  X  |  X  |  X  |
+-----------------+
|  X  |  O  |  X  |
+-----------------+
|  X  |  X  |  X  |
+-----------------+
=> 9 Felderd
"""

class TicTacToe():
	def __init__(self):
		self.spieler_zug = 0# spieler 1 (spieler2 => 1)
		self.SpielEnde = 0
		self.spiel_zuege = 0
		if len(sys.argv) >= 2: self.name_1 = sys.argv[1]
		else: self.name_1 = "Spieler 1"
		if len(sys.argv) >= 3: self.name_2 = sys.argv[2]
		else: self.name_2 = "Spieler 2"
		self.Feld = {
		 1: ["1", "2", "3"],
		 2: ["4", "5", "6"],
		 3: ["7", "8", "9"]
		}

		
	def generiere_feld(self):
		print u"\t\t\t      by pascal :D"
		print "\t\t%s\t\tgegen\t\t%s" % (self.name_1, self.name_2)
		print "\t\t+-----------+-----------+-----------+"
		print "\t\t|           |           |           |"
		print "\t\t|     %s     |     %s     |     %s     |" % (self.Feld[1][0],self.Feld[1][1],self.Feld[1][2])
		print "\t\t|           |           |           |"
		print "\t\t+-----------+-----------+-----------+"
		print "\t\t|           |           |           |"
		print "\t\t|     %s     |     %s     |     %s     |" % (self.Feld[2][0],self.Feld[2][1],self.Feld[2][2])
		print "\t\t|           |           |           |"
		print "\t\t+-----------+-----------+-----------+"
		print "\t\t|           |           |           |"
		print "\t\t|     %s     |     %s     |     %s     |" % (self.Feld[3][0],self.Feld[3][1],self.Feld[3][2])
		print "\t\t|           |           |           |"
		print "\t\t+-----------+-----------+-----------+"
	
	def setzeFeldX(self, reihe="", position=""):
		print "\t\t\t%s ist am Zug.\n\n" % (self.name_1)
		self.zahlenFeld("X")
	
	def setzeFeldO(self, reihe="", position=""):
		print "\t\t\t%s ist am Zug.\n\n" % (self.name_2)
		self.zahlenFeld("O")
				
	def zahlenFeld(self, stein):
		Map = {
		1:"1,0",
		2:"1,1",
		3:"1,2",
		4:"2,0",
		5:"2,1",
		6:"2,2",
		7:"3,0",
		8:"3,1",
		9:"3,2"
		}
		while True:		
			feld = input("\tAuf welches Feld moechtest du deinen Stein setzen?: ")
			if Map.has_key(feld):
				if self.Feld[int(Map[feld].split(",")[0])][int(Map[feld].split(",")[1])].isdigit() == True: break
				

		self.Feld[int(Map[feld].split(",")[0])][int(Map[feld].split(",")[1])] = stein
		
	def m(self, reihe, position):
		return self.Feld[reihe][position]
	def endgame(self):
		print "\n\t\tSieger ist: %s" % (str(self.spieler_zug).replace("1", self.name_1).replace("0", self.name_2))
		self.SpielEnde = 1
					
	def pruefe_Spielfeld(self):
		
		
		if self.m(1,0) == self.m(1,0) and self.m(1,1) == self.m(1,0) and self.m(1,2) == self.m(1,0): self.endgame() # reihe 1
		elif self.m(2,0) == self.m(1,0) and self.m(2,1) == self.m(1,0) and self.m(2,2) == self.m(2,0):  self.endgame()# reihe2.
		elif self.m(3,0)  == self.m(3,0) and self.m(3,1)  == self.m(3,0) and self.m(3,2) == self.m(3,0):  self.endgame()# reihe3.
		
		elif self.m(1,0) == self.m(1,0) and self.m(2,0) == self.m(1,0) and self.m(3,0) == self.m(1,0):  self.endgame()# spalte1
		elif self.m(1,1) == self.m(1,1) and self.m(2,1) == self.m(1,1) and self.m(3,1) == self.m(1,1):  self.endgame()# spalte2
		elif self.m(1,2) == self.m(1,2) and self.m(2,2) == self.m(1,2) and self.m(3,2) == self.m(1,2):  self.endgame()# spalte3
		
		elif self.m(1,0)  == self.m(1,0) and self.m(2,1)  == self.m(1,0) and self.m(3,2) == self.m(1,0): self.endgame()#\
		elif self.m(1,2) == self.m(1,2) and self.m(2,1) == self.m(1,2) and self.m(3,0) == self.m(1,2): self.endgame()#/
		
	
	def spielerFeld(self):
		
		if self.spieler_zug == 1:#spieler 2
			self.setzeFeldO()
			self.spieler_zug = 0
		else:
			self.setzeFeldX()
			self.spieler_zug = 1
		
if __name__ == "__main__":
	os.system("clear")
	MeinSpiel = TicTacToe()
	MeinSpiel.generiere_feld()
	start_time = time.time()
	while True:
		MeinSpiel.spiel_zuege += 1
		if MeinSpiel.spiel_zuege >= 10:
			print "\t\t\tUNENTSCHIEDEN"
			break
		MeinSpiel.spielerFeld()
		os.system("clear")
		MeinSpiel.generiere_feld()
		MeinSpiel.pruefe_Spielfeld()
		if MeinSpiel.SpielEnde == 1: 
			print "Das Spiel hat %s Sekunden gedauert." % (round(time.time() - start_time))
			break
