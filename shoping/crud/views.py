from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Lecture, Eval

def LectureList(request):
    lectures = Lecture.objects
    return render(request, 'LectureList.html', {'lectures' : lectures})
def EvalList(request, lect_id):
    lect = get_object_or_404(Lecture, pk = lect_id)
    evals = Eval.objects.filter(lect_id = lect_id).order_by('title')
    keys = {
        'lect' : lect,
        'evals' : evals
    }
    return render(request, 'EvalList.html', keys)
def write(request, lect_id):
    lect = get_object_or_404(Lecture, pk = lect_id)
    return render(request, 'write.html', {'lect' : lect})
def create(request):
    if request.method == "POST":
        a_eval = Eval()
        a_eval.lect = Lecture.objects.get(lectureName = request.POST['lect'])
        a_eval.title = request.POST['title']
        a_eval.pub_date = timezone.datetime.now()
        a_eval.body = request.POST['body']
        a_eval.image = request.FILES['image']
        a_eval.save()
        return redirect('detail/' + str(a_eval.id))
    else:
        return render(request, 'write.html')

def detail(request, eval_id):
    eval_ = get_object_or_404(Eval, pk = eval_id)
    return render(request, 'EvalDetail.html', {'eval_' : eval_})