import webbrowser
import json
import StringIO

from dropbox import client, rest, session

from lemonpie.config import *
from crumble.utils import read_csv

class Dropbox:
    '''
    Initialize a Dropbox session. With the dropbox session
    it is possible to get data from the App specific folder.
    '''
    def __init__(self):
        sess = session.DropboxSession(DROP_KEY, DROP_SECRET, ACCESS_TYPE)
        request_token = sess.obtain_request_token()
        url = sess.build_authorize_url(request_token)
        try:
            access_token = sess.set_token(ACCESS_KEY, ACCESS_SECRET)
            self.client = client.DropboxClient(sess)
            self.metadata = self.client.metadata('/').get('contents')
        except rest.ErrorResponse:
            webbrowser.open(url)
            access_token = sess.obtain_access_token(request_token)
            self.client = client.DropboxClient(sess)
            self.metadata = self.client.metadata('/').get('contents')

    def get_geojson(self):
        for file_ in self.metadata:
            if file_.get('mime_type') == 'application/javascript':
                jsonrequest = self.client.get_file(file_.get('path'))
                geojson = json.load(jsonrequest)
        return geojson


    def get_csv(self):
        for file_ in self.metadata:
            if file_.get('mime_type') == 'text/csv':
                csv_file = self.client.get_file(file_.get('path'))
                csvdata = read_csv(csv_file)
        return geojson.read

def main():
    drop_shiz = Dropbox()
    geojson = drop_shiz.get_csv()
