import phonenumbers
number="+918885306551"
from phonenumbers import geocoder
cnum=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(cnum,"en"))
from phonenumbers import carrier
snum=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(snum,"en"))
