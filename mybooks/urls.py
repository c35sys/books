from django.conf.urls import patterns, url
from views import AuthorAdd, AuthorList, AuthorEdit, AuthorDelete, \
    AuthorDetails, BookAdd, BookList

urlpatterns = patterns('',
    # List Authors
    url(r'^$', AuthorList.as_view(), name='author-list'),
    url(r'^author/list/$', AuthorList.as_view(), name='author_list'),
    # Author Details
    url(r'^author/(?P<pk>\d+)/$', AuthorDetails.as_view(),
            name='author_details'),
    # Add Author
    url(r'^author/add/$', AuthorAdd.as_view(), name='author_add'),
    # Modify Author
    url(r'^author/(?P<pk>\d+)/edit/$', AuthorEdit.as_view(),
            name='author_modify'),
    # Delete Author
    url(r'^author/(?P<pk>\d+)/delete/$', AuthorDelete.as_view(),
            name='author_delete'),
    # Add Book
    url(r'^author/(?P<pk>\d+)/book/add/$', BookAdd.as_view(),
            name='book_add'),
    # Book list per author
    url(r'^author/(?P<pk>\d+)/book/list/$', BookList.as_view(),
    name='book_list'),
)
