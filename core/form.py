from django import forms

class ContactForm(forms.Form):
    nombre=forms.CharField(max_length=140, label="Nombre")
    email=forms.EmailField(label="Email")
    comentario=forms.CharField(max_length=10000,label="Comentario",widget=forms.Textarea)
    
    def clean_nombre(self):
        nombre=self.cleaned_data.get("nombre")
        if len(nombre) < 5:
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres")
        return nombre
