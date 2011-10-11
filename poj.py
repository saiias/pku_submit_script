#!/usr/bin/python
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
from optparse import OptionParser

usr="saiias"

class POJ:
    def __init__(self,options,problem_id):
        self.option=options
        self.problem_id = problem_id
        if options.show_status:
            return
        
        if options.titech:
            print "using Titech Procy"
            self.proxies={'http':'http://proxy.noc.titech.ac.jp:3128'}
        else:
            self.proxies=None

    def check(self,ans_path,output_path):
        return subprocess.call(['diff',ans_path,output_path,'y','--strip-trailing-cr','-W','79','-a','-d']) == 0

    def get_open(self):
        ck = cookielib.CookieJar()
        ckhdr = urllib2.HTTPCookieProcessor(ck)
        if self.proxies == None:
            return urllib2.build_opener(ckhdr)
        else:
            return  urllib2.build_opener(ckhdr, urllib2.ProxyHandler(self.proxies))
            
    def get_url(self):
        return 'http://acm.pku.edu.cn/JudgeOnline/problem?id='+self.problem_id


    def submit(self):
        opener = self.get_open()
        postdata = dict()
        postdata['user_id1'] = usr
        usrpass=getpass.getpass(prompt="Password:")
        postdata['password1'] =usrpass
        params = urllib.urlencode(postdata)
        p = opener.open('http://poj.org/login', params)

        print 'Lognin ...' + str(p.getcode())
        postdata = dict()
        postdata['language'] = '0'
        postdata['problem_id'] = self.problem_id
        postdata['source'] =open(self.get_file_name()).read()
        postdata['submit'] ='Submit'
        parameter= urllib.urlencode(postdata)
        proc = opener.open('http://poj.org/submit', parameter)
        print 'Submit ... ' + str(proc.geturl())
        
        time.sleep(2.0)
        self.show_status()
        
    def show_status(self):
        webbrowser.open("http://poj.org/status?problem_id=&user_id="+usr+"&result=&language=")

    def get_file_name(self):
        return self.problem_id+'.cpp'
        
    def compile(self):
        return subprocess.call(['g++','-O2','-o','a.out','-Wno-deprecated','-Wall',self.get_file_name]) == 0

    def execute(self,input_file,output_file):
        start_time = time.time();
        p = subprocess.Popen(['./a.out'], stdin=open(input_file_path, 'r'), stdout=open(output_file_path, 'w'))
        if p.wait() != 0:
            print 'RuntimeError?'
            exit(-1)
        end_time = time.time()
        return end_time - start_time

    def download(self):
        html=urllib.urlopne('http://acm.pku.cn/JudgeOnline/problem?id='+self.problem_id,proxies=self.proxies).read()

        
        

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


    
if __name__ == '__main__':
    main()
