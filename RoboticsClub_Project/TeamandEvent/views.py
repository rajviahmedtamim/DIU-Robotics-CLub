from django.shortcuts import render, get_object_or_404
from RoboticsClub_app.models import Setting
from TeamandEvent.models import Event, DURCPanel


def EventView(request):
    event = get_object_or_404(Event, id=1)
    setting = get_object_or_404(Setting, id=1)
    context = {
        'event': event,
        'setting': setting,
    }
    return render(request, 'event.html', context)


def PanelMember(request):
    panel = DURCPanel.objects.all()
    setting = get_object_or_404(Setting, id=1)
    context = {
        'panel': panel,
        'setting': setting,
    }
    return render(request, 'panelMember.html', context)
