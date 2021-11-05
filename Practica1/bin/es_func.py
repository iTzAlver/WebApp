from elasticsearch import Elasticsearch
from datetime import datetime


es = Elasticsearch([{'host': 'localhost', 'port': 9200}], http_auth=('elastic','byBl35zHZlWoKi9Wvhnj'))
LLAVE_CODIGO = 'storeregisterkeymustberandom'

def b_thES(usr,thr):
	query = {'query': {'match_phrase': {'usr':usr}}}
	res = es.search(index=usr, body=query,size=9999)
	res = res['hits']['hits']
	response = [[]]
	for element in res:
		#response.append([element['_source']['usr'], element['_source']['Number'], element['_source']['timestamp']])
		response.append(element['_source']['Number'])
	response.pop(0)
	response2=[[]]
	for element in response:
		if element >= float(thr):
			response2.append(element)
	response2.pop(0)
	if len(response2) > 5:
		response2 = response2[0:5]
	return response2

def delete_all_users():
    search_body = {"from": 0, "size": 10000, "query": {"query_string": {"query": "*"}}}
    for e in es.search(index=LLAVE_CODIGO,body=search_body).get("hits").get("hits"):
        print(e["_type"])
        print(e["_id"])
        es.delete(index=LLAVE_CODIGO, doc_type=e["_type"], id=e["_id"])

def searchLogin(usr, password):
	query = {'query': {'match_phrase': {'usr':usr}}}
	res = es.search(index=LLAVE_CODIGO,body=query)
	res = res['hits']['hits']
	if res == []:
		returned = False
		exitcode = 'no_user'
	else:
		res = res[0]['_source']
		passAuth = res['pass']
		if passAuth == password:
			returned = True
			exitcode = 'sucess'
		else:
			returned = False
			exitcode = 'wrong_pass'
	return [returned, exitcode]

def storeRegister(usr, password):
	[isRegistered, ecode] = searchLogin(usr,password)
	if ecode != 'no_user':
		returned = False
	else:
		cell = {"usr": usr, "pass": password}
		es.index(index=LLAVE_CODIGO,body=cell)
		guardarES(usr,0)
		returned = True
	return returned

def guardarES(usr, number):
	timestamp = datetime.now()
	cell = {"usr": usr, "Number": number, "timestamp": timestamp}
	res = es.index(index=usr, body=cell)
	return res

def b_usrES(usr):
	query = {'query': {'match_phrase': {'usr':usr}}}
	res = es.search(index=usr, body=query,size=1000)
	res = res['hits']['hits']
	response = [[]]
	for element in res:
		#response.append([element['_source']['usr'], element['_source']['Number'], element['_source']['timestamp']])
		response.append(element['_source']['Number'])
	response.pop(0)
	return response

def b_numES(usr,num):
	query = {'query': {'match': {'Number': num}  }
            }
	res = es.search(index=usr, body=query, size=1000)
	res = res['hits']['hits']
	response = [[]]
	for element in res:
		response.append([element['_source']['usr'], element['_source']['Number'], element['_source']['timestamp']])
	response.pop(0)
	return response

def b_timES(usr,timestamp):
	query = {'query': {'match': {'timestamp': timestamp}  }
			}
	res = es.search(index=usr, body=query,size=1000)
	res = res['hits']['hits']
	response = [[]]
	for element in res:
		response.append([element['_source']['usr'], element['_source']['Number'], element['_source']['timestamp']])
	response.pop(0)
	return response

if __name__ == '__main__':
	print("Testing Elastic Search functions:")
	user = "alverciito"
	number = 7
	guardarES(user,number)
	response = b_usrES(user)
	for element in response:
		print(element[1])