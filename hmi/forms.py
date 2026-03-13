from django import forms

class ControlForm(forms.Form):
    # Requirement 4: Define min/max values for error checking
    threshold = forms.FloatField(
        label='Alert Threshold (cm)',
        min_value=0.0,
        max_value=500.0,
        help_text="Enter a value between 0 and 500"
    )