from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.urls import reverse
from .modelservice import TaskService


def index(request):
    match request.method:
        case "GET":
            return get(request)
        case "POST":
            return post(request)
        case _:
            return HttpResponse("invalid method", status=400)


def get(request):
    return render(
        request, "todo/index.html", {"tasks": TaskService().order_by_descending()}
    )


def post(request):
    try:
        [title, text] = [request.POST["title"], request.POST["text"]]
    except KeyError:
        return HttpResponse("invalid post", status=400)
    else:
        request.session["message"] = TaskService().create(title, text)

    return HttpResponseRedirect(reverse("todo:index"))


def delete(request, id):
    request.session["message"] = TaskService().delete(id)["message"]

    return render(request, "todo/index.html")
