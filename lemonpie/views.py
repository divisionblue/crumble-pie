from flask import render_template, request, redirect, url_for, flash, json, g
from flask.ext.uploads import UploadSet, configure_uploads, UploadNotAllowed, ARCHIVES

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
    layers = ['None']
    flash('bon giorno!')
    return render_template('index.html', layers=layers)
