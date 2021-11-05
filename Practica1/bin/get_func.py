import requests
from bs4 import BeautifulSoup
import time

URL = 'https://www.numeroalazar.com.ar/'
GPH_URL = 'https://beebotte.com/dash/ffc47900-38cd-11ec-954b-39d34f82886a'

def getRND():
	response = requests.get(URL)
	content = response.content
	html = BeautifulSoup(content,'html.parser')
	nums = html.find(id="numeros_generados")
	number = float(nums.get_text()[20:26])
	return number

if __name__ == '__main__':
	print('Testing random number funcion.')
	print('Note: Program is in an undefined loop, use CTRL^C to exit.')
	while True:
		num = getRND()
		print(num)
		time.sleep(120)