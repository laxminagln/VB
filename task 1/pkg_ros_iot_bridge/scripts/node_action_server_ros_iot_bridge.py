import requests

URL = "https://script.google.com/macros/s/AKfycbzbuynqMRUxELtCYGSv23gepkxy6FG_ij9xxC91AsF6ufbvLnY/exec"

def myFun(n):
	for i in range(n):
		value = int(input("Enter value : "))
		parameters = {"id":"Sheet1", "value":value} 
		response = requests.get(URL, params=parameters)
		print(response.content)

if __name__ == '__main__':
	n = input("Number = ")
	myFun(n)

