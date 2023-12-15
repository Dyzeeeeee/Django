# bookface/forms.py
from django import forms
from .models import Post, UserProfile, Message

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control-no-border'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
        
        
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']