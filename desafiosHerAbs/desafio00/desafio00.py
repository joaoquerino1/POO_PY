from rich import print, inspect
from poligono import *

def main():
    p1 = Quadrado(12)

    print(f"Perímetro do quadrado: {p1.perimetro():.1f}")
    print(f"Área do quadrado: {p1.area():.1f}")

    p2 = Circulo(20)

    print(f"Perímetro do círculo: {p2.perimetro():.1f}")
    print(f"Área do círculo: {p2.area():.1f}")



if __name__ == "__main__":
    main()