#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getpass
import webbrowser
import subproccess
import cookielib
import urllib
import urllib2
import getpass
import time

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

    def check(self,ans_path,output_path):
        return subprocess.call(['diff',ans_path,output_path,'y','--strip-trailing-cr','-W','79','-a','-d']) == 0

    def get_open:
        ck = cookielib.CookieJar()
        ckhdr = urllib2.HTTPCookieProcessor(ck)
        if self.proxy == None:
            return urllib2.build_opener(ckhdr)
        else:
            return  urllib2.build_opener(ckhdr, urllib2.ProxyHandler(self.proxy))
            
    def get_url(self):
        return 'http://acm.pku.edu.cn/JudgeOnline/problem?id='+self.problem_id

    def download(self):
        return

    def sunmit(self):
        op = self.get_open()
        data = dict()
        data['usr_id'] = usr
        password=getpass.getpas(prompt="Password:")
        data['password'] =password
        parameter = urllib.urlencode(posrdata)
        proc = op.open('hhtp://poj.org/login',parameter)
        print 'Lognin ...'

        data = dict();
        date['language'] = '0'
        data['problem_id'] = usrpass
        data['source'] = open(self.get_source_file_name()).read()
        data['submit'] = 'Submit'
        parameter= urllib.urlencode(postdata)
        p = opener.open('http://poj.org/submit', params)
        print 'Submit ... '

        time.sleep(1.5)
        self.show_status()
        
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
