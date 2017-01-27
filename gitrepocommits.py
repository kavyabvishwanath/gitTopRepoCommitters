from gitrepos import gettopNrepos
from gitcommits import getTopCommitters
import sys,getopt

baseURL='https://api.github.com/'
#request = Request('https://api.github.com/orgs/google/repos')

if __name__ == "__main__":
        #get organisation,repocount,committerscount from command line
        argv=sys.argv[1:]
        try:
                opts, args = getopt.getopt(argv,"o:r:c:",["org=","repos=","commits="])
        except getopt.GetoptError:
                print "usage python gitrepocommits.py -o <orgname> -r <r top repos> -c <c top commits>"
                sys.exit(2)
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
        if org=='':
                org="google"
        if repo=='':
                repo=5
        if committers=='':
                committers=3
        #get r top repos for the organisation
        topNrepos=gettopNrepos(baseURL,org,int(repo))
        #get c top committers
        topCommitters=getTopCommitters(baseURL,org,topNrepos.keys(),int(committers))
        #print top committers
        for topCommiter in topCommitters:
                print topCommiter.repo,'|',topCommiter.committer,'|',topCommiter.commits 

