import socket
import time
import math

import subprocess, sys


from datetime import datetime as dt

from data_processing import writing_to_file, closing_file, opening_file


def run_script():
	p = subprocess.Popen(["powershell.exe", 
              "./notification.ps1"], 
              stdout=sys.stdout)
	p.communicate()

def send_data(socket_num):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = '192.168.5.198'
	print(host)
	port = int(socket_num)

	s.connect((host, port))

	exit_condition = True;

	month_of = str(dt.now().month) + '_' + str(dt.now().year) + '.csv'

	counter = 0
	temp_counter = 0

	while(exit_condition):
		if(month_of != str(dt.now().month) + '_' + str(dt.now().year) + '.csv'):
			closing_file(f)
			f = opening_file(month_of = str(dt.now().month) + '_' + str(dt.now().year) + '.csv')
		
		
		
		data = s.recv(1024).decode('utf-8')
		#print('data: ', data[-1])
		
		
		if(int(data[-1]) == 1):
			counter += 1
			unseated_counter = 0
		
		elif(int(data[-1]) == 0):
			unseated_counter += 1
			if(unseated_counter == 2):
				k = open('sessions.csv', 'a')
				session_string = str(dt.now())[:-16] + ' : ' + str(counter)
				writing_to_file(k, session_string)
				counter = 0
		
		if(((counter % 30) == 0) and counter != 0):
			closing_file(f)
			g = open('notification.ps1', 'w')
			hour = math.floor(counter/60)
			minute = counter % 60
			stringTemp1 = 'New-BurntToastNotification -Text "You have been sitting for '
			stringTemp2 = ' hour(s) and '
			stringTemp3 = ' minutes straight "
			g.write(stringTemp1 + str(hour) + stringTemp2 + str(minute) + stringTemp3)
			g.close()
			
			run_script()
			
		#print(counter)	
						
		f = opening_file(month_of)
		writing_to_file(f, str(data))
		closing_file(f)
		
		
		
			
		
		
	s.close()
 
 

send_data(input())



