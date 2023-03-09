import phonenumbers

telefone = input('Digite o telefone no formato 11999999999: ')
telefone_formatado = phonenumbers.parse(telefone, "BR")
print(telefone_formatado)

#descobrir a localização do telefone
from phonenumbers import geocoder
local = geocoder.description_for_number(telefone_formatado, "pt")
print(local)

#descobrir o operadora do telefone
from phonenumbers import carrier
operadora = carrier.name_for_number(telefone_formatado, "pt")
print(operadora)
