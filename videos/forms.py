from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(
        #atributes
        attrs={
            "class": "form-control",
            "placeholder": "Leave a Comment!"
        }))
