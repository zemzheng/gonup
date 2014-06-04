#!/usr/bin/python

import sys
import os
import ConfigParser
import config
import go

_dir = os.path.dirname( __file__ ) or '.'

cf = ConfigParser.RawConfigParser( config.update['conf'] )
cf.read( config.update['path'] )

if __name__ == '__main__':
    if len( sys.argv ) > 1:
      project = sys.argv[1]
    else:
      project = ''

    if cf.has_section( project ):

        server = go.getOptionsByName(
            str( cf.get( project, 'svr') ) 
        )
        if server:
            path = str( cf.get( project, 'path' ) )
            pkg  = str( cf.get( project, 'pkg'  ) )

            os.system( 'rz -bye' )
            os.system( 'expect %s/expect/scpThenUnzip.exp %s@%s %s %s %s' % (
                    config._dir,
                    server['user'], server['host'], server['pasw'], 
                    path, pkg
                ) 
            )
            os.system( 'rm %s -f' % ( pkg ) )
    else:
      print '''List to be udpate:
      =========================================================
      \n\t |''', '\n\t | * '.join( cf.sections() );


