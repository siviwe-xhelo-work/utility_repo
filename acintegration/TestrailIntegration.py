import json
import re
import requests
import json
from requests.auth import HTTPBasicAuth

BASE_URL = 'https://testrail.absa.co.za/index.php?/api/v2/'
headers={
    'Content-Type': 'application/json'
    }

class TestrailIntegration:
    def __init__(self,username,password):
        global basicAuth
        basicAuth = HTTPBasicAuth(username, password)
    
    #Get a test case by Id
    def get_test_case_by_id(self,test_id):
        response = requests.get(BASE_URL + 'get_case/' + test_id,
                            headers=headers,
                            auth=basicAuth,verify=False)
        print(response.json())

    #Get a results by Id
    def get_result_by_id(self,results_id):
        response = requests.get(BASE_URL + 'get_results/' + results_id,
                            headers=headers,
                            auth=basicAuth,verify=False)
        print(response.json())

    #Get a run by Id
    def get_run_by_id(self,run_id):
        response = requests.get(BASE_URL + 'get_run/' + run_id,
                            headers=headers,
                            auth=basicAuth,verify=False)
        return response.json()

    #Add new result for a particular tescate
    def add_result_for_case(self,result):
        response = requests.post(BASE_URL + 'add_result_for_case/28776/2953464/',
                            headers=headers,
                            auth=basicAuth,verify=False,
                            data={'status_id': 5, 'comment': 'Siviwe 20220603' })
        print(response.json())
    
    def add_result(self,data,test_case_id):
        response =requests.post(BASE_URL + 'add_result/' + test_case_id,
        json=data, 
        auth=basicAuth,
        verify=False)
        return response.json()

