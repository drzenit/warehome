from django.shortcuts import render, redirect

from . import models
from . import common


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        season = request.POST['season']
        description = request.POST['description']
        if (models.Item.objects.last() == None):
            nextId = 1
        else:
            nextId = models.Item.objects.last().id + 1
        qrCodePath = common.generateQRcode(nextId)
        item = models.Item(name=name, description=description, season=season, qrCodePath=qrCodePath)
        item.save()

        return redirect('index')

    dbData = list(models.Item.objects.all())

    context = {
        'wareData': dbData,
    }

    return render(request, 'warehouse/mainPage.html', context)

def itemView(request, pk):
    itemData = models.Item.objects.get(id = pk)

    context = {
        'itemData': itemData,
    }

    return render(request, 'warehouse/itemPage.html', context)
