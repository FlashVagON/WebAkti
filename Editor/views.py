from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.template import loader
from .models import T_NormativAct
from .forms import PostForm
from django.views.generic import ListView, DetailView
import logging

logger = logging.getLogger(__name__)


def index(request):#delete that function
    query=request.GET.get("searchtxt")
    if query:
        list = T_NormativAct.objects.filter(regnum__icontains=query).order_by('id')
    else:
        logger.error('else')
        list = T_NormativAct.objects.order_by('id')
    template = loader.get_template('Editor/main.html')
    context = {
        'list': list,
    }
    return HttpResponse(template.render(context, request))



def detail(request, id):
    try: akt = T_NormativAct.objects.get(pk=id)
    except T_NormativAct.DoesNotExist:
        raise Http404("акт does not    exist") 
    return render(request, 'Editor/detail.html', {'akt': akt})
    
def listing(request):  
    query=request.GET.get("searchtxt")
    if query:
        list = T_NormativAct.objects.filter(regnum__icontains=query).order_by('id')
    else:
        logger.error('else')
        list = T_NormativAct.objects.order_by('id')                          #https://djbook.ru/rel1.9/topics/pagination.html
    akts_count = list#T_NormativAct.objects.all() #общее количество актов
    paginator = Paginator(akts_count, 5)  # Показывать по 5 актов на странице
    page = request.GET.get('page')
    try: all_akts = paginator.page(page)
    except PageNotAnInteger:  # If page is not an integer, deliver first page.
        all_akts = paginator.page(1) 
    except EmptyPage:  # If page is out of range (e.g. 9999), deliver last page of results. 
        all_akts = paginator.page(paginator.num_pages)
    template = loader.get_template('Editor/main.html')
    context = {
        'all_akts':all_akts,
        'list': all_akts,
    }
    return HttpResponse(template.render(context, request))
    #return render_to_response(request, 'Editor/main.html', {'all_akts':all_akts,})

class PostsListView(ListView):  # представление в виде списка
    model = T_NormativAct  # модель для представления


class PostDetailView(DetailView):  # детализированное представление модели
    model = T_NormativAct


def addact(request, akt_id=None):
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
        akt_data = T_NormativAct.objects.get(pk=akt_id)
        form = PostForm(instance=akt_data)
    return render(request, 'Editor/post_edit.html', {'form': form})
