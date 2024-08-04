

from django.shortcuts import render, redirect


from top.forms import TopForm
from top.models import Top, Type


# Create your views here.


def index(request):
    form = TopForm()
    if not request.user.is_authenticated:
        return redirect('base')
    tops = Top.objects.all()

    if request.method == 'POST':
        form = TopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    ctx = {
        'tops': tops,
        'form': form
    }

    return render(request, 'top/index.html', ctx)


def delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('base')
    top = Top.objects.get(pk=pk)
    top.delete()
    return redirect('index')


def edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('base')
    top = Top.objects.get(pk=pk)
    if request.method == 'POST':
        form = TopForm(request.POST, request.FILES, instance=top)
        if form.is_valid():
            form.save()
            return redirect('index')

    ctx = {
        'form': TopForm(instance=top),
    }

    return render(request, 'top/edit.html', ctx)