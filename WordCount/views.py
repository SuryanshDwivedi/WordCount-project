from django.http import HttpResponse
from django.shortcuts import render
import operator
def hello(request):
    return render(request,'home.html')
worddictionary={}
def count(request):
    text=request.GET['name']
    wordcount=text.split()
    for word in wordcount:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    sortedword=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'text':text,'wordy':len(wordcount),'worddict':sortedword})
def about(request):
    return render(request,'about.html')
