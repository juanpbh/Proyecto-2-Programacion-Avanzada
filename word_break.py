import os

def word_break(s: str, word_dict: set) -> bool:
    """
    Función para determinar si una cadena puede segmentarse en una secuencia de palabras del diccionario.

    Args:
        s (str): Cadena a segmentar.
        word_dict (set): Conjunto de palabras del diccionario.

    Returns:
        bool: True si la cadena puede segmentarse, False en caso contrario.
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]

def word_break_file_crud():
    """
    Función para manejar operaciones CRUD relacionadas con el word break.
    """
    while True:
        print("Seleccione una operación CRUD para el word break:")
        print("1. Crear archivo con resultado de word break")
        print("2. Leer archivo con resultado de word break")
        print("3. Actualizar archivo con resultado de word break")
        print("4. Eliminar archivo con resultado de word break")
        print("5. Regresar al menú principal")

        option = input("Ingrese su opción: ")

        if option == '1':
            input_path = input("Ingrese la ruta del archivo de texto: ").strip('"')
            dict_path = input("Ingrese la ruta del archivo de texto con el diccionario: ").strip('"')
            output_path = input("Ingrese la ruta del archivo nuevo donde se guardará el resultado: ").strip('"')
            with open(input_path, 'r') as file:
                s = file.read().strip()
            with open(dict_path, 'r') as file:
                word_dict = set(file.read().split())
            result = word_break(s, word_dict)
            with open(output_path, 'w') as file:
                file.write('Sí' if result else 'No')
            print(f"Resultado guardado en {output_path}.")
        elif option == '2':
            file_path = input("Ingrese la ruta del archivo de texto: ").strip('"')
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                print(f"Contenido del archivo:\n{content}")
            except FileNotFoundError:
                print("El archivo no existe.")
        elif option == '3':
            input_path = input("Ingrese la ruta del archivo de texto: ").strip('"')
            dict_path = input("Ingrese la ruta del archivo de texto con el diccionario: ").strip('"')
            output_path = input("Ingrese la ruta del archivo de texto a actualizar: ").strip('"')
            with open(input_path, 'r') as file:
                s = file.read().strip()
            with open(dict_path, 'r') as file:
                word_dict = set(file.read().split())
            result = word_break(s, word_dict)
            with open(output_path, 'w') as file:
                file.write('Sí' if result else 'No')
            print(f"Archivo actualizado en {output_path}.")
        elif option == '4':
            file_path = input("Ingrese la ruta del archivo de texto a eliminar: ").strip('"')
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Archivo {file_path} eliminado.")
            else:
                print(f"El archivo {file_path} no existe.")
        elif option == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
