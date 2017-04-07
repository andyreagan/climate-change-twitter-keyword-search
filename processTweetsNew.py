# processTweetsNew.py
# crawl the tweets, and compute the labMT vectors around keywords
# output with daily resolution
#
# NOTES
# uses the new 15-minute compressed format
# 
# USAGE 
# gzip -cd tweets.gz | python processTweetsNew.py 2014-01-01 keywords
#  
# this will read keywords.txt and the tweets from stdin
# and save a frequency file, labMT vector in keywords/[keyword]
# for each keyword

# we'll use most of these
from json import loads
import codecs
import datetime
import re
import numpy
from labMTsimple.storyLab import *
import sys

def tweetreader(tweettext,keyWords,outfile):
    # takes in the hashtag-stripped text
    # the keyword list
    # and the title of the file to append to
    for i in xrange(len(keyWords)):
        if re.search(r"\b%s\b" % keyWords[i],tweettext,flags=re.IGNORECASE) is not None:
            g = codecs.open('rawtweets/{0}/{1}.txt'.format(keyWords[i].replace(' ','-'),outfile),'a','utf8')
            g.write(tweettext.replace('\n',' '))
            g.write('\n')
            g.close()

def gzipper(keyWords,outfile):
    f = sys.stdin
    for line in f:
        try:
            tweet = loads(line)
        except:
            print "failed to load a tweet"
        if 'text' in tweet:
            tweetreader(tweet['text'].replace('#',' '),keyWords,outfile)

if __name__ == '__main__':
    # load the things
    outfile = sys.argv[1]
    
    keyWords = ['climate','global warming','climaterealists','climatechange','globalwarming','agw']
    
    gzipper(keyWords,outfile)
    print "complete"
  







