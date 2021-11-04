from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect

from account.models import Account
from addresses.forms import AddressFormProfile
from addresses.models import Address
from conf.conf import Locations, Titles
from user_profile.forms import ProfileForm


def index(req):
    context = {
        "title": Titles.USER_PROFILE.value,
        "profile_form": ProfileForm(),
        "address_form": AddressFormProfile()
    }
    if req.method == "GET":
        return render(req, Locations.USER_PROFILE.value, context)
    elif req.method == "POST":
        try:
            profile = Account.objects.update(
                username=req.POST["username"],
                email=req.POST["email"],
                image=req.POST["image"],
                first_name=req.POST["first_name"],
                last_name=req.POST["last_name"],
                phone=req.POST["phone"],
                about=req.POST["about"],
            )
            profile.save()
            messages.success(req, f"✨ ✨ ✨ Successfully updated {profile.username}! ✨ ✨ ✨")
            address = Address.objects.update(
                street=req.POST["street"],
                postcode=req.POST["postcode"],
                city=req.POST["citry"],
                country=req.POST["country"],
                user=req.POST["user"]
            )
            address.save()
            messages.success(req, f"✨ ✨ ✨ Successfully updated {address.street}! ✨ ✨ ✨")
        except IntegrityError:
            messages.error("🤔 🤔 🤔 Something went wrong. 🤔 🤔 🤔")
        return redirect(index)
