from urllib2 import Request, urlopen, URLError
import json
import operator
import collections

def getRepoCommitsURL(baseURL,org,repo):
        return  baseURL+'repos/'+org+'/' +repo+'/commits'

def getResponse(URL):
        try:
                reposList=urlopen(URL)
                return json.loads(reposList.read())
        except URLError, e:
                print 'Error fetching Repos: ',e

def getTopCommits(commitersCommit):
        sortByCommits=sorted(commitersCommit.items(),key=operator.itemgetter(1),reverse=True)
        return sortByCommits

def getTopCommitters(baseURL,org,topNrepos,n):
        topRepoCommittersList=[]
        topRepoCommitters=collections.namedtuple('RepoCommitters',['repo','committer','commits'])
        committerProfileList={}
        committerProfile=collections.namedtuple('CommitterProfile',['name','email'])
        for repo in topNrepos:
                commitersCommit={}
                repoCommitsURL=getRepoCommitsURL(baseURL,org,repo)
                committers=getResponse(repoCommitsURL)
                for committer in committers:
                        committerEmail=committer['commit']['committer']['email']
                        if committerEmail in commitersCommit:
                                commitersCommit[committerEmail]=commitersCommit[committerEmail]+1
                        else:
                                commitersCommit[committerEmail]=1
                                committerProfileList[committerEmail]=(committerProfile(committer['commit']['committer']['name'],
                                                                             committer['commit']['committer']['email']
                                                                        ))
                topCommitters=getTopCommits(commitersCommit)
                if len(topCommitters)<n:
                        lastIndex=len(topCommitters)
                else:
                        lastIndex=n
                count=0
                for c in topCommitters:
                        count=count+1
                        topRepoCommittersList.append(topRepoCommitters(repo,committerProfileList[c[0]].name,c[1]))
                        if(count==lastIndex):
                                break
        return topRepoCommittersList
