from django import forms
from .models import Leave

class DateInput(forms.DateInput):
    input_type = 'date'

LEAVE_CHOICES = (
    Leave.LEAVE_TYPES
)

class BookLeaveForm(forms.Form):
    # leave_date = forms.DateField(
    #     label="Leave Date",
    #     required=True,
    #     widget=DateInput,
    # )
    leave_start = forms.DateField(
        label="Leave From",
        required=True,
        widget=DateInput(attrs={
            'id': 'leave_start_date_input',
        }),
    )
    leave_until = forms.DateField(
        label="To",
        required=True,
        widget=DateInput(attrs={
            'id': 'leave_until_date_input',
        }),
    )
    leave_type = forms.ChoiceField(choices=LEAVE_CHOICES, required=True)
    leave_reason = forms.CharField(max_length=128, widget=forms.Textarea(), required=True)