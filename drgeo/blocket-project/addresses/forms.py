from django import forms

from addresses.models import Address


class AddressFormProfile(forms.Form):
    address = forms.CharField(max_length=30)
    postcode = forms.IntegerField()
    city = forms.CharField()
    country = forms.CharField(max_length=30)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["address"].widget.attrs.update({
            "required": "",
            "type": "text",
            "class": "form-control",
            "id": "address",
            "placeholder": "Address"
        })
        self.fields["postcode"].widget.attrs.update({
            "required": "",
            "type": "text",
            "class": "form-control",
            "id": "postcode",
            "placeholder": "Postcode"
        })
        self.fields["city"].widget.attrs.update({
            "required": "",
            "type": "text",
            "class": "form-control",
            "id": "city",
            "placeholder": "City"
        })
        self.fields["country"].widget.attrs.update({
            "required": "",
            "type": "text",
            "class": "form-control",
            "id": "country",
            "placeholder": "Country"
        })

        class Meta:
            model = Address
            fields =[
                "address",
                "postcode",
                "city",
                "country",
            ]