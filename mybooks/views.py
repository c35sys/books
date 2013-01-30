# Create your views here.
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from forms import BookForm
from models import Book, Author


class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'
    success_url = reverse_lazy('author_list')


class AuthorDetails(DetailView):
    model = Author
    template_name = 'author_details.html'
    success_url = reverse_lazy('author_details')


class AuthorAdd(CreateView):
    model = Author
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')


class AuthorEdit(UpdateView):
    model = Author
    template_name = 'author_form.html'
    success_url = reverse_lazy('author_list')


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')


class BookView(object):
    model = Book
    queryset = Book.objects.all()


class BookAdd(CreateView):
    # use Book model
    model = Book
    # use BookForm form
    form_class = BookForm
    # declare the template
    template_name = 'book_form.html'
    # declare success_url
    success_url = reverse_lazy('author_list')

    # get author id from URL
    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context['author'] = self.kwargs['pk']
        return context

    # override author_id book form
    def form_valid(self, form):
        new_book = form.save(commit=False)
        # get author id from context then pass it to form
        new_book.author_id = self.get_context_data()['author']
        new_book.save()
        return super(BookAdd, self).form_valid(form)

    # define success_url based on author_id
    def get_success_url(self):
        return reverse('book_list', args=[self.get_context_data()['author'], ])


class BookList(ListView):
    model = Book
    template_name = 'book_list.html'
    success_url = reverse_lazy('book_list')

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        # get author id from URL the get all books by this author
        context['book_list'] = Book.objects.filter(author_id=self.kwargs['pk'])
        # get author object
        context['author'] = Author.objects.get(id=self.kwargs['pk'])
        return context
