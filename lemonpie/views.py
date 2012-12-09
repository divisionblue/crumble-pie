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

@lemonpie.route('/dropbox_geojson', methods=['GET'])
def dropbox_get_json():
    db = drop_util.Dropbox()
    geojsonfiles = db.get_geojson()
    print geojsonfiles
    return geojsonfiles

@lemonpie.route('/')
def index():
    """index page"""
    layers = {}
    try:
        geojsonfiles = dropbox_get_json()
        print geojsonfiles
        for name, geojson in geojsonfiles.iteritems():
            layers = {name: geojson['data']}
    except:
        flash('Reading dropbox failed')
    return render_template('index.html', layers=geojsonfiles)
