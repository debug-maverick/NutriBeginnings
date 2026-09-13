from django import forms
from .models import Progress, Blog


class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ["date", "weight", "calories", "water", "steps", "notes"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 4, "placeholder": "How did you feel today?"}),
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "slug", "excerpt", "content", "author"]
        widgets = {
            "excerpt": forms.Textarea(attrs={"rows": 3}),
            "content": forms.Textarea(attrs={"rows": 12}),
        }
