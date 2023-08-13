import math

def fatorial(n):
    return math.factorial(n)

def arranjos_simples(n, r):
    return fatorial(n) // fatorial(n - r)

def permutacao_simples(n):
    return fatorial(n)

def combinacao(n, r):
    return fatorial(n) // (fatorial(r) * fatorial(n - r))

def permutacao_repeticao(n, r_list):
    denominator = 1
    for r in r_list:
        denominator *= fatorial(r)
    return fatorial(sum(r_list)) // denominator

# Exemplos de uso
n = 5
r = 3
r_list = [2, 1, 2]

print(f"Fatorial de {n}: {fatorial(n)}")
print(f"Arranjos simples de {n} elementos escolhendo {r}: {arranjos_simples(n, r)}")
print(f"Permutação simples de {n} elementos: {permutacao_simples(n)}")
print(f"Combinação de {n} elementos escolhendo {r}: {combinacao(n, r)}")
print(f"Permutação com elementos repetidos de {r_list}: {permutacao_repeticao(n, r_list)}")