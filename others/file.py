#!/usr/bin/env python
# coding=utf-8
import os

# get file name
ls = os.linesep

def make():
    'makeTextFile.py  --  create text file.'
    while True:
        fname = raw_input('Input file name:')
        if os.path.exists(fname):
            print "Error : '%s' already exists." % fname
        else:
            break

    # get file content(text) lines
    all = []
    print "\nEnter lins ('.' by itself to quit).\n"

    # loop until user terminates input
    while True:
        entry = raw_input('==>')
        if entry == '.':
            break
        else:
            all.append(entry)

    # write linse to file with proper line-ending
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
    print "-----File-----Done!-----"

def read():
    'readTextFile.py  --  read and display text file.'
    # get filename
    fname = raw_input('Enter file name:')
    print 
    # attempt to open file for reading
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "*** file open error:", e
    else:
        # display contnets to the screen
        for eachLine in fobj:
            print eachLine,
        fobj.close()

print '''
<------------------|------------------->
<--------1---------|---------2--------->
<-----new file-----|-----read file----->
<------------------|------------------->
'''
user = input("Choose num:")
if user == 1:
    make()
elif user == 2:
    read()
else:
    print "Error"
