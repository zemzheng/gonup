#!/usr/bin/python

import os
import sys
import ConfigParser
import config

cf = ConfigParser.RawConfigParser( config.go['conf'] )
cf.read( config.go['path'] )

def getOptionsByName( name ):

    if cf.has_section( name ):
        return {
            'host' : str( cf.get( name, 'host' ) ),
            'desc' : str( cf.get( name, 'desc' ) ),
            'pasw' : str( cf.get( name, 'pasw' ) ),
            'port' : str( cf.get( name, 'port' ) ),
            'user' : str( cf.get( name, 'user' ) ),
            'path' : str( cf.get( name, 'path' ) ),
            'cmd'  : str( cf.get( name, 'cmd'  ) )
        }

    return None

def showAllSvrs():
    return cf.sections()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        svr = sys.argv[1]
    else:
        svr = ''

    options = getOptionsByName( svr )
    if options:

        print 'Try to connect to %s@ %s closed. ' % ( options['user'],  options['host'] )
        print '------- Start ------\n'
        print options['desc'], '\n'

        os.system( 
            'expect ' + config._dir + '/expect/go.exp %s %s %s %s %s %s' % ( 
                options['host'], options['user'], options['pasw'], options['port'], options['path'], options['cmd']
            ) 
        )

        print 'Connect to %s@ %s closed. ' % ( options['user'],  options['host'] )
        print '------- END -------\n'

    else:
        print '''Servers you can go to:
        ===========================================
        \n\t |''', '\n\t | * '.join( showAllSvrs() );

