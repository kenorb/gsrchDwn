#!/usr/bin/python
#
# neo1981 (neo1981@gmail.com)
# http://www.infosec-neo.blogspot.com  -- 
#
# Program to download the pdf files for given search
# This program will automatically add "filetype:pdf" to the searched query
# Continue function "-c ResultNo" would continue from c number upwards downloading of files
# 
import os.path, sys
sys.path.insert(0, "xgoogle") # Add current xgoogle dir to search path
from xgoogle.search import GoogleSearch, SearchError
import getopt
import urllib2
import urllib
import os.path as ospath

global rem_file # global variable to be used in dlProgress

def dlProgress(count, blockSize, totalSize):
  percent = int(count*blockSize*100/totalSize)
  sys.stdout.write("\r" + rem_file + "...%d%%" % percent)
  sys.stdout.flush()

# parse command line options
try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["query=","ftype=","cnt=","dir=","--help"])
except getopt.error, msg:
    print 'python gsrchDwn.py --query [\"query_text\"] [--ftype file_extension] [--cnt contine_result_number] [--dir download_dir]',msg
    sys.exit(2)

query = ''
mfiletype = 'pdf'
n_cnt = 0
dwn_dir = "."



# Process options
for o, a in opts:
    if o == "--query":
        query = a
    if o == "--ftype":
        mfiletype = a
    if o == "--cnt":
        n_cnt = int(a)
    if o == "--dir":
        dwn_dir = a.replace('\\',"\\\\")
        
  
    
if query == '':
    print ('python gsrchDwn.py --query [query_text] [--ftype file_extension] [--cnt contine_result_number] [--dir download_dir]')
    sys.exit(2)


try:

    cnt = 0
    
    gs = GoogleSearch(query)
    gs.filetype = mfiletype    
    gs.results_per_page = 50
    pgCnt = 1

    if n_cnt <> 0:
        print "Download Continuing from result number: ",str(n_cnt)

    #import pdb

    while True:
        gs.page = pgCnt
        results = gs.get_results()
        pgCnt = pgCnt +1  #Increase page count to next page
        
        if not results: # no more results were found
            break

        for res in results:
            cnt = cnt +1
            print "Serach No. : ",str(cnt)      
            print res.title.encode("utf8")
            print res.desc.encode("utf8")
            temp_url = res.url.encode("utf8")
            if n_cnt <> 0:
                 if cnt < n_cnt:
                    continue

            #Temp trace
            #pdb.set_trace()  

            rem_file = res.title.encode("utf8") #rem_file used in download progress 
            loc_file =  dwn_dir + "\\" + temp_url.split("/")[-1]

            if ospath.isfile(loc_file):
                print "File already exist: ",loc_file
                print "Not downloading file"
                continue
            
            print "Now downloading... ", temp_url
            print
            
            try:
                urllib.urlretrieve(temp_url, loc_file, reporthook=dlProgress)    
                print "Download Complete: ", loc_file
            except IOError:
                print "***Unable to Download file:IOError ",rem_file
                print "Continuing with Next result."
            except:
                print "***Unable to Download file:Unknown Error ",rem_file
                print "Continuing with Next result."


except SearchError, e:
  print "Search failed: %s" % e
