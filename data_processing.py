# saving and processing data

import csv
from datetime import datetime as dt

def opening_file(month_of):
	return open(month_of, 'a')
	
	
def closing_file(file_name):
	file_name.close()
	
def writing_to_file(file_name, data):
	print(data)
	file_name.write(data + '\n')
	
	

# machine learning?
