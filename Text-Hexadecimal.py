def string_to_hex(input_string):
    hex_output = ''.join(format(ord(c), '02x') for c in input_string)
    return hex_output

while True:
    input_string = input("Introduce un texto: ")
    hex_output = string_to_hex(input_string)
    print(f"Texto en hexadecimal: {hex_output}")

    again = input("¿Quieres convertir otro texto? (Presiona la tecla '1' para si, cualquier otra tecla para salir):" )
    if again.lower() != '1':
        break
