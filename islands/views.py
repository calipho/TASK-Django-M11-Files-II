from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from islands import models


def get_islands(request: HttpRequest) -> HttpResponse:
    islands: list[models.Island] = list(models.Island.objects.all())

    context = {
        "islands": islands,

    }

    return render(request, "island_list.html", context)


def upload_island_image(request: HttpRequest) -> HttpResponse:
    models.IslandPhoto.objects.create(image=request.FILES["image"])
    return render(request, "upload_island_image.html")
