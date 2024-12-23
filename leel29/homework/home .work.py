


def threeproduct(a, b, c):
    product = a * b * c
    print(product)


def greet(name):
  print(f"hello")


def comparison(a, b):
    print(f"{a} < {b}: {a < b}")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} <= {b}: {a <= b}")
    print(f"{a} >= {b}: {a >= b}")

def agecalc(age):
    from datetime import datetime
    current_year = datetime.now().year
    birth_year = current_year - age
