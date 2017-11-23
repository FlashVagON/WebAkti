from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.template import loader
from .models import T_NormativAct
from .forms import PostForm
from django.views.generic import ListView, DetailView
import logging
logger = logging.getLogger(__name__)

def index(request):
    list = T_NormativAct.objects.order_by('id')
    template = loader.get_template('Editor/main.html')
    context = {
        'list': list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, id):
    try:
        akt = T_NormativAct.objects.get(pk=id)
    except T_NormativAct.DoesNotExist:
        raise Http404("акт does not exist")
    return render(request, 'Editor/detail.html', {'akt': akt})


class PostsListView(ListView):  # представление в виде списка
    model = T_NormativAct  # модель для представления


class PostDetailView(DetailView):  # детализированное представление модели
    model = T_NormativAct


def addact(request,akt_id=None):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        logger.error('posting ' + str(request.user.is_authenticated))
        if form.is_valid() and request.user.is_authenticated:  # only authenticated users can post
            post = form.save(commit=False)
            if akt_id is not None:
                post.pk = akt_id
                logger.error('изменение удалось')
            post.save()
            return redirect('detail', id=post.id)
        logger.error('Что-то не так с загрузкой')
        return render(request, 'Editor/detail.html')
    if akt_id is None:
        form = PostForm()
    else:
        akt_data=T_NormativAct.objects.get(pk=akt_id)
        form = PostForm(instance=akt_data)
    return render(request, 'Editor/post_edit.html', {'form': form})
