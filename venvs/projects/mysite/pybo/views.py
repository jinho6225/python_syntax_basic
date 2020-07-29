from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.

# ---------------------------------------- [edit] ---------------------------------------- #
from django.http import HttpResponse
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
# ---------------------------------------------------------------------------------------- #

def index(request):
# ---------------------------------------- [edit] ---------------------------------------- #
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

    return render(request, 'pybo/question_list.html', context)
# ---------------------------------------------------------------------------------------- #

def detail(request, question_id):
# ---------------------------------------- [edit] ---------------------------------------- #
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    
    return render(request, 'pybo/question_detail.html', context)
# ---------------------------------------------------------------------------------------- #

def answer_create(request, question_id):
# ---------------------------------------- [edit] ---------------------------------------- #
    question = get_object_or_404(Question, pk=question_id)
    # ---------------------------------------- [edit] ---------------------------------------- #
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
    # ---------------------------------------------------------------------------------------- #

def question_create(request):
# ---------------------------------------- [edit] ---------------------------------------- #
    if request.method == 'POST':
        form = QuestionForm(request.POST)    
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = { 'form': form }
    
    return render(request, 'pybo/question_form.html', context)
# ---------------------------------------------------------------------------------------- #

