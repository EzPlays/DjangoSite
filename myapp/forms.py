from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Titulo de la tarea', max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    descripcion = forms.CharField(label='Descripcion de la tarea' , widget=forms.Textarea(attrs={'class': 'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label='nombre del proyecto', max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))