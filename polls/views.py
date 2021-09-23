from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Question,Choice
def home(request):
    return render(request,'home.html')
def index(request):
    question_list=Question.objects.all()
    return render(request,'index.html',{'list':question_list})
def detail(request, question_id):
    question=get_object_or_404(Question,id=question_id)
    b=Choice.objects.filter(question__id=question_id)
    return render(request,'detail.html',{'question':question})

def vote(request, question_id):
    if request.method=='POST':
        question=get_object_or_404(Question,id=question_id)
        a=question.choice_set.get(pk=request.POST['choice'])
        a.votes+=1
        a.save()
    return render(request, 'result.html', {'question': question})    