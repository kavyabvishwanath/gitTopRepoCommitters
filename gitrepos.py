## this script gets top N repos for given organisation org

from urllib2 import Request, urlopen, URLError
import json
import sys

def getReposURL(baseURL,org):
        return baseURL+'orgs/'+org+'/repos'

def getResponse(URL):
        try:
                reposList=urlopen(URL)
                return json.loads(reposList.read())
        except URLError, e:
                print 'Error fetching Repos: ',e

## main module which returns the top N repos for given organisation
def gettopNrepos(baseURL,org,topn):
        topNrepos={} #holds the top r repos
        topForks=[0 for i in range(0,topn)] #holds the top repo counts at any point we maintain state of only required top number of top repos
        reposURL=getReposURL(baseURL,org)
        reposList=getResponse(reposURL)
        if not reposList:
            print 'No repositories found for ',org
            sys.exit(2)
        for repo in reposList:
                repoName=repo['name']
                repoForkCount=repo['forks_count']
                curMinForks=min(topForks)
                curMinForksIndex=topForks.index(curMinForks)
                if curMinForks <= repoForkCount:
                        #base case
                        if any(topNrepos)==False or len(topNrepos) < topn:
                                topNrepos[repoName]=repoForkCount
                                topForks[curMinForksIndex]=repoForkCount
                        else:
                                for topRepo in topNrepos:
                                        if topNrepos[topRepo]==curMinForks:
                                                del topNrepos[topRepo]
                                                topNrepos[repoName]=repoForkCount
                                                topForks[curMinForksIndex]=repoForkCount
                                                break
        return topNrepos
