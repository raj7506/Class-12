country_code = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
print("Country code for India -")
print(country_code.get('India', 'Not found'))
print("Country code for Japan -")
print(country_code.get('Japan', 'Not found'))

squares = {1 :1,2 :4,3 :9,4 :16,5 :25}
print(squares.pop(4))