from django.shortcuts import render,redirect, get_object_or_404
from RoboticsClub_app.models import Setting, ContactMessage, ContactForm,AboutCateory,DURCGallery
from Club_Project_App.models import ProjectCategory, ClubProjects
from TeamandEvent.models import DURCPanel


def Home(request):
    panel = DURCPanel.objects.all().order_by('-id')[:4]
    setting = get_object_or_404(Setting, id=1)
    sliding_image = ClubProjects.objects.all().order_by('-id')[:4]
    joinClub = get_object_or_404(AboutCateory, id=2)
    context = {'setting':setting, 'sliding_image':sliding_image, 'panel':panel, 'joinClub':joinClub}
    return render(request, 'homebase.html',context)


def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            return redirect('Contact')

    form = ContactForm
    setting = Setting.objects.get(id=1)
    context = {
        'form': form,
        'setting': setting,
    }
    return render(request, 'contactMessage.html', context)


def Singleproject(request, id):
    setting = get_object_or_404(Setting, id=1)
    singlepro = get_object_or_404(ClubProjects, id=id)
    context={'setting':setting,'singleproject':singlepro}
    return  render(request, 'singleproject.html', context)


def Multipleproject(request):
    setting = get_object_or_404(Setting)
    multipleproject = ClubProjects.objects.all()
    context={'setting':setting,'multipleproject':multipleproject}
    return  render(request, 'multipleprojects.html', context)


def Aboutus(request):

    aboutCategory = get_object_or_404(AboutCateory)
    setting = get_object_or_404(Setting, id=1)
    gallery = DURCGallery.objects.all()
    context = {
               'aboutCategory': aboutCategory,
               'setting': setting,
               'gallery': gallery
            }
    return render(request, 'aboutus.html', context)
