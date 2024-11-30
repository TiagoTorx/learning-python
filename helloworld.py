# def é a forma de definir uma função. Tudo o que estiver indentado abaixo da função é parte desta função.
# no caso do if, isso possibilita que o código não rode automaticamente caso seja utilizado dentro de outro componente.

def main():
    print("Hello World!")
    name = input ("What is your name? ")
    print("Nice to meet you", name)

if __name__ == "__main__":
    main()