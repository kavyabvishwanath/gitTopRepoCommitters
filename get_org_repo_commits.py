from gitrepos import gettopNrepos
from gitcommits import getTopCommitters
import sys,getopt

baseURL='https://api.github.com/'
#request = Request('https://api.github.com/orgs/google/repos')

if __name__ == "__main__":
        argv=sys.argv[1:]
        opts, args = getopt.getopt(argv,"o:r:c:",["or=","re=","commis="])
        org=''
        repo=''
        committers=''
        for opt,b in opts:
                if opt=='-o':
                        org=b
                if opt=='-r':
                        repo=b
                if opt=='-c':
                        committers=b
        print org,repo,committers
        #get organisation name from command line
 #       org='google'
        #get repos for the organisation
        topNrepos=gettopNrepos(baseURL,org,repo)
        topCommitters=getTopCommitters(baseURL,org,topNrepos.keys(),committers)
        for topCommiter in topCommitters:
                print topCommiter.repo,topCommiter.committer,topCommiter.commits 

