from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    # ✅ Basic sanitization example
    def clean_name(self):
        name = self.cleaned_data["name"]
        if "<" in name or ">" in name:  # Prevent XSS injection attempts
            raise forms.ValidationError("Invalid characters in name")
        return name
