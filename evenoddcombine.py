#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#(c) Stefan Murawski 2014 (s.murawski@batronix.com)

from intelhex import IntelHex
import sys
import os

def main():
    if len(sys.argv) > 1:
        currentworkdir = os.path.abspath(os.path.dirname(sys.argv[0]))
        evenfilepath = str(os.path.abspath(sys.argv[1]))
        oddfilepath  = str(os.path.abspath(sys.argv[2]))
        newfilepath = os.path.join(currentworkdir , "output.hex")
        tempfileeven = open(evenfilepath, "r")
        tempfileodd = open(oddfilepath, "r")
        evenfile = IntelHex()
        evenfile.loadfile(tempfileeven,evenfilepath.split(".")[-1])
        #evenfile = IntelHex(evenfilepath)
        oddfile = IntelHex()
        oddfile.loadfile(tempfileodd,oddfilepath.split(".")[-1])
        #oddfile = IntelHex(oddfilepath)
        evendict = evenfile.todict()
        odddict = oddfile.todict()
        newdict = {}
        newindex = 0
        if evenfile.maxaddr() >= oddfile.maxaddr():
            maxaddr = evenfile.maxaddr()
        else:
            maxaddr = oddfile.maxaddr()
        #for i in range(len(evendict)):
        for i in range(0,maxaddr+1): #Evtl immer bei 0 und nicht bei inputfile.minaddr() anfangen
            try:
                newdict[newindex] = evendict[i]
            except KeyError: #Leere Adressen werden manchmal beim Speichern übersprungen
                #newdicteven[newindex] = 0x00
                pass
            newindex+=1
            try:
                newdict[newindex] = odddict[i]
            except KeyError: #Leere Adressen werden manchmal beim Speichern übersprungen
                #newdicteven[newindex] = 0x00
                pass
            newindex+=1
        newhex = IntelHex(newdict)
        output = open(newfilepath, 'w')
        newhex.write_hex_file(output)
        output.close()

if __name__ == "__main__":
    main()
