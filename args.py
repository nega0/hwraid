#!/usr/bin/env python2.7

import argparse

nagiosmode = False
debugmode = False
notempmode = False

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

group.add_argument('--nagios',  help='enable nagios support',               action='store_true')
group.add_argument('--debug',   help='enable debugging output',             action='store_true')
group.add_argument('--notemp',  help='disable temperature reporting',       action='store_true')
group.add_argument('--testbin', help='path to fake "megacli" test program', action='store')

args = parser.parse_args()
nagisomode = args.nagios
debugmode  = args.debug
notempmode = args.notemp

print(nagiosmode)
print(debugmode)
print(notempmode)
print(args.testbin)
