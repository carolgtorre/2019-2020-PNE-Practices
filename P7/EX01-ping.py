import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMETERS = '?content-type=application/json'

URL = SERVER + ENDPOINT + PARAMETERS

print(f"Server: {SERVER}")
print(f"URL: {URL}")

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + PARAMETERS)
response = connection.getresponse()
print("Response received!:", response.status, response.reason)
answer_decoded = response.read().decode()
# print(type(answer_decoded), answer_decoded)
dict_response = json.loads(answer_decoded)
# print(type(dict_response), dict_response)
if dict_response['ping'] == 1:
    print('PING OK! The data base is running!')
else:
    print('Data base is down!!')