from django import forms

class SentenceUploadForm(forms.Form):
    sentence = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))

    def __init__(self, *args, **kwargs):
        super(SentenceUploadForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter your sentence here'