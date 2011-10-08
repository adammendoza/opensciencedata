from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.template import RequestContext
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datasets.models import Dataset
from datasets.forms import DatasetForm

def index(request):
    datasets_all = Dataset.objects.order_by('updated').all()
    paginator = Paginator(datasets_all, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        datasets = paginator.page(page)
    except (EmptyPage, InvalidPage):
        datasets = paginator.page(paginator.num_pages)

    return render_to_response('datasets/index.html',{
        'datasets': datasets,
    }, RequestContext(request))


@login_required
def add_dataset(request):
    if request.method == 'POST':
        form = DatasetForm(request.POST)
        if form.is_valid():
            new_dataset = form.save(commit=False)
            new_dataset.user = request.user
            new_dataset.save()
            return redirect('/datasets/%d' % new_dataset.id)
    else:
        form = DatasetForm()

    return render_to_response('datasets/add.html',{
        'form': form,
    }, RequestContext(request))
    

def view_dataset(request, id):
    dataset = get_object_or_404(Dataset, id=id)
    return render_to_response('datasets/view.html',{
        'dataset': dataset,
    }, RequestContext(request))


@login_required
def edit_dataset(request, id):
    dataset = get_object_or_404(Dataset, id=id)
    if dataset.user is not request.user:
        redirect("/datasets/%d" % id)

    if request.method == 'POST':
        form = DatasetForm(request.POST, instance=dataset)
        if form.is_valid():
            form.save()
    else:
        form = DatasetForm(instance=dataset)

    return render_to_response('datasets/add.html',{
        'form': form,
    }, RequestContext(request))


def download_dataset(request, id):
    dataset = get_object_or_404(Dataset, id=id)
    dataset.downloads += 1
    dataset.save()
    redirect(dataset.data.url)