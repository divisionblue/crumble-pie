from flask import render_template, request, redirect, url_for, flash, json, g
from flask.ext.uploads import UploadSet, configure_uploads, ARCHIVES #, UploadNotAllowed

from lemonpie import lemonpie
from lemonpie.lib import drop_util
#from forms import

# file upload settings
uploaded_files = UploadSet('files', ARCHIVES)
configure_uploads(lemonpie, uploaded_files)

def to_index():
    return redirect(url_for('index'))

def read_dropbox_json():
    #json_data = open('lemonpie/static/js/data/stations.js','r')
    #data = json.load(json_data)
    #pprint(data)
    #json_data.close()
    #import ipdb; ipdb.set_trace()
    db = drop_util.Dropbox()
    geojson = db.get_geojson()
    return geojson

@lemonpie.route('/')
def index():
    """index page"""
    data = ''
    try:
        data = read_dropbox_json()
    except:
        flash('Reading dropbox failed')
    layers = {'stations': data}
    return render_template('index.html', layers=layers)
