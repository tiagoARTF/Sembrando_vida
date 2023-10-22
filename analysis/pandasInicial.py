import pandas as pd
import random

pd.set_option('display.max_rows', None)  
pd.set_option('display.max_columns', None)

def lista_municipios():
    municipios_antioquia = ["Medellín", "Bello", "Itagüí", "Envigado", "Sabaneta", "Rionegro", "La Ceja", "Caldas", "Copacabana", "Girardota", "Barbosa", "Caucasia", "Apartadó", "Turbo", "Necoclí", "Yarumal", "Amalfi", "Segovia", "Yolombó", "Caracolí", "San Pedro", "Abejorral", "Sonsón", "Marinilla", "Guatapé", "Peñol", "San Carlos", "San Rafael", "Gómez Plata", "Puerto Berrío", "Puerto Nare", "Nechí", "Zaragoza", "Cáceres", "Tarazá", "Valdivia", "Anorí", "Maceo", "Yondó", "Cisneros", "Belmira", "Campamento", "Santa Rosa de Osos", "Angostura", "Briceño", "Donmatías", "San Andrés de Cuerquía", "Valparaíso", "Frontino", "Dabeiba", "Uramita", "Murindó", "Liborina", "Cañasgordas", "Toledo", "Buriticá", "Salgar", "Fredonia", "Betania", "Ciudad Bolívar", "Salcedo", "Concepción", "Vigía del Fuerte", "Arboletes", "Bagre", "Nechí", "Zaragoza", "Cáceres", "Tarazá", "Valdivia", "Anorí", "Maceo", "Yondó", "Cisneros", "Belmira", "Campamento", "Santa Rosa de Osos", "Angostura", "Briceño", "Donmatías", "San Andrés de Cuerquía", "Valparaíso", "Frontino", "Dabeiba", "Uramita", "Murindó", "Liborina", "Cañasgordas", "Toledo", "Buriticá", "Salgar", "Fredonia", "Betania", "Ciudad Bolívar", "Salcedo", "Concepción", "Vigía del Fuerte", "Arboletes", "Bagre", "Caracolí", "San Pedro", "Abejorral", "Sonsón", "Marinilla", "Guatapé", "Peñol", "San Carlos", "San Rafael", "Gómez Plata", "Puerto Berrío", "Puerto Nare", "Nechí", "Zaragoza", "Cáceres", "Tarazá", "Valdivia", "Anorí", "Maceo", "Yondó", "Cisneros", "Belmira", "Campamento", "Santa Rosa de Osos", "Angostura", "Briceño", "Donmatías", "San Andrés de Cuerquía", "Valparaíso", "Frontino", "Dabeiba", "Uramita", "Murindó", "Liborina", "Cañasgordas", "Toledo", "Buriticá", "Salgar", "Fredonia", "Betania", "Ciudad Bolívar", "Salcedo", "Concepción", "Vigía del Fuerte", "Arboletes", "Bagre"]
    
    municipios = random.choices(municipios_antioquia, k=2000)
    arboles_tipo = ["Pino", "Eucalipto", "Roble", "Cedro", "Nogal", "Laurel"]
    
    listmuni = []
    
    for municipio in municipios:
        arbol_tipo = random.choice(arboles_tipo)
        arboles_cantidad = random.randint(100, 500)
        listmuni.append({"Municipio": municipio, "Tipo de Árboles": arbol_tipo, "Cantidad de Árboles": arboles_cantidad})
    
    municipios_df = pd.DataFrame(listmuni)
    return municipios_df

listmuni = lista_municipios()

print(listmuni)
