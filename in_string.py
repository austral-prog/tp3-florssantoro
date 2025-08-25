def check_vowels():
    nombre = input()
    a = "a" in nombre or "A" in nombre
    e = "e" in nombre or "E" in nombre
    i = "i" in nombre or "I" in nombre
    o = "o" in nombre or "O" in nombre
    u = "u" in nombre or "U" in nombre

    print(f"Contiene a: {a}")
    print(f"Contiene e: {e}")
    print(f"Contiene i: {i}")
    print(f"Contiene o: {o}")
    print(f"Contiene u: {u}")
    
    # Código a implementar utilizando input.

check_vowels()

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
