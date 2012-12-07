import webbrowser

from dropbox import client, rest, session

from lemonpie import config

APP_KEY = config.DROP_KEY
APP_SECRET = config.DROP_SECRET

# ACCESS_TYPE should be 'dropbox' or 'app_folder' as configured for your app
ACCESS_TYPE = 'app_folder'

def main():
    sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
    request_token = sess.obtain_request_token()
    try:
        url = sess.build_authorize_url(request_token)
        access_token = sess.obtain_access_token(request_token)
        client = client.DropboxClient(sess)
    except rest.ErrorResponse:
        url = sess.build_authorize_url(request_token)
        webbrowser.open(url)
    metadata = client.metadata().get('contents')
    for file_ in metadata:
        if file_.get('mime_type') == 'application/javascript':
            geojson = file_
    return geojson
