import webbrowser
import json
#import StringIO

from dropbox import client, rest, session

from localconfig import DROP_KEY, DROP_SECRET, ACCESS_TYPE, ACCESS_KEY, ACCESS_SECRET
from crumble.utils import read_csv

class Dropbox:
    '''
    Initialize a Dropbox session. With the dropbox session
    it is possible to get data from the App specific folder.
    '''
    def __init__(self):
        '''initialise class'''
        sess = session.DropboxSession(DROP_KEY, DROP_SECRET, ACCESS_TYPE)
        request_token = sess.obtain_request_token()
        url = sess.build_authorize_url(request_token)
        try:
            access_token = sess.set_token(ACCESS_KEY, ACCESS_SECRET)
            self.client = client.DropboxClient(sess)
            self.metadata = self.client.metadata('/').get('contents')
            print self.metadata
        except rest.ErrorResponse:
            webbrowser.open(url)
            #import ipdb; ipdb.set_trace()
            access_token = sess.obtain_access_token(request_token)
            self.client = client.DropboxClient(sess)
            self.metadata = self.client.metadata('/').get('contents')

    def get_geojson(self):
        '''read geojson files and return geojson'''
        for file_ in self.metadata:
            if file_.get('mime_type') == 'application/javascript':
                jsonrequest = self.client.get_file(file_.get('path'))
                geojson = json.load(jsonrequest)
        return geojson


    def get_csv(self):
        '''read csv files; convert to geojson and return'''
        for file_ in self.metadata:
            if file_.get('mime_type') == 'text/csv':
                csv_file = self.client.get_file(file_.get('path'))
                csvdata = read_csv(csv_file)
        return csvdata

def main():
    drop_shiz = Dropbox()
    geojson = drop_shiz.get_geojson()
    print geojson
