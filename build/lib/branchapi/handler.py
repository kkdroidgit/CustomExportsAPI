# handler.py

# built-in packages
from importlib import resources
from urllib.request import urlopen
import os
import json
import time
from datetime import datetime
import requests


# branchapi packages
import branchapi
from branchapi.utils import read_json_data, is_valid_url, random_string

class APIHandler(object):
    
    def __init__(self, url:str, payload_filename:str, params:dict, headers:dict):

        if is_valid_url(url):
            self.url = url
        else:
            raise NotImplementedError("URL is not valid")
    
        self.payload = self._read_payload(payload_filename)
        self.params = params
        self.headers = headers

    def _read_payload(self, filename):
        with resources.path('branchapi', filename) as path:
            payload_file_location = path
        
        return json.dumps(read_json_data(payload_file_location))

    def post_request(self):
        post_resp = requests.post(self.url, params=self.params, data=self.payload, headers=self.headers)
        return post_resp.json()

    def get_request(self, url):
        get_resp = requests.get(url, headers=self.headers).json()
        while get_resp['status'] != 'complete':
            print(get_resp)
            time.sleep(5)
            get_resp = requests.get(url, headers=self.headers).json()
        
        return get_resp
    
def download_csv(csv_filepath:str, getURL:str):
    filename = '{}.csv'.format(random_string(6))
    with open(os.path.join(csv_filepath, filename), 'wb') as file:
        obj = urlopen(getURL)
        file.write(obj.read())

    return 'Successfully downloaded: {}'.format(os.path.join(csv_filepath, filename))

if __name__ == "__main__":
    PARAMS_DICT  = {'app_id': branchapi.APP_ID}
    HEADERS_DICT = {'Content-Type': 'application/json', 'Access-Token': branchapi.ACCESS_TOKEN}

    api = APIHandler(url=branchapi.URL, payload_filename='payload.json', params= PARAMS_DICT, headers=HEADERS_DICT)

    post_response = api.post_request()
    print(post_response)
    get_response = api.get_request(post_response['export_job_status_url'])
    print(get_response)