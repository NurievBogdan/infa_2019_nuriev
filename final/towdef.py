import pygame
import os



class Tower:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.width = 0
		self.height = 0
		self.image = None

		self.menu = None

	def draw(self, win):
		"""
		Рисует башню
		"""
		image = self.tower.image
		win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2) )

	#def click(self, X, Y):
		""" 
		Клик по башне; так сказать, ее выбор
		"""
		#if X <= self.x+self.width and X >= self.x:
			#if Y <= self.y + self.height and Y >= self.y:
				#return True
		#return False

	def range(self, r):
		self.range = r 

	def atack(self, enemies):
		"""
		"""
		self.inRange = False
		enemy_in_range = []
		for enemy in enemies:
			x = enemy.x
			y = enemy.y

			distance = math.sqrt((self.x - enemy.img.get_width()/2 - x)**2 + (self.y -enemy.img.get_height()/2 - y)**2)
			if distsnce < self.range:
				self.inRange = True
				enemy_closest.append(enemy)


		enemy_closest = enemy_closest[::-1]

	


