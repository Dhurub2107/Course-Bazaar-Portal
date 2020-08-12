from django import forms
class CandidateForm(forms.Form):
    CID = forms.CharField(label='CID',max_length=20)
    PINCODE = forms.CharField(label='PINCODE', max_length=50)