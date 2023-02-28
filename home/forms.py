from django import forms


class PerformanceForm(forms.Form):

    education = (
                ('0', 'None'),
                ('1', 'Primary(4th grade)'),
                ('2', 'Primary(5th - 9th grade)'),
                ('3', 'Secondary'),
                ('4', 'Tertiary'),
    )
    gender = [['0', 'female'], ['1', 'male']]

    first_grade = forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}), max_length=3, label="First Grade")
    second_grade = forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}), max_length=3, label="Second Grade")
    fathers_education = forms.ChoiceField(choices=education, label="Father's Education")
    mothers_education = forms.ChoiceField(choices=education, label="Mother's Education")
    study_time = forms.CharField(widget=forms.TextInput(attrs={'type': 'number'}), label="Study Time")
    sex = forms.ChoiceField(choices=gender, label="Sex")
