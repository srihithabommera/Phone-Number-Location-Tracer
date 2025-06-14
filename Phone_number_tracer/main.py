import phonenumbers as pn
from phonenumbers import geocoder as gc
phone_number1=pn.parse("+917893970755")
phone_number2=pn.parse("+908500664411")
print("\nPhone Numbers Location: ")
print(gc.description_for_number(phone_number1,"en"))
print(gc.description_for_number(phone_number2,"en"))