from flask import Flask, redirect, render_template, request, url_for
import re
import requests
import os
from time import time
from multiprocessing.pool import ThreadPool

##url = 'https://www.python.org/static/img/python-logo@2x.png'

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




def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True
url = 'http://aviaryan.in/images/profile.png'
def filename(url):
    if url.find('/'):
      return url.rsplit('/', 1)[1]


def url_response(url):
    path,url = url
    name = filename(url)
    #print('c:/users/AVINASH/Desktop/html/' + path)
    path1 = 'c:/users/AVINASH/Desktop/html/'+ path+".png"
    r = requests.get(url, stream = True, allow_redirects=True)
    with open(path1, 'wb') as f:
        for ch in r:
            f.write(ch)


def download(url):
    print('Beginning file download with requests')
    if type(url) is str:
        r = requests.get(url)
        name=filename(url)
        with open('c:/users/AVINASH/Desktop/html/'+name, 'wb') as f:
            f.write(r.content)

        # Retrieve HTTP meta-data
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        start = time()
        print(f"Time to download: {time() - start}")

        
    elif type(url) is list:
        start = time()
        for x in url:
            url_response (x)
        print(f"Time to download: {time() - start}")

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def home():
    return redirect(url_for('download_me'))
    
@app.route('/download/<path:fileaddress>', methods = ['GET','POST'])
def download_me(fileaddress):
    download(fileaddress)
    return render_template("in.html")
    
if __name__ == '__main__':
        app.run(debug= True, host = "0.0.0.0",port=80) 
