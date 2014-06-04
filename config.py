#!/usr/bin/python

import os
_dir = os.path.dirname( __file__ ) or '.'

update = {
    "path" : "%s/update.conf" % ( _dir ),
    "conf" : {}
}

go = {
    "path" : "%s/svrs.conf" % ( _dir ),
    "conf" : {
        'desc' : 'Welcome to use go',
        'pasw' : 'Hello World',
        'port' : 22,
        'user' : 'root',
        'path' : '.',
        'cmd'  : ''
    }
}
