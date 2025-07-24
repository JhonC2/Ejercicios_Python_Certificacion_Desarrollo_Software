'''
Estrellas mas cercanas a la Tierra

estrella1 = 'Sol'
estrella2 = 'Alfa Centauri'
estrella3 = 'Estrella de Barnard'
estrella4 = 'Luhman 16'

Montanas mas altas en cada placa tectonica

Africana = 'Kilimanjaro'
Antartica = 'Macizo Vinson'
Indoaustraliana = 'Monte Jaya'
Euroasiatica = 'Everest'
Norteamerica = 'Monte Denali'
Pacifico = 'Volcan Mauna Kea'
Suramericana = 'Aconcagua'
'''

# Sustituir las variables del primer grupo por una lista denominada <estrellas>

estrellas = [
    'Sol',
    'Alfa Centauri',
    'Estrella de Barnard',
    'Luhman 16'
]

# Imprimir el nombre de la cuarta estrella mas cercana a la tierra

print(estrellas[3])

# Crear un diccionario <montanas> del segundo grupo con todos los valores

montanas = {
    'Africana': 'Kilimanjaro',
    'Antartica': 'Macizo Vinson',
    'Indoaustraliana': 'Monte Jaya',
    'Euroasiatica': 'Everest',
    'Norteamerica': 'Monte Denali',
    'Pacifico': 'Volcan Mauna Kea',
    'Suramericana': 'Aconcagua'
}

# Imprimir el nombre de la montana mas alta de la placa del Pacifico

print(montanas['Pacifico'])