#! /usr/bin/env python
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

    def check_diff(self,ans_path,output_path):
        return subprocess.call(['diff',ans_path,output_path,'-y','--strip-trailing-cr','-W','79','-a','-d']) == 0

    def format_pre(self, s):
        s = s.replace('<br />', '\n')
        s = s.replace('&lt;', '<')
        s = s.replace('&gt;', '>')
        s = s.replace('&quot;', '"')
        s = s.replace('\r', '')
        if not s.endswith('\n'):
            s += '\n'
        while s.endswith('\n\n'):
            s = s[0:len(s) - 1]
        while s.startswith('\n'):
            s = s[1:]
        return s
    
    def check(self):
        print "Compile ... "
        if not self.compile():
            print 'Compile Error'
            exit(-1)
            
        self.input_file= self.problem_id +'_in.txt'
        self.output_file = self.problem_id +'_out.txt'

        if(not os.path.isfile(dir+self.problem_id+'_in.txt')):
            
            print 'Download ... '

            html = self.download()
            index = html.rfind('>Sample Input</')
            html = html[index:]
            p = re.compile('<pre>(.+?)</pre>', re.M | re.S | re.I)
            result = p.findall(html)
            n = len(result) / 2;
            for index in range(n):
                open(dir+self.input_file, 'w').write(self.format_pre(result[index * 2]))
                open(dir+self.output_file, 'w').write(self.format_pre(result[index * 2 + 1]))
            
        exe_time = 0.0
        temp_time = self.execute(dir+self.input_file,dir+'result.txt')


        if exe_time < temp_time:
            exe_time = temp_time

        if self.check_diff(dir+self.output_file,dir+'result.txt'):
            print''
            print 'OK'
            print 'time: '+str(exe_time) + ' sec'
        else:
            print''
            print 'WrongAnswer'
            print 'time: '+str(exe_time) + ' sec'


    def make_file(self,file):
        file = file.replace('\r','')
        if not file.endswith('\n'):
            file += '\n'

        return file


    def get_open(self):
        ck = cookielib.CookieJar()
        ckhdr = urllib2.HTTPCookieProcessor(ck)
        if self.proxies == None:
            return urllib2.build_opener(ckhdr)
        else:
            return  urllib2.build_opener(ckhdr, urllib2.ProxyHandler(self.proxies))
        
    def get_url(self):
        return 'http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id='+self.problem_id


    def submit(self):
        opener = self.get_open()
        postdata = dict()
        postdata['userID'] = usr
        usrpass=getpass.getpass(prompt="Password:")
        postdata['password'] =usrpass
        postdata['language'] = 'C++'
        postdata['problem_id'] = self.problem_id
        postdata['sourceCode'] =open(self.get_file_name()).read()
        postdata['submit'] ='Send'
        parameter= urllib.urlencode(postdata)
        proc = opener.open('http://judge.u-aizu.ac.jp/onlinejudge/servlet/Submit', parameter)
        print 'Submit ... '
        
    def show_status(self):
        webbrowser.open("http://judge.u-aizu.ac.jp/onlinejudge/user.jsp?id="+usr)

    def get_file_name(self):
        return self.problem_id+'.cpp'
    
    def compile(self):
        return subprocess.call(['g++','-O2','-o','a.out','-Wno-deprecated','-Wall',self.get_file_name()]) == 0

    def execute(self,input_file,output_file):
        start_time = time.time();

        p = subprocess.Popen(['./a.out'], stdin=open(input_file,'r'), stdout=open(output_file,'w'))

        if p.wait() != 0:
            print 'RuntimeError?'
            exit(-1)
        end_time = time.time()
        return end_time - start_time

    def download(self):
        self.html=urllib.urlopen('http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id='+self.problem_id,proxies=self.proxies).read()
        return self.html
    
    def get_result(self):
        self.result=urllib.urlopen('http://poj.org/status?problem_id=&user_id='+usr+'&result=&language=',proxies=self.proxies).read()


    
def main():
    parser = OptionParser();
    parser.add_option("-s","--submit",action="store_true",dest="submit",default=False,help="Submit program");
    parser.add_option("-t","--titech",action="store_true",dest="titech",default=False,help="Use titech proxy");
    parser.add_option("-o","--show_status",action="store_true",dest="show_status",default=False,help="Show_your_status");

    (options, args) = parser.parse_args()

    if options.show_status:
        webbrowser.open("http://judge.u-aizu.ac.jp/onlinejudge/status.jsp")
        return

    if len(args) == 0:
        print "Input ProblemID"
        parser.print_help()
        return

    status = AOJ(options,args[0])
#    status.show_status();

    if options.submit:
        status.submit()
        return

    status.check()


if __name__ == "__main__":
    main()
    
