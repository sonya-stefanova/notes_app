from django import forms

from notes_app.web.models import Profile, Note



class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'image_url',)

class NoteBaseForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

class NoteCreateForm(NoteBaseForm):
    pass


class NoteEditForm(NoteBaseForm):
    pass

class NoteDeleteForm(NoteBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
