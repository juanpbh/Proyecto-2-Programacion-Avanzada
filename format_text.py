from typing import List
import os

def format_text(text: str, maxWidth: int) -> List[str]:
    """
    Función para formatear el texto justificándolo según un ancho máximo.

    Args:
        text (str): Texto a formatear.
        maxWidth (int): Ancho máximo de cada línea.

    Returns:
        List[str]: Lista de líneas formateadas.
    """
    if not (1 <= len(text) <= 1000):
        raise ValueError("La longitud del texto debe estar entre 1 y 1000 caracteres.")
    if not (1 <= maxWidth <= 100):
        raise ValueError("El ancho máximo debe estar entre 1 y 100.")

    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > maxWidth:
            spaces_to_add = maxWidth - current_length
            if len(current_line) == 1:
                lines.append(current_line[0].ljust(maxWidth))
            else:
                for i in range(spaces_to_add):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                lines.append(''.join(current_line))
            current_line, current_length = [], 0
        current_line.append(word)
        current_length += len(word)

    lines.append(' '.join(current_line).ljust(maxWidth))
    return lines

def format_text_file_crud():
    """
    Función para manejar operaciones CRUD relacionadas con el formateo de texto.
    """
    while True:
        print("Seleccione una operación CRUD para formatear texto:")
        print("1. Crear archivo de texto formateado")
        print("2. Leer archivo de texto formateado")
        print("3. Actualizar archivo de texto formateado")
        print("4. Eliminar archivo de texto formateado")
        print("5. Regresar al menú principal")

        option = input("Ingrese su opción: ")

        if option == '1':
            input_path = input("Ingrese la ruta del archivo de texto de entrada: ").strip('"')
            max_width = int(input("Ingrese el ancho máximo: "))
            output_path = input("Ingrese la ruta del archivo nuevo donde se guardará el texto formateado: ").strip('"')
            with open(input_path, 'r') as file:
                text = file.read()
            formatted_text = format_text(text, max_width)
            with open(output_path, 'w') as file:
                file.write('\n'.join(formatted_text))
            print(f"Texto formateado y guardado en {output_path}.")
        elif option == '2':
            file_path = input("Ingrese la ruta del archivo de texto formateado: ").strip('"')
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                print(f"Contenido del archivo:\n{content}")
            except FileNotFoundError:
                print("El archivo no existe.")
        elif option == '3':
            input_path = input("Ingrese la ruta del archivo de texto de entrada: ").strip('"')
            max_width = int(input("Ingrese el ancho máximo: "))
            output_path = input("Ingrese la ruta del archivo de texto formateado a actualizar: ").strip('"')
            with open(input_path, 'r') as file:
                text = file.read()
            formatted_text = format_text(text, max_width)
            with open(output_path, 'w') as file:
                file.write('\n'.join(formatted_text))
            print(f"Archivo actualizado en {output_path}.")
        elif option == '4':
            file_path = input("Ingrese la ruta del archivo de texto formateado a eliminar: ").strip('"')
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Archivo {file_path} eliminado.")
            else:
                print(f"El archivo {file_path} no existe.")
        elif option == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
