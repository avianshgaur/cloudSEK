from flask import Flask, redirect, render_template, request, url_for
import re
import requests
import os
from time import time
from multiprocessing.pool import ThreadPool
####input for singlr thread
##url = 'https://www.python.org/static/img/python-logo@2x.png'

####input for multi thread

##urls = [("Event1", "https://www.python.org/events/python-events/805/"),
##
##("Event2", "https://www.python.org/events/python-events/801/"),
##
##("Event3", "https://www.python.org/events/python-events/790/"),
##
##("Event4", "https://www.python.org/events/python-events/798/"),
##
##("Event5", "https://www.python.org/events/python-events/807/"),
##
##("Event6", "https://www.python.org/events/python-events/807/"),
##
##("Event7", "https://www.python.org/events/python-events/757/"),
##
##("Event8", "https://www.python.org/events/python-user-group/816/")]
##




##names the file
def filename(url):
    if url.find('/'):
      return url.rsplit('/', 1)[1]

#for multithread
def url_response(url):
    path,url = url
    name = filename(url)
        
    ##path1 = '<address of downloading directory>'+ path+".png"
    path1 = 'https://github.com/avianshgaur/cloudSEK/tree/master/1/downloaded/'+ path+".png"
    r = requests.get(url, stream = True, allow_redirects=True)
    with open(path1, 'wb') as f:
        for ch in r:
            f.write(ch)

##main download function
def download(url):
    print('Beginning file download with requests')
    if type(url) is str:
        r = requests.get(url)
        name=filename(url)
        ##with open('<address of downloading directory>'+name, 'wb') as f:
        with open('https://github.com/avianshgaur/cloudSEK/tree/master/1/downloaded'+name, 'wb') as f:
            f.write(r.content)

        # Retrieve HTTP meta-data
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        start = time()
        print(f"Time to download: {time() - start}")

    ##if url is a list then this will execute multithread download    
    elif type(url) is list:
        start = time()
        for x in url:
            url_response (x)
        print(f"Time to download: {time() - start}")

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def home():
    return render_template("in.html")
    
@app.route('/download/<path:fileaddress>', methods = ['GET','POST'])
def download_me(fileaddress):
    download(fileaddress)
    return render_template("in.html")
    
if __name__ == '__main__':
        app.run(debug= True, host = "0.0.0.0",port=80) 
