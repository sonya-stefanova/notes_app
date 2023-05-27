from django.shortcuts import render, redirect
from notes_app.web.forms import ProfileCreateForm, NoteBaseForm, NoteDeleteForm, NoteCreateForm, NoteEditForm
from notes_app.web.models import Profile, Note


def get_profile():
    profile = Profile.objects.first() or None
    return profile


def show_home(request):
    profile = get_profile()

    if not profile:
        return redirect('add profile')

    notes = Note.objects.all()

    context = {
        'profile': profile,
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)




def add_profile(request):
    profile = get_profile()

    if profile is not None:
        return redirect('home')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)

def profile_details(request):
    profile = get_profile()
    number_current_notes = Note.objects.all().count()

    context = {
        'number_current_notes': number_current_notes,
        'profile':profile,
    }
    return render(request, 'profile.html', context)



def delete_profile(request):
    current_profile = Profile.objects.get()
    Note.objects.all().delete()
    current_profile.delete()
    return redirect('home')



def create_note(request):
    if request.method == 'GET':
        form = NoteCreateForm()

    else:
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = NoteEditForm(instance=note)

    else:
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note details', pk=note.pk)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-edit.html', context)


def note_details(request, pk):
    note = Note.objects.filter(pk=pk).get()

    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)


def note_delete(request, pk):
    note = Note.objects.\
        filter(pk=pk).\
        get()

    if request.method == 'GET':
        form = NoteDeleteForm(instance=note)

    else:
        form = NoteDeleteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-delete.html', context)