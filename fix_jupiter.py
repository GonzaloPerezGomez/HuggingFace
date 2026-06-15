import json
import os

# Filtramos solo los notebooks del directorio actual
notebooks = [x for x in os.listdir('.') if x.endswith('.ipynb')]

for archivo in notebooks:
    print(f"Revisando: {archivo}...")
    try:
        # 1. Leemos el archivo explícitamente con f_in
        with open(archivo, 'r', encoding='utf-8') as f_in:
            nb = json.load(f_in)

        # 2. Buscamos y eliminamos los metadatos de los widgets
        if 'widgets' in nb.get('metadata', {}):
            del nb['metadata']['widgets']
            
            # 3. Escribimos los cambios usando f_out
            with open(archivo, 'w', encoding='utf-8') as f_out:
                json.dump(nb, f_out, indent=1)
                
            print(f" -> ¡Arreglado! Ya puedes abrir este notebook.")
        else:
            print(" -> Todo OK. No se encontró la llave 'widgets'.")
            
    except Exception as e:
        print(f" -> Hubo un error al procesar {archivo}: {e}")
        
print("\n¡Proceso finalizado!")