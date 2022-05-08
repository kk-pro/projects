import re, requests
import os, sys

# The post data to the blockchain
def blockPost(file,data):
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'content':data,'author':file}

    session = requests.Session()
    session.post('http://127.0.0.1:5000/submit',headers=headers,data=payload)
    requests.get('http://127.0.0.1:8000/mine')

folder_path = sys.argv[1]

def zipf(folder_path):

    folder_path = os.path.abspath(folder_path)

    number = 1
    while True:
        zipfilename= os.path.basename(folder_path)
        if not os.path.exists(zipfilename):
            break
    
    print(f'creating {zipfilename}')
    
    # walking through folders
    for foldername , subfolders , filenames in os.walk(folder_path):
        print(f'Adding files in {foldername}. . . ')

        # adding all files in the folder to blockchain
        for f in filenames:
            fi = open(folder_path+"/"+f, "r")
            data = fi.read()
            blockPost(f,data)
     
zipf(folder_path)
