from beebotte import *
from datetime import datetime

APP_KEY = "c6E2ubuPxfpDNAQT5LkCV4Sg"
SECRET_KEY = "rTqVftLgkS5na2G80dAFKE0NTh6egjLl"
bclient = BBT(APP_KEY, SECRET_KEY)

def guardarBB(cliente, usr, num):
	timestamp = datetime.now()
	chname = str(timestamp)
	bclient.write('databasetest','timestamp', chname)
	bclient.write('databasetest','number', num)
	bclient.write('databasetest','usr', usr)
	return 0

def leerBB(cliente,param):
	response = bclient.read('databasetest',param,limit=25)
	reta = []
	ret = []
	for element in response:
		ret.append(element['data'])
	ret.pop(0)
	return ret


if __name__ == '__main__':
	print('Testing Beebotte functions.')
	guardarBB(bclient, 'alverciito', 3)
	response = leerBB(bclient, 'number')
	for element in response:
		print(element)
