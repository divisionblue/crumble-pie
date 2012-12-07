#!/usr/bin/env python
from lemonpie import lemonpie
from flask_debugtoolbar import DebugToolbarExtension

lemonpie.debug = True
lemonpie.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(lemonpie)
lemonpie.run('0.0.0.0')
