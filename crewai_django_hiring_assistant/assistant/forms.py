from django import forms
from .models import HiringGeneration

class HiringRequestForm(forms.ModelForm):
    class Meta:
        model = HiringGeneration
        fields = ["job_title", "skills", "experience_level", "additional_details"]
        widgets = {
            "job_title": forms.TextInput(attrs={"placeholder": "e.g. Python Backend Developer"}),
            "skills": forms.Textarea(attrs={"rows": 4, "placeholder": "Python, Django, REST APIs, SQL..."}),
            "experience_level": forms.Select(),
            "additional_details": forms.Textarea(attrs={"rows": 3, "placeholder": "Industry, responsibilities, location, tools..."}),
        }

    def clean_job_title(self):
        value = self.cleaned_data["job_title"].strip()
        if len(value) < 2:
            raise forms.ValidationError("Enter a valid job title.")
        return value

    def clean_skills(self):
        value = self.cleaned_data["skills"].strip()
        if len(value) < 2:
            raise forms.ValidationError("Enter at least one required skill.")
        return value
