import InsectClass as i

mosquito = i.Insect(2,4)
housefly = i.Insect(4,8)

mosquito.flight_length()
housefly.flight_length()

print(f'The mosquito can fly up to {mosquito.get_miles()} miles')
print(f'The housefly can fly up to {housefly.get_miles()} miles')