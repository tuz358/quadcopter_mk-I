#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import os
import time
import datetime
import socket

file = open('/dev/input/js0','r')	# DualShock3
data = []
LLR = 20		# Left analog stick Left - Right
LUD = 120		# Left analog stick UP - DOWN 
RLR = 100		# Right analog stick Left - Right
RUD = 0			# Right analog stick UP - DOWN

mode = "wait"
before_time = 0
now_time = 0


s = socket.socket()
s.connect(('192.168.5.1',50000))		# Quadcopter's IP address
print('Connecting Successful.')

Throttle = 0
Roll = 0
Pitch = 0
Yaw = 0
R_Sign = '+'
P_Sign = '+'
Y_Sign = '+'

while 1:
        for character in file.read(1):
        	data += ['%02X' % ord(character)]
		if len(data) == 8:
			if data[6] == '01':
				mode = "button" 
				if data[4] == '01': #pressed button
					if data[7] == '00': # SELECT
						sys.stdout.write('You pressed the SELECT button\n')
						
						
					elif data[7] == '01': #L3
						sys.stdout.write('You pressed the L3 button\n')
						

					elif data[7] == '02': #R3
						sys.stdout.write('You pressed the R3 button\n')
						
					
					elif data[7] == '03': #START
						sys.stdout.write('You pressed the START button\n')
						
					
					elif data[7] == '04': #UP	
						sys.stdout.write('You pressed the UP button\n')
					
					elif data[7] == '05': #RIGHT
						sys.stdout.write('You pressed the RIGHT button\n')
					
					elif data[7] == '06': #DOWN	
						sys.stdout.write('You pressed the DOWN button\n')
					
					elif data[7] == '07': #LEFT	
						sys.stdout.write('You pressed the LEFT button\n')
					
					elif data[7] == '08': #L2	
						sys.stdout.write('You pressed the L2 button\n')
						time.sleep(0.11)
					
					elif data[7] == '09': #R2	
						sys.stdout.write('You pressed the R2 button\n')
						time.sleep(0.11)
					
					elif data[7] == '0A': #L1	
						sys.stdout.write('You pressed the L1 button\n')
						time.sleep(0.11)
					
					elif data[7] == '0B': #R1
						sys.stdout.write('You pressed the R1 button\n')
						time.sleep(0.11)
					
					elif data[7] == '0C': #TRIANGLE	
						sys.stdout.write('You pressed the TRIANGLE button\n')
					
					elif data[7] == '0D': #CIRCLE	
						sys.stdout.write('You pressed the CIRCLE button\n')
					
					elif data[7] == '0E': #CROSS	
						sys.stdout.write('You pressed the CROSS button\n')
					
					elif data[7] == '0F': #SQUARE	
						sys.stdout.write('You pressed the SQUARE button\n')
					

				elif data[4] == '00': #released button
					
					if data[7] == '00': # SELECT
						sys.stdout.write('You released the SELECT button\n')
					elif data[7] == '01': #L3
						sys.stdout.write('You released the L3 button\n')
					elif data[7] == '02': #R3
						sys.stdout.write('You released the R3 button\n')
					elif data[7] == '03': #START
						sys.stdout.write('You released the START button\n')
					elif data[7] == '04': #UP	
						sys.stdout.write('You released the UP button\n')
					elif data[7] == '05': #RIGHT
						sys.stdout.write('You released the RIGHT button\n')	
					elif data[7] == '06': #DOWN
						sys.stdout.write('You released the DOWN button\n')
					elif data[7] == '07': #LEFT
						sys.stdout.write('You released the LEFT button\n')
					elif data[7] == '08': #L2
						time.sleep(0.11)
						sys.stdout.write('You released the L2 button\n')
					elif data[7] == '09': #R2	
						time.sleep(0.11)
						sys.stdout.write('You released the R2 button\n')
					elif data[7] == '0A': #L1
						time.sleep(0.11)
						sys.stdout.write('You released the L1 button\n')
					elif data[7] == '0B': #R1
						time.sleep(0.11)
						sys.stdout.write('You released the R1 button\n')
					elif data[7] == '0C': #TRIANGLE
						sys.stdout.write('You released the TRIANGLE button\n')
					elif data[7] == '0D': #CIRCLE
						sys.stdout.write('You released the CIRCLE button\n')
					elif data[7] == '0E': #CROSS
						sys.stdout.write('You released the CROSS button\n')
					elif data[7] == '0F': #SQUARE
						sys.stdout.write('You released the SQUARE button\n')
			elif data[6] == '02':
				
				now = datetime.datetime.now()
				now_time = now.minute * 60000 + now.second * 1000 + now.microsecond/1000
				a_data = int(data[5],16)
				if a_data >= 0 and a_data < 128:
					a_data = a_data + 128
				elif a_data >= 128 and a_data < 256:
					a_data = a_data - 128


				if data[7] == '00':	#Left stick L-R		PS06
					#a_data = (int(a_data/2.13) - 120) * -1
					#a_data =int(( a_data - 60) * 1.66 + 20)
					#if a_data <= 20:
					#	a_data = 20
					LLR = a_data - 128
					joy = True
					mode = "analog"
					data = [str(int(x,16)) for x in data]
					sys.stdout.write('LLR ' + str(a_data) + '\n')
					Yaw = int(abs(LLR * (100/256.0)))
					#sys.stdout.write('L ' + str(a_data) + '\n')
							
				elif data[7] == '01':	#Left stick U-D		PS05
					#a_data = int(a_data/2.13)
					#a_data = a_data * 2
					#if a_data >= 120:
					#	a_data = 120
					LUD = -1*(a_data - 128)
					joy = True
					mode = "analog"
					data = [str(int(x,16)) for x in data]
					#sys.stdout.write('L ' + ' '.join(data[4:6]+list(str(a_data))) + '\n')
					sys.stdout.write('LUD ' + str(a_data) + '\n')
					Throttle = int(LUD * (100/256.0))
					
				elif data[7] == '02':	#Right stick L-R	PS03
					#a_data = (int(a_data/2.13) - 120) * -1
					#a_data = int(a_data * 1.66)
					#if a_data >= 100:
					#	a_data = 100
					RLR = a_data - 128
					joy = True
					mode = "analog"
					data = [str(int(x,16)) for x in data]
					#sys.stdout.write('R ' + ' '.join(data[4:6]+list(str(a_data))) + '\n')
					Roll = int(abs(RLR * (100/256.0)))
					sys.stdout.write('RLR ' + str(a_data) + '\n')
					
				elif data[7] == '03':	#Right stick U-D	PS02
					#a_data = (int(a_data/2.13) - 120) * -1
					#a_data = (a_data - 60 ) * 2
					#if a_data <= 0:
					#	a_data = 0
					RUD = -1*(a_data - 128)
					joy = True
					mode = "analog"
					#data = str(int(data[4]+data[5],16))
					data = [str(int(x,16)) for x in data]
					#sys.stdout.write('R ' + ' '.join(data[4:6]+list(str(a_data))) + '\n')
					Pitch = int(abs(RUD * (100/256.0)))
					sys.stdout.write('RUD ' + str(a_data) + '\n')
					
				else:
					joy = False
				dif = now_time - before_time
				if dif > 110 and joy == True:
					
					now = datetime.datetime.now()
					before_time = now.minute * 60000 + now.second * 1000 + now.microsecond/1000
			
			if RLR >= 0:
			    R_Sign = '+'
			else:
			    R_Sign = '-'
			if RUD >= 0:
			    P_Sign = '+'
			else:
			    P_Sign = '-'
			if LLR >= 0:
			    Y_Sign = '+'
			else:
			    Y_Sign = '-'

			pkt = 'T' + str(Throttle).zfill(3)
			pkt += 'R' + R_Sign + str(Roll).zfill(3)
			pkt += 'P' + P_Sign + str(Pitch).zfill(3)
			pkt += 'Y' + Y_Sign + str(Yaw).zfill(3)
			s.send(pkt)

			sys.stdout.flush()
			data = []			
	now = datetime.datetime.now()
	j_time = now.minute * 60000 + now.second * 1000 + now.microsecond/1000
	dif = j_time - before_time
	if dif > 200 and mode == "analog":
		now = datetime.datetime.now()
		before_time = now.minute * 60000 + now.second * 1000 + now.microsecond/1000
sys.stdout.flush()
data = []        
