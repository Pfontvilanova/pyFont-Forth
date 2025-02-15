from forth_module import Forth

def main():
    forth = Forth()
    
    # Ejecutar código Forth desde Python
    result = forth.run("3 5 +")
    print(f"Resultado de '3 5 +': {result}")
    
    result = forth.run("10 2 /")
    print(f"Resultado de '10 2 /': {result}")
    
    result = forth.run("5 dup *")
    print(f"Resultado de '5 dup *': {result}")

if __name__ == "__main__":
    main()
