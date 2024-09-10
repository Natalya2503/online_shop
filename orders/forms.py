from django import forms



class CreateOrderForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите вашу фамилию'

            }
        )

    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона (000) 000-0000'
            }
        )
    )
 
    delivery_address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'delivery-address',
                'rows': 2,
                'placeholder':'Введите адрес доставки'
            }
        ),
       
    )

  

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры')
        return data