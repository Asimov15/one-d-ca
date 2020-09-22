#!/usr/bin/python
# dz 03/12/2017
# Create 1d cellular automata

import sys
import math
import pygame
from pygame.locals import *

class automata():
	def __init__(self, ruleset):

		#create the screen
		self.window = pygame.display.set_mode((1900, 1200)) 
		pygame.display.set_caption("Rule: {0}".format(ruleset))
		self.window.fill((255,255,255))
		self.length     = 900
		self.linea      = [] 
		self.lineb      = []
		self.rule       = ruleset
		self.stepnum    = 0
		self.pixel_size = 2

		# 1 = black
		# 0 = white

		for i in range(self.length):
			self.linea.append(0)
			self.lineb.append(0)

		# seed with one dot
		self.linea[self.length / 2] = 1

	def output(self):
		a = 0
		for x in self.linea:
			a += 1
			if x == 1:
				pygame.draw.rect(self.window, (0,0,0), 
				(a * self.pixel_size, self.stepnum * self.pixel_size, self.pixel_size, self.pixel_size))

	def get_cell(self,i):
		#wrapper function for getting pixel to handle the boundary.
		boundary_value = 0
		if i < 0:
			return int(self.linea[0])
		elif i >= len(self.linea):
			return int(self.linea[self.length - 1])
		else:
			return int(self.linea[i])

	def get_input(self,i):
		# calculate the pattern code of the three pixels above this pixel
		pattern_code = 0
		cell_value = 0
		for j in range(1,-2,-1):
			cell_value = self.get_cell(i+j)
			pattern_code = pattern_code + cell_value * math.pow(2, 1-j)
		return int(pattern_code)

	def step(self):
		# calculate next line
		for i in range(self.length):
			a = '{0:08b}'.format(self.rule)[7-self.get_input(i)]
			self.lineb[i] = int(a)

		for i in range(self.length):
			self.linea[i] = self.lineb[i]
		self.stepnum += 1

	def run(self,number_steps):
		# perform the automata for n iterations
		self.output()
		print "Rule: {0}".format(self.rule)
		for i in range(number_steps):
			self.step()
			self.output()

		pygame.image.save(self.window,"ca{0:03d}.png".format(self.rule))

pygame.init()

for ruleset_counter in range(256):
	ruleset_obj = automata(ruleset_counter)
	ruleset_obj.run(400)
