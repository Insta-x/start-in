from dataclasses import field
from django.forms import ModelForm
from .models import Project, Donation

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'donation_target']

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = ['project', 'amount']