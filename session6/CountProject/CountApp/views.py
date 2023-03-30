from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request,'count.html')

def result(request):
    text = request.POST['text_']
    total_len=len(text)
    no_blank_len = len(text.replace(' ', ''))
    words = len(text.split())

    return render(request,'result.html',{
        'text':text,
        'total_len':total_len,
        'no_blank_len':no_blank_len,
        'words':words
        })