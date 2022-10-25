from ast import arg
from django.contrib.auth.forms import UserCreationForm
from .models import NormalUser, NormalUserProfile

class NormalUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = NormalUser
        fields = UserCreationForm.Meta.fields
    
    def __init__(self, *args, **kwargs):
        # print("ARGS*", *args)
        # print("ARGS ", args)
        super().__init__(*args, **kwargs)
        if len(args) > 0:
            self.data = args[0]
        # print("SELF DATA", list(args))
    
    def save(self, commit=True):
        user = super().save(commit)
        NormalUserProfile.objects.create(
            user = user,
            name = self.data.get('name'),
            birth_date = self.data.get('birth_date'),
            job = self.data.get('job'),
            description = self.data.get('description'),
        ).save()
        return user
