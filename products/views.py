from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Microcontroller
from .forms import MicrocontrollerForm
from django.db.models.functions import Lower

from django.db.models import Q


def all_microcontrollers(request):
    """View to display all microcontrollers with optional sorting and search
    functionality."""
    microcontrollers = Microcontroller.objects.all()

    query = None
    selected_categories = None
    sort = None
    direction = None

    if request.GET:
        # Handle sorting
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                microcontrollers = microcontrollers.annotate(
                    lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            microcontrollers = microcontrollers.order_by(sortkey)

        # Handle category filtering
        if "category" in request.GET:
            selected_categories = request.GET["category"].split(",")
            print(selected_categories)
            microcontrollers = microcontrollers.filter(
                name__icontains=selected_categories[0]
            )

        # Handle search functionality
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            microcontrollers = microcontrollers.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "microcontrollers": microcontrollers,
        "search_term": query,
        "current_categories": selected_categories,  
        "current_sorting": current_sorting,
    }
    return render(request, "products/microcontrollers.html", context)


# Display details of a single microcontroller


def microcontroller_detail(request, microcontroller_id):
    """View to display details of a specific microcontroller."""
    microcontroller = get_object_or_404(
        Microcontroller, pk=microcontroller_id)
    context = {
        "microcontroller": microcontroller,
    }
    return render(request, "products/microcontroller_detail.html", context)


# Add a new microcontroller


@login_required
def add_microcontroller(request):
    """View to add a new microcontroller to the system."""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        microcontroller_form = MicrocontrollerForm(request.POST)

        if microcontroller_form.is_valid():
            microcontroller = microcontroller_form.save()
            messages.success(request, "Microcontroller successfully added!")
            return redirect(
                reverse("microcontroller_detail", args=[microcontroller.id])
            )
        else:
            messages.error(
                request,
                "Failed to add the microcontroller."
                 " Please ensure the form is valid.",
            )
    else:
        microcontroller_form = MicrocontrollerForm()

    context = {
        "form": microcontroller_form,
    }
    return render(request, "products/add_product.html", context)


# Edit an existing microcontroller


@login_required
def edit_microcontroller(request, microcontroller_id):
    """View to edit an existing microcontroller."""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    # Get the microcontroller object
    microcontroller = get_object_or_404(
        Microcontroller, pk=microcontroller_id)

    if request.method == "POST":
        microcontroller_form = MicrocontrollerForm(
            request.POST, request.FILES, instance=microcontroller
        )  # Include request.FILES to handle image upload
        if microcontroller_form.is_valid():
            microcontroller_form.save()
            messages.success(request,
                              "Microcontroller successfully updated!")
            return redirect(
                reverse("microcontroller_detail", args=[microcontroller.id])
            )
        else:
            messages.error(
                request,
                "Failed to update the microcontroller."
                 " Please ensure the form is valid.",
            )
    else:
        microcontroller_form = MicrocontrollerForm(instance=microcontroller)
        messages.info(request, f"You are editing {microcontroller.name}")

    context = {
        "microcontroller_form": microcontroller_form,
        "microcontroller": microcontroller,  # Ensure correct context
    }
    return render(request, "products/edit_microcontroller.html", context)


# Delete an existing microcontroller


@login_required
def delete_microcontroller(request, microcontroller_id):
    """View to delete a microcontroller from the system."""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    microcontroller = get_object_or_404(
        Microcontroller, pk=microcontroller_id)
    microcontroller.delete()
    messages.success(request, "Microcontroller deleted successfully!")
    return redirect(reverse("all_microcontrollers"))

# View to add features for a microcontroller

