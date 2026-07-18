from django.shortcuts import render

def home(request):
    context = {
        "name": "Ulugbek",
        "age": 20,
        "students": ["Ali", "Vali", "Hasan"],
    }

    return render(request, "home.html", context)
