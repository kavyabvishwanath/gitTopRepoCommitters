## the script finds committers specific data for the repos

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

#this module sorts the list of commiters by the number of commits
def getTopCommits(commitersCommit):
        #sorts by the number of commits
        sortByCommits=sorted(commitersCommit.items(),key=operator.itemgetter(1),reverse=True)
        return sortByCommits

#This module returns topNCommiters for the passed topNrepos
def getTopCommitters(baseURL,org,topNrepos,n):
        #final output list top c committers
        topRepoCommittersList=[]
        topRepoCommitters=collections.namedtuple('RepoCommitters',['repo','committer','commits'])
        #holds committers profile
        committerProfileList={}
        committerProfile=collections.namedtuple('CommitterProfile',['name','email'])
        #the loop gets commits for the selected top r repos

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

                #if the top repo has less than c committers handle then return all committers else return top c
                if len(topCommitters)<n:
                        lastIndex=len(topCommitters)
                else:
                        lastIndex=n
                count=0

                #find top repo - top committers profile
                for c in topCommitters:
                        count=count+1
                        topRepoCommittersList.append(topRepoCommitters(repo,committerProfileList[c[0]].name,c[1]))
                        if(count==lastIndex):
                                break
        return topRepoCommittersList
