from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Microcontroller, Manufacturer, Peripheral, Features
from .forms import MicrocontrollerForm, ManufacturerForm, PeripheralForm, FeaturesForm
from django.db.models.functions import Lower

from django.db.models import Q

# Display all microcontrollers


def all_microcontrollers(request):
    """View to display all microcontrollers with optional sorting and search functionality."""
    microcontrollers = Microcontroller.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                microcontrollers = microcontrollers.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            microcontrollers = microcontrollers.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            microcontrollers = microcontrollers.filter(category__name__in=categories)
            categories = Manufacturer.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            microcontrollers = microcontrollers.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'microcontrollers': microcontrollers,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/microcontrollers.html', context)



# Display details of a single microcontroller

def microcontroller_detail(request, microcontroller_id):
    """View to display details of a specific microcontroller."""
    microcontroller = get_object_or_404(Microcontroller, pk=microcontroller_id)
    context = {
        'microcontroller': microcontroller,
    }
    return render(request, 'products/microcontroller_detail.html', context)

# Add a new microcontroller


@login_required
def add_microcontroller(request):
    """View to add a new microcontroller to the system."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        microcontroller_form = MicrocontrollerForm(request.POST)
        manufacturer_form = ManufacturerForm(request.POST)
        peripheral_form = PeripheralForm(request.POST)
        features_form = FeaturesForm(request.POST)

        if microcontroller_form.is_valid() and manufacturer_form.is_valid() and peripheral_form.is_valid() and features_form.is_valid():
            microcontroller = microcontroller_form.save()
            manufacturer_form.save()
            peripheral_form.save()
            features = features_form.save(commit=False)
            features.microcontroller = microcontroller
            features.save()
            messages.success(request, 'Microcontroller successfully added!')
            return redirect(reverse('microcontroller_detail', args=[microcontroller.id]))
        else:
            messages.error(
                request, 'Failed to add the microcontroller. Please ensure the form is valid.')
    else:
        microcontroller_form = MicrocontrollerForm()
        manufacturer_form = ManufacturerForm()
        peripheral_form = PeripheralForm()
        features_form = FeaturesForm()

    context = {
        'form': microcontroller_form,
        'manufacturer_form': manufacturer_form,
        'peripheral_form': peripheral_form,
        'features_form': features_form
    }
    return render(request, 'products/add_product.html', context)

# Edit an existing microcontroller


@login_required
def edit_microcontroller(request, microcontroller_id):
    """View to edit an existing microcontroller."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Get the microcontroller object
    microcontroller = get_object_or_404(Microcontroller, pk=microcontroller_id)

    if request.method == 'POST':
        microcontroller_form = MicrocontrollerForm(
            request.POST, request.FILES, instance=microcontroller)  # Include request.FILES to handle image upload
        if microcontroller_form.is_valid():
            microcontroller_form.save()
            messages.success(request, 'Microcontroller successfully updated!')
            return redirect(reverse('microcontroller_detail', args=[microcontroller.id]))
        else:
            messages.error(
                request, 'Failed to update the microcontroller. Please ensure the form is valid.')
    else:
        microcontroller_form = MicrocontrollerForm(instance=microcontroller)
        messages.info(request, f'You are editing {microcontroller.name}')

    context = {
        'microcontroller_form': microcontroller_form,
        'microcontroller': microcontroller,  # Ensure correct context
    }
    return render(request, 'products/edit_microcontroller.html', context)


# Delete an existing microcontroller


@login_required
def delete_microcontroller(request, microcontroller_id):
    """View to delete a microcontroller from the system."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    microcontroller = get_object_or_404(Microcontroller, pk=microcontroller_id)
    microcontroller.delete()
    messages.success(request, 'Microcontroller deleted successfully!')
    return redirect(reverse('all_microcontrollers'))

# View to add a manufacturer


@login_required
def add_manufacturer(request):
    """View to add a new manufacturer."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Manufacturer successfully added!')
            return redirect(reverse('all_microcontrollers'))
        else:
            messages.error(
                request, 'Failed to add manufacturer. Please ensure the form is valid.')
    else:
        form = ManufacturerForm()

    context = {
        'form': form,
    }
    return render(request, 'products/add_manufacturer.html', context)

# View to add a peripheral


@login_required
def add_peripheral(request):
    """View to add a new peripheral."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PeripheralForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Peripheral successfully added!')
            return redirect(reverse('all_microcontrollers'))
        else:
            messages.error(
                request, 'Failed to add peripheral. Please ensure the form is valid.')
    else:
        form = PeripheralForm()

    context = {
        'form': form,
    }
    return render(request, 'products/add_peripheral.html', context)


# View to add features for a microcontroller

@login_required
def add_features(request, microcontroller_id):
    """View to add features to a specific microcontroller."""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    microcontroller = get_object_or_404(Microcontroller, pk=microcontroller_id)
    if request.method == 'POST':
        form = FeaturesForm(request.POST)
        if form.is_valid():
            features = form.save(commit=False)
            features.microcontroller = microcontroller
            features.save()
            messages.success(
                request, 'Features successfully added to microcontroller!')
            return redirect(reverse('microcontroller_detail', args=[microcontroller.id]))
        else:
            messages.error(
                request, 'Failed to add features. Please ensure the form is valid.')
    else:
        form = FeaturesForm()

    context = {
        'form': form,
        'microcontroller': microcontroller,
    }
    return render(request, 'products/add_features.html', context)
