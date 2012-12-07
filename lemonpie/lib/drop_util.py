import webbrowser

from dropbox import client, rest, session

from lemonpie import config

APP_KEY = config.DROP_KEY
APP_SECRET = config.DROP_SECRET

class Dropbox:
    def __init__(self):
        sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
        request_token = sess.obtain_request_token()
        try:
            url = sess.build_authorize_url(request_token)
            access_token = sess.obtain_access_token(request_token)
            self.client = client.DropboxClient(sess)
        except rest.ErrorResponse:
            url = sess.build_authorize_url(request_token)
            webbrowser.open(url)


    def get_geojson(self):
        metadata = self.client.metadata().get('contents')
        for file_ in metadata:
            if file_.get('mime_type') == 'application/javascript':
                geojson = self.client.get_file(file_)
        return geojson.read()
