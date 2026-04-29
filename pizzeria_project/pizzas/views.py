from django.shortcuts import render

def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzas/index.html')
from .models import Pizza

def pizzas(request):
    """Show all pizzas."""
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)
from .models import Pizza

def pizza(request, pizza_id):
    """Show a single pizza and its toppings."""

    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()

    context = {
        'pizza': pizza,
        'toppings': toppings
    }

    return render(request, 'pizzas/pizza.html', context)
