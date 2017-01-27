from urllib2 import Request, urlopen, URLError
import json

def getReposURL(baseURL,org):
        return baseURL+'orgs/'+org+'/repos'

def getResponse(URL):
        try:
                reposList=urlopen(URL)
                return json.loads(reposList.read())
        except URLError, e:
                print 'Error fetching Repos: ',e

def gettopNrepos(baseURL,org,topn):
        topNrepos={}
        topForks=[0,0,0,0,0]
        reposURL=getReposURL(baseURL,org)
        reposList=getResponse(reposURL)
        for repo in reposList:
                repoName=repo['name']
                repoForkCount=repo['forks_count']
                curMinForks=min(topForks)
                curMinForksIndex=topForks.index(curMinForks)
                if curMinForks <= repoForkCount:
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
