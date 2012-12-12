import webbrowser
import json
import StringIO

from dropbox import client, rest, session

from localconfig import DROP_KEY, DROP_SECRET, ACCESS_TYPE, ACCESS_KEY, ACCESS_SECRET
from crumble.utils import read_csv

class Dropbox:
    '''
    Initialize a Dropbox session. With the dropbox session
    it is possible to get data from the App specific folder.
    '''
    def __init__(self, folder=''):
        '''initialise class'''
        self.folder = folder
        sess = session.DropboxSession(DROP_KEY, DROP_SECRET, ACCESS_TYPE)
        request_token = sess.obtain_request_token()
        url = sess.build_authorize_url(request_token)
        try:
            access_token = sess.set_token(ACCESS_KEY, ACCESS_SECRET)
            self.client = client.DropboxClient(sess)
            self.metadata = self.client.metadata(self.folder).get('contents')
        except rest.ErrorResponse:
            webbrowser.open(url)
            access_token = sess.obtain_access_token(request_token)
            self.client = client.DropboxClient(sess)
            self.metadata = self.client.metadata(self.folder).get('contents')

    def get_geojson(self):
        '''read geojson files and return geojson'''
        geojsonfiles = {}
        for (counter, file_) in enumerate(self.metadata):
            if counter > 5:
                return geojsonfiles
            #NOTE make the difference between mime types here,
            # in the same loop, don't write a seperate method for csv
            if file_.get('mime_type') == 'application/javascript':
                jsonrequest = self.client.get_file(file_.get('path'))
                geojson = json.load(jsonrequest)
                filename = file_.get('path').split('/')[-1].split('.')[0] #NOTE get the basename properly
                geojsonfiles[filename] = {'data': geojson, 'metadata': file_}
        return geojsonfiles


    def get_csv(self):
        '''read csv files; convert to geojson and return'''
        for (counter, file_) in enumerate(self.metadata):
            csvdata = {}
            if counter > 5:
                return csvdata
            if file_.get('mime_type') == 'text/csv':
                csv_file = self.client.get_file(file_.get('path'))
                csv_string = StringIO.StringIO(csv_file.read())
                csvdata = read_csv(csv_string)
        return csvdata

def main():
    drop_shiz = Dropbox()
    geojson = drop_shiz.get_geojson()
    print geojson
