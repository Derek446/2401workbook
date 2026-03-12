from django import forms


class BulkAssignmentUploadForm(forms.Form):
    csv_file = forms.FileField(label="Select a CSV file")

    # Let's add some validation to ensure the uploaded file is a CSV
    def clean_csv_file(self):
        file = self.cleaned_data.get('csv_file')
        # Validate file type extension
        if not file.name.endswith('.csv'):
            raise forms.ValidationError("Please upload a valid CSV file.")

        # Check the content type
        allowed_types = [
            'text/csv',
            'application/vnd.ms-excel',      # Windows/Excel commonly sends this
            'application/csv',
            'text/plain',                     # Some systems report CSVs as plain text
            'application/octet-stream',       # Generic binary — less specific but common
        ]
        if file and file.content_type not in allowed_types:
            raise forms.ValidationError("File type is not CSV.")

        return file
