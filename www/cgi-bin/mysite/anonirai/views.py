from django.shortcuts import render
from django.http import HttpResponse
from . import forms
import json
from requests_oauthlib import OAuth1Session

CONSUMER_KEY = ""
CONSUMER_SECRET =""

ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

ngwords = []
#NGワードを入れる

CK = CONSUMER_KEY
CS = CONSUMER_SECRET
AT = ACCESS_TOKEN
ATS = ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)
url = "https://api.twitter.com/1.1/statuses/update.json"

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're the arai-san.")

def anonirai(request):
    form = forms.SendTweet()
    d ={
        "form": form,
    }
    return render(request, 'anonirai.html', d)

def result(request):
    result_tweet = request.GET.get('tweet')
    if(result_tweet.find('@')==-1 and result_tweet.find('/')==-1):
        for ng in ngwords:
            if(result_tweet.find(ng)>-1):
                return render(request, 'error.html')
                exit()
        params = {"status" : result_tweet}
        res = twitter.post(url, params = params)
        return render(request, 'result.html', {'tweet': result_tweet})
    else:
        return render(request, 'error.html')
