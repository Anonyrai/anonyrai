from django import forms


class SendTweet(forms.Form):
    tweet = forms.CharField(
        max_length=140,
        required=True,
        widget=forms.Textarea
    )
