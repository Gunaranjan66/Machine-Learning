import pygame
import sys
import numpy as np
from pygame.locals import *
class Tic_Tac_Toc:
	def __init__(self,width,height,rows,color=[255,255,255],alpha=0):
		pygame.init()
		self.BLUE=[0,0,255]
		self.width=width
		self.height=height
		self.rows=rows
		self.window=pygame.display.set_mode((width,height+50))
		self.flag=True
		self.color=color
		self.cir=np.random.randint(0,2)
		self.surfBwt=self.width//self.rows
		self.game=np.zeros((self.rows,self.rows))
		self.myMove=(1==self.cir)
		self.ai=1
		self.human=-1
		self.startMove=True
		self.font1 = pygame.font.SysFont(None, 48)
		self.count=0
		self.start()
	def equals3(self,li):
		start=li[0]
		for i in li[1:]:
			if i!=start:
				return False
		return True
	def is_empty3(self,li):
		for i in li:
			if not i:
				return False
		return True
	def check_row_col(self,arr):
		if self.is_empty3(arr):
			if self.equals3(arr):
				return 1
		return 0
	def check_cross(self):
		if self.is_empty3([self.game[0,0],self.game[1,1],self.game[2,2]]):
			if self.equals3([self.game[0,0],self.game[1,1],self.game[2,2]]):
				return 1
		if self.is_empty3([self.game[0,2],self.game[1,1],self.game[2,0]]):
			if self.equals3([self.game[0,2],self.game[1,1],self.game[2,0]]):
				return 1
		return 0
	def game_winner(self):
		for i in range(self.rows):
			if (self.check_row_col(self.game[i])):
				return self.game[i,0]
			if  self.check_row_col(self.game[:,i]):
				return self.game[0,i]
		if self.check_cross():
			return self.game[1,1]
		return self.game_draw()
    		
	def draw_X(self,x,y):
		pos_x=(x*self.surfBwt)
		pos_y=y*self.surfBwt
		pygame.draw.line(self.window,self.color,[pos_x+10,pos_y+10],[pos_x+self.surfBwt-10,pos_y+self.surfBwt-10],2)
		pygame.draw.line(self.window,self.color,[pos_x-10+self.surfBwt,pos_y+10],[pos_x+10,pos_y+self.surfBwt-10],2)
	def draw_circle(self,x,y):
		center=[x*self.surfBwt+self.surfBwt//2,y*self.surfBwt+self.surfBwt//2]
		pygame.draw.circle(self.window,self.color,center,(self.surfBwt//2)-10,2)
	def game_draw(self):
		for i in range(len(self.game)):
			for j in range(len(self.game[i])):
				if not self.game[i,j]:
					return -2
		return 0
#Min Max Algorithm
	def minmax(self,maxPlayer):
		res_score=self.game_winner()
		if not res_score==-2:
			return res_score
		elif maxPlayer:
			bestScore=-np.inf
			for i in range(3):
				for j in range(3):
					if not self.game[i,j]:
						self.game[i,j]=self.ai
						score=self.minmax(False)
						self.game[i,j]=0
						bestScore=max(score,bestScore)
			return bestScore
		else:
			bestScore=np.inf
			for i in range(3):
				for j in range(3):
					if not self.game[i,j]:
						self.game[i,j]=self.human
						score=self.minmax(True)
						self.game[i,j]=0
						bestScore=min(score,bestScore)
			return bestScore
	def best_move(self):
		bestScore=-np.inf
		bestPos=False
		if self.startMove:
			self.startMove=False
			x,y=[np.random.randint(0,3),np.random.randint(0,3)]
			while  self.game[x,y]:
				x,y=[np.random.randint(0,3),np.random.randint(0,3)]
			return [x,y]
		for i in range(len(self.game)):
			for j in range(len(self.game[i])):
				if not self.game[i,j]:
					self.game[i,j]=self.ai
					score=self.minmax(False)
					self.game[i,j]=0
					if score>bestScore:
						bestScore=score
						bestPos=[i,j]
		return bestPos
	def drawGrid(self):
		x=0
		y=0
		for i in range(self.rows+1):
			pygame.draw.line(self.window,[128,128,128],[x,0],[x,self.width])
			pygame.draw.line(self.window,[128,128,128],[0,y],[self.height,y])
			x+=self.surfBwt
			y+=self.surfBwt
	def start(self):
		while self.flag:
			for event in pygame.event.get():
				#---------------- IF The User want to Quit ------------------------------------#
				if event.type==pygame.QUIT:
					pygame.quit()
					sys.exit(0)
				#---------------------------- END ------------------------------------#


				#-----------------------  User Move  ------------------------------------#
				if self.myMove:
					if event.type==pygame.MOUSEBUTTONDOWN:
						x,y=pygame.mouse.get_pos()
						x=x//self.surfBwt
						y=y//self.surfBwt
						if not self.game[y,x]:
							if self.cir:
								self.draw_circle(x,y)
								self.cir=0
								self.game[y,x]=self.human
								self.myMove=False
								
				#---------------------------- END ------------------------------------#

				#-----------------------  System Move  ------------------------------------#
				else:
					x=self.best_move()
					if x :
						self.draw_X(x[1],x[0])
						self.cir=1
						self.game[x[0],x[1]]=1
						self.myMove=True
				#---------------------------- END ------------------------------------ #
			# ----------------------------- Check Conditions ---------------------------- #
			if self.game_winner()!=-2:
				res=self.game_winner()
				if res==-1:
					out="Human Win"
				elif res==1:
					out="System Win"
				else:
					out="Draw"
				self.img1 = self.font1.render(out , True, self.BLUE)
				self.window.blit(self.img1,(10,self.height+10))
				self.flag=False

			#---------------------------- END ------------------------------------#
			self.drawGrid()

			pygame.display.update()
		while 1:
			for event in pygame.event.get():
				#---------------- IF The User want to Quit ------------------------------------#
				if event.type==pygame.QUIT:
					pygame.quit()
					sys.exit(0)

def main():
    cordinate=Tic_Tac_Toc(360,360,3,[255,255,255],0)
main()
