## pip3 install phonenumbers

import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier 

phone_number = phonenumbers.parse("+919912401019")

print( geocoder.description_for_number( phone_number, 'en'))
print( carrier.name_for_number( phone_number, 'en'))



