activate_this = '/root/.virtualenvs/lemonpie/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys, os
sys.path.insert(0, '/var/www/lemonpie')
from lemonpie import lemonpie as application
