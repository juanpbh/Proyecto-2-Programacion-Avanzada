from typing import List
import os

def word_wrap(words: List[str], max_width: int) -> List[str]:
    """
    Función para organizar palabras en líneas con un ancho máximo de caracteres, minimizando el costo del espacio en blanco.

    Args:
        words (List[str]): Lista de palabras a organizar.
        max_width (int): Ancho máximo de cada línea.

    Returns:
        List[str]: Lista de líneas organizadas.
    """
    n = len(words)
    dp = [float('inf')] * n
    ans = [0] * n
    dp[-1] = 0

    for i in range(n - 2, -1, -1):
        length = -1
        for j in range(i, n):
            length += len(words[j]) + 1
            if length > max_width:
                break
            if j == n - 1:
                cost = 0
            else:
                cost = (max_width - length) ** 2 + dp[j + 1]
            if cost < dp[i]:
                dp[i] = cost
                ans[i] = j + 1

    i = 0
    lines = []
    while i < n:
        line = ' '.join(words[i:ans[i]])
        lines.append(line)
        i = ans[i]

    return lines

def word_wrap_file_crud():
    """
    Función para manejar operaciones CRUD relacionadas con el word wrap.
    """
    while True:
        print("Seleccione una operación CRUD para el word wrap:")
        print("1. Crear archivo con resultado de word wrap")
        print("2. Leer archivo con resultado de word wrap")
        print("3. Actualizar archivo con resultado de word wrap")
        print("4. Eliminar archivo con resultado de word wrap")
        print("5. Regresar al menú principal")

        option = input("Ingrese su opción: ")

        if option == '1':
            input_path = input("Ingrese la ruta del archivo de texto: ").strip('"')
            max_width = int(input("Ingrese el ancho máximo: "))
            output_path = input("Ingrese la ruta del archivo nuevo donde se guardará el texto organizado: ").strip('"')
            with open(input_path, 'r') as file:
                words = file.read().split()
            wrapped_text = word_wrap(words, max_width)
            with open(output_path, 'w') as file:
                file.write('\n'.join(wrapped_text))
            print(f"Texto organizado y guardado en {output_path}.")
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
            max_width = int(input("Ingrese el ancho máximo: "))
            output_path = input("Ingrese la ruta del archivo de texto a actualizar: ").strip('"')
            with open(input_path, 'r') as file:
                words = file.read().split()
            wrapped_text = word_wrap(words, max_width)
            with open(output_path, 'w') as file:
                file.write('\n'.join(wrapped_text))
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
