import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

phone_number = input("Ingresa el telefono: ")

data = phonenumbers.parse(phone_number)
print(geocoder.description_for_number(data,'es'))
print(carrier.name_for_number(data,'es'))