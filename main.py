import sys
from format_text import format_text_file_crud
from longest_common_substring import longest_common_substring_file_crud
from word_break import word_break_file_crud
from word_wrap import word_wrap_file_crud

def main():
    """
    Función principal para manejar las operaciones CRUD y formatear el texto.
    """
    while True:
        print("Seleccione una opción:")
        print("1. Formatear texto")
        print("2. Longest Common Substring")
        print("3. Word Break")
        print("4. Word Wrap")
        print("5. Salir")

        option = input("Ingrese su opción: ")

        if option == '1':
            format_text_file_crud()
        elif option == '2':
            longest_common_substring_file_crud()
        elif option == '3':
            word_break_file_crud()
        elif option == '4':
            word_wrap_file_crud()
        elif option == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
