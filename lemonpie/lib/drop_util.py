import webbrowser
import json

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
        try:
            url = sess.build_authorize_url(request_token)
            access_token = sess.obtain_access_token(request_token)
            self.client = client.DropboxClient(sess)
            metadata = self.client.metadata('/').get('contents')
        except rest.ErrorResponse:
            url = sess.build_authorize_url(request_token)
            webbrowser.open(url)
            raw_input()
            access_token = sess.obtain_access_token(request_token)
            self.client = client.DropboxClient(sess)
            self.metadata = self.client.metadata('/').get('contents')

    def get_geojson(self):
        for file_ in self.metadata:
            if file_.get('mime_type') == 'application/javascript':
                geojson = self.client.get_file(file_.get('path'))

        return geojson.read()


    def get_csv(self):
        for file_ in self.metadata:
            if file_.get('mime_type') == 'text/csv':
                csv_file = self.client.get_file(file_.get('path'))
                import ipdb;ipdb.set_trace()
                csvdata = read_csv(csv_file)
        return geojson.read

def main():
    drop_shiz = Dropbox()
    geojson = drop_shiz.get_csv()
