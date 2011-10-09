#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getpass
import webbrowser
from optparse import OptionParser

usr='sa__i'

class POJ:
    def __init__(self,options,problem_id):
        self.option=options
        self.problem_id = problem_id

        if options.show_status:
            return
        
        if options.titech:
            self.proxy={'http':'http://proxy.noc.titech.ac.jp:3128'}
        else:
            self.proxy=None


    def get_url(self):
        return 'http://acm.pku.edu.cn/JudgeOnline/problem?id='+self.problem_id

    def download(self):
        return

    def sunmit(self):
        op = self.get_opener()
        data = dict()
        data['usr_id'] = usr
        password=getpass.getpas(prompt="Password:")
        data['password'] =password
        
        
    def show_status(self):
        webbrowser.open("http://poj.org/status?problem_id=&user_id="+usr+"&result=&language=")


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

    status = POJ(options,args)
    status.show_status();
    print "1"

    
if __name__ == '__main__':
    main()
