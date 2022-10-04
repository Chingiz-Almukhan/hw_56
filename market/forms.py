from django import forms

CATEGORIES = (
    ('other', 'Разное'), ('products', 'Продукты'), ('technique', 'Техника'), ('sport', 'Спорт'), ('clothes', 'Одежда'))


class AddEditForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Название',
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Введите название',
                                      'type': 'text', 'class': 'form-control mb-2'}))
    description = forms.CharField(max_length=254, required=False, label='Описание',
                                  widget=forms.Textarea(
                                      attrs={'placeholder': 'Введите описание',
                                             'type': 'text', 'class': 'form-control mb-2'}))
    image = forms.CharField(max_length=100, required=True, label='Название',
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Введите ссылку на фотографию',
                                       'type': 'text', 'class': 'form-control mb-2'}))
    category = forms.ChoiceField(choices=CATEGORIES, required=True)
    qty = forms.IntegerField(min_value=1, required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Введите количество',
               'type': 'text', 'class': 'form-control mb-2'}))
    cost = forms.DecimalField(max_digits=7, decimal_places=2, required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Введите цену',
               'type': 'text', 'class': 'form-control mb-2'}))


class SearchForm(forms.Form):
    search = forms.CharField(max_length=200, required=True, label='Название',
                             widget=forms.TextInput(
                                 attrs={'placeholder': 'Введите название',
                                        'type': 'text', 'class': 'form-control mb-2'}))
