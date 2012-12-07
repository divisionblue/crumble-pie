from flask import render_template, request, redirect, url_for, flash, json, g
from flask.ext.uploads import UploadSet, configure_uploads, UploadNotAllowed, ARCHIVES

from pprint import pprint

from lemonpie import lemonpie
#from lib import dropbox
#from forms import

# file upload settings
uploaded_files = UploadSet('files', ARCHIVES)
configure_uploads(lemonpie, uploaded_files)

def to_index():
    return redirect(url_for('index'))

@lemonpie.route('/')
def index():
    """index page"""
    json_data=open('lemonpie/static/js/data/stations.js','r')
    data = json.load(json_data)
    #pprint(data)
    json_data.close()
    layers = {'stations': data}
    return render_template('index.html', layers=layers)
