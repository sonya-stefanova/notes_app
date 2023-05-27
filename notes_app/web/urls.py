from django.urls import path

from notes_app.web.views import profile_details, show_home, create_note, edit_note, note_details, note_delete, \
    delete_profile, add_profile

urlpatterns = (
    path('', show_home, name='home'),

    path('profile/', profile_details, name='profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('profile/add/', add_profile, name ='add profile'),#additional to the provided URLs

    path('add/', create_note, name='create note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('details/<int:pk>/', note_details, name='note details'),
    path('delete/<int:pk>/', note_delete, name='delete note'),)