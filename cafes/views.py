from django.shortcuts import render, redirect
from .models import Cafe


def home(request):
    query = request.GET.get("q")

    if query:
        cafes = Cafe.objects.filter(city__icontains=query)
    else:
        cafes = Cafe.objects.all()

    return render(
        request,
        "home.html",
        {
            "cafes": cafes,
            "query": query,
        },
    )


def add_cafe(request):

    if request.method == "POST":

        Cafe.objects.create(
            name=request.POST.get("name"),
            city=request.POST.get("city"),
            address=request.POST.get("address"),
            description=request.POST.get("description"),
            image=request.FILES.get("image"),
            wifi="wifi" in request.POST,
            power_socket="power_socket" in request.POST,
            parking="parking" in request.POST,
            coffee_price=request.POST.get("coffee_price"),
            rating=request.POST.get("rating"),
        )

        return redirect("home")

    return render(request, "add_cafe.html")


def cafe_detail(request, id):
    cafe = Cafe.objects.get(id=id)
    return render(request, "cafe_detail.html", {"cafe": cafe})
