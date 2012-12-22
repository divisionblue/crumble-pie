from flask import render_template, request, redirect, url_for, flash, json, jsonify, g
from flask.ext.uploads import UploadSet, configure_uploads, ARCHIVES #, UploadNotAllowed

from lemonpie import lemonpie
from lemonpie.lib import drop_util
#from forms import

# file upload settings
uploaded_files = UploadSet('files', ARCHIVES)
configure_uploads(lemonpie, uploaded_files)

def to_index():
    return redirect(url_for('index'))

@lemonpie.route('/<folder>/dropbox_geojson', methods=['GET'])
def dropbox_get_json(folder, json=True):
    db = drop_util.Dropbox(folder)
    geojsonfiles = db.get_geojson()
    if json:
        return jsonify(geojsonfiles)
    else:
        return geojsonfiles

@lemonpie.route('/')
def index():
    """Landing page"""
    geojsonfiles = {}
    try:
        geojsonfiles = dropbox_get_json('lemonpie', False)
    except:
        flash('Reading dropbox failed')
    return render_template('index.html', layers=geojsonfiles)

@lemonpie.route('/<folder>/map', methods=['GET'])
def map(folder):
    """map geojson from dropbox folder"""
    geojsonfiles = {}
    try:
        geojsonfiles = dropbox_get_json(folder, False)
    except:
        flash('Reading dropbox failed')
    return render_template('map.html', layers=geojsonfiles)
