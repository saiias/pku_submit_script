#! usr/bin/env python
# -*- coding: utf-8 -*-

import os
import getpass
import webbrowser
import subprocess
import re
import cookielib
import urllib
import urllib2
import getpass
import time
import cookielib
import shutil
import popen2
import os.path
from optparse import OptionParser

usr=""
dir=""+'/'

class AOJ:

def main():
def main():
    parser = OptionParser();
    parser.add_option("-s","--submit",action="store_true",dest="submit",default=False,help="Submit program");
    parser.add_option("-t","--titech",action="store_true",dest="titech",default=False,help="Use titech proxy");
    parser.add_option("-o","--show_status",action="store_true",dest="show_status",default=False,help="Show_your_status");

    (options, args) = parser.parse_args()

    if options.show_status:
        webbrowser.open("http://poj.org/status?problem_id=&user_id="+usr+"&result=&language=")
        return

    if len(args) == 0:
        print "Input ProblemID"
        parser.print_help()
        return

    status = POJ(options,args[0])
#    status.show_status();

    if options.submit:
        status.submit()
        return

    status.check()


if __name__ == "__main__":
    main()
    
