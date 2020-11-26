# main.py

#branchapi package
import branchapi
from branchapi.handler import APIHandler, download_csv
#built-in package
import time

PARAMS_DICT  = {'app_id': branchapi.APP_ID}
HEADERS_DICT = {'Content-Type': 'application/json', 'Access-Token': branchapi.ACCESS_TOKEN}

print("Running..")
def main(path_to_save_csv = None):

    api = APIHandler(url=branchapi.URL, payload_filename='payload.json', params= PARAMS_DICT, headers=HEADERS_DICT)

    post_response = api.post_request()
    print(post_response)
    get_response = api.get_request(post_response['export_job_status_url'])
    
    print(get_response)
    

    if 'response_url' in get_response.keys():
        resp_url = get_response['response_url']

    print(download_csv(path_to_save_csv, resp_url))
 
if __name__ == "__main__":
    main(path_to_save_csv='.')