from django.shortcuts import render, redirect
from .models import Show


def index(request):
    context = {
        'shows': Show.objects.all()
    }
    # line below passes stuff on to template shows.html
    return render(request, 'shows.html', context)

# displays the form for the new show page


def new(request):
    return render(request, 'new.html')
# displays shows/create


def create(request):
    Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description'],
    )
    return redirect('/shows')

# displays edit html
def edit(request, show_id):
    tv_show = Show.objects.get(id=show_id)
    context = {
        # 'show' gets used at from end and contains id from Show class
        'show': tv_show
    }
    return render(request, 'edit.html', context)

def update(request, show_id):
    update_show = Show.objects.get(id = show_id)

    update_show.title = request.POST['title']
    update_show.network = request.POST['network']
    update_show.release_date = request.POST['release_date']
    update_show.description = request.POST['description']
    update_show.save()

    return redirect('/shows/')

# displays show html
def show(request, show_id):
    # id = show_id (show_id is coming in as function parameter)
    tv_show = Show.objects.get(id=show_id)
    context = {
        # 'show' gets used at from end and contains id from Show class
        'show': tv_show
    }
    # stuff below gets passed onto template
    return render(request, 'show.html', context)


def delete(request, show_id):
    delete_show = Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect('/shows')
