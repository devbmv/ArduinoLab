from django.shortcuts import render, redirect
from .models import Author, Book, Publisher, Series
from .forms import AuthorForm, BookForm, PublisherForm, SeriesForm

# View pentru pagina principală
def main_page(request):
    return render(request, 'test_app/main_page.html')

def add_all_on_one_page(request):
    if request.method == 'POST':
        # Form handling for each model
        author_form = AuthorForm(request.POST, prefix='author')
        book_form = BookForm(request.POST, prefix='book')
        publisher_form = PublisherForm(request.POST, prefix='publisher')
        series_form = SeriesForm(request.POST, prefix='series')

        # Check each form if valid, then save the data
        if author_form.is_valid():
            author_form.save()
        if book_form.is_valid():
            book_form.save()
        if publisher_form.is_valid():
            publisher_form.save()
        if series_form.is_valid():
            series_form.save()

        return redirect('main_page')  # Redirect to the main page or wherever you'd like

    else:
        # Initialize empty forms when GET request
        author_form = AuthorForm(prefix='author')
        book_form = BookForm(prefix='book')
        publisher_form = PublisherForm(prefix='publisher')
        series_form = SeriesForm(prefix='series')

    context = {
        'author_form': author_form,
        'book_form': book_form,
        'publisher_form': publisher_form,
        'series_form': series_form
    }
    return render(request, 'test_app/add_all.html', context)
# View funcțional pentru adăugarea unui nou autor
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors_list')  # Redirecționează după salvare
    else:
        form = AuthorForm()
    return render(request, 'test_app/add_author.html', {'form': form})

# View funcțional pentru adăugarea unei noi cărți
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')  # Redirecționează după salvare
    else:
        form = BookForm()
    return render(request, 'test_app/add_book.html', {'form': form})

# View funcțional pentru adăugarea unui nou publisher
def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publishers_list')  # Redirecționează după salvare
    else:
        form = PublisherForm()
    return render(request, 'test_app/add_publisher.html', {'form': form})

# View funcțional pentru adăugarea unei noi serii
def add_series(request):
    if request.method == 'POST':
        form = SeriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('series_list')  # Redirecționează după salvare
    else:
        form = SeriesForm()
    return render(request, 'test_app/add_series.html', {'form': form})

# View funcțional pentru listarea autorilor
def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'test_app/author_list.html', {'authors': authors})

# View funcțional pentru listarea cărților
def books_list(request):
    books = Book.objects.all()
    return render(request, 'test_app/book_list.html', {'books': books})

# View funcțional pentru listarea publisher-ilor
def publishers_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'test_app/publisher_list.html', {'publishers': publishers})

# View funcțional pentru listarea seriilor
def series_list(request):
    series = Series.objects.all()
    return render(request, 'test_app/series_list.html', {'series': series})
