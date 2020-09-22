#!/usr/bin/python
# dz 03/12/2017
# Create 1d cellular automata

import sys
import math
import pygame
from pygame.locals import *

class automata():
	def __init__(self, r):

		#create the screen
		self.window = pygame.display.set_mode((1900, 1200)) 
		pygame.display.set_caption("Rule: {0}".format(r))
		
		self.length     = 1000
		self.linea      = []
		self.lineb      = []
		self.rule       = r
		self.rule_truth = []
		self.stepnum    = 0
		self.pixel_size = 2

		# create array based on rule and reverse order Wolfram has defined his rules this way.
		# ie format in big endian
		# 0 = black
		# 1 = white

		# for i in '{0:08b}'.format(self.rule)[::-1]: 
			# if i == "0":
				# self.rule_truth.append(0)
			# else:
				# self.rule_truth.append(1)
				
		for i in range(self.length):
			self.linea.append(0)
			self.lineb.append(0)

		# seed with on dot

		self.linea[self.length / 2] = 1

	def output(self):
		a = 0
		for x in self.linea:
			a += 1
			if x == 1:
				pygame.draw.rect(self.window, (255,255,255), 
				(a * self.pixel_size, self.stepnum * self.pixel_size, self.pixel_size, self.pixel_size))

	def get_cell(self,i):

		#wrapper function for getting pixel to handle the boundary.		
		boundary_value = 0
		if i < 0 or i >= len(self.linea):
			return int(boundary_value)
		else:
			return int(self.linea[i])

	def get_input(self,i):

		# get the value of the the three pixels above this pixel
		x = 0
		for j in range(-1,2):
			x = x + self.get_cell(i+j) * math.pow(2, 1-j)

		return int(x)

	def step(self):

		# calculate next line
		for i in range(self.length):
			self.lineb[i] = '{0:08b}'.format(self.rule)[self.get_input(i)*-1 - 1]

		for i in range(self.length):
			self.linea[i] = self.lineb[i]
		self.stepnum += 1

	def run(self,n):

		# perform the automata for n iterations
		self.output()
		print "Rule: {0}".format(self.rule)
		for i in range(int(n)):
			self.step()
			self.output()

		pygame.image.save(self.window,"ca{0:03d}.png".format(self.rule))

pygame.init()

for ruleset_counter in range(256):
	ruleset_obj = automata(ruleset_counter)
	ruleset_obj.run(500)
