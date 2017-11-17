from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import T_NormativAct
from .forms import PostForm
from django.views.generic import ListView, DetailView
def index(request):
    list = T_NormativAct.objects.order_by('id')
    template = loader.get_template('Editor/main.html')
    context = {
    'list': list,
    }
    return HttpResponse(template.render(context, request))
	
def detail(request,id):
    try:
        akt = T_NormativAct.objects.get(pk=id)
    except T_NormativAct.DoesNotExist:
        raise Http404("акт does not exist")
    return render(request, 'Editor/detail.html', {'akt': akt})
	
class PostsListView(ListView): # представление в виде списка
    model = T_NormativAct                   # модель для представления 

class PostDetailView(DetailView): # детализированное представление модели
    model = T_NormativAct

def addact(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            return redirect('detail', pk=post.pk)
    return render(request, 'Editor/post_edit.html', {'form': form})