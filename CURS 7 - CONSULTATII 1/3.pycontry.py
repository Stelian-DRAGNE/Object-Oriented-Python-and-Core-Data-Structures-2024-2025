
import pycountry

print(len(pycountry.countries))

# Pentru a itera prin tari
contry_codes = []
for country in pycountry.countries:
    contry_codes.append(country.alpha_2)

print(contry_codes)

germany = pycountry.countries.get(alpha_2='DE')
print(germany)