#!/usr/bin/python

import sys
import os
import ConfigParser
import config
import go

if __name__ == '__main__':
    result = {}
    for t in [ "update", "go" ]:
        m = getattr( config, t )
        cf = ConfigParser.RawConfigParser( m['conf'] )
        cf.read( m['path'] )
        result[ t ] = ' '.join( cf.sections() )

    target = ( len( sys.argv ) > 1 and sys.argv[1] in [ "update", "go" ] ) and sys.argv[1] or "update"
    print result[ target ]


