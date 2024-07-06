import os

def longest_common_substring(s1: str, s2: str) -> str:
    """
    Función para encontrar la subcadena común más larga entre dos cadenas.

    Args:
        s1 (str): Primera cadena.
        s2 (str): Segunda cadena.

    Returns:
        str: Subcadena común más larga.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    length = 0
    ending_index = m

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > length:
                    length = dp[i][j]
                    ending_index = i
            else:
                dp[i][j] = 0

    return s1[ending_index - length: ending_index]

def longest_common_substring_file_crud():
    """
    Función para manejar operaciones CRUD relacionadas con la subcadena común más larga.
    """
    while True:
        print("Seleccione una operación CRUD para la subcadena común más larga:")
        print("1. Crear archivo con la subcadena común más larga")
        print("2. Leer archivo con la subcadena común más larga")
        print("3. Actualizar archivo con la subcadena común más larga")
        print("4. Eliminar archivo con la subcadena común más larga")
        print("5. Regresar al menú principal")

        option = input("Ingrese su opción: ")

        if option == '1':
            input_path1 = input("Ingrese la ruta del primer archivo de texto: ").strip('"')
            input_path2 = input("Ingrese la ruta del segundo archivo de texto: ").strip('"')
            output_path = input("Ingrese la ruta del archivo nuevo donde se guardará el resultado: ").strip('"')
            with open(input_path1, 'r') as file1, open(input_path2, 'r') as file2:
                s1 = file1.read()
                s2 = file2.read()
            result = longest_common_substring(s1, s2)
            with open(output_path, 'w') as file:
                file.write(result)
            print(f"Subcadena común más larga guardada en {output_path}.")
        elif option == '2':
            file_path = input("Ingrese la ruta del archivo de texto: ").strip('"')
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                print(f"Contenido del archivo:\n{content}")
            except FileNotFoundError:
                print("El archivo no existe.")
        elif option == '3':
            input_path1 = input("Ingrese la ruta del primer archivo de texto: ").strip('"')
            input_path2 = input("Ingrese la ruta del segundo archivo de texto: ").strip('"')
            output_path = input("Ingrese la ruta del archivo de texto a actualizar: ").strip('"')
            with open(input_path1, 'r') as file1, open(input_path2, 'r') as file2:
                s1 = file1.read()
                s2 = file2.read()
            result = longest_common_substring(s1, s2)
            with open(output_path, 'w') as file:
                file.write(result)
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
