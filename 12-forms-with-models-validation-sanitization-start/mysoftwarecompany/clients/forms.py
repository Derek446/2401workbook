from django import forms

from .models import Company

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    # Custom validation for the name field
    # the <fieldname> method is used to add custom validation to a field.
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name) < 2:
            # this will raise an validation error if the name is less than 2 characters long.
            raise forms.ValidationError("Name must be at least 2 characters long.")
        return name

    # Custom validation for the message field
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message and len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message


class CompanyForm(forms.ModelForm):
    # the inner Meta class tells django which model to use and which fields to include in the form
    class Meta:
        model = Company
        fields = ['name', 'email', 'description']
        # note in our model we also have created_at and updated_at fields, but we don't need to include them in the form since they are automatically set by django

    def clean_name(self): # field-level validation
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Company name must be at least 3 characters long.")
        return name

    def clean(self): # cross-field validation
        # note the line below calls the parent class's clean method to get the cleaned data remember this is from inheritence.
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        # we can search our database
        if Company.objects.filter(email=email).exists():
            self.add_error('email', 'A company with this email already exists.') # to add the error to a specific field instead of the whole form.
            # note you can also use
            # raise forms.ValidationError("A company with this email already exists.")

        # check for banned words.
        name = cleaned_data.get('name', '')
        description = cleaned_data.get('description', '')
        forbidden_words = ['spam', 'fake', 'scam']
        for word in forbidden_words:
            if word in description.lower():
                self.add_error('description', f"The company contains a forbidden word: {word}")
                # raise forms.ValidationError(f"The company contains a forbidden word: {word}")
            if word in name.lower():
                self.add_error('name', f"The company contains a forbidden word: {word}")

        return cleaned_data