import sys
import time
import re


def fatorial(n: int) -> int:
    """
    Calcula n! de forma recursiva.

    Ideia:
    - caso base: 0! = 1 e 1! = 1
    - passo recursivo: n! = n * (n - 1)!
    """
    # Fatorial de número negativo não existe nesse contexto.
    if n < 0:
        raise ValueError("n deve ser >= 0")

    # Aqui a recursão para.
    if n == 0 or n == 1:
        return 1

    # Chamada recursiva reduzindo o problema em 1 unidade.
    return n * fatorial(n - 1)


def medir_tempo(n: int) -> tuple[int, int, float, int]:
    """
    Mede o tempo para calcular fatorial(n) e retorna:
    (n, resultado, tempo_em_segundos, qtd_digitos_do_resultado).
    """
    inicio = time.perf_counter()
    resultado = fatorial(n)
    fim = time.perf_counter()

    tempo = fim - inicio
    digitos = len(str(resultado))
    return n, resultado, tempo, digitos


def ler_lista_inteiros(entrada: str) -> list[int]:
    """
    Converte uma string em lista de inteiros.
    Exemplos aceitos: "3,5,7", "3 5 7", "[3, 5, 7]".
    """
    texto = entrada.strip()
    if texto.startswith("[") and texto.endswith("]"):
        texto = texto[1:-1]

    tokens = [token for token in re.split(r"[,\s;]+", texto) if token]
    if not tokens:
        raise ValueError("Informe ao menos um inteiro.")

    try:
        valores = [int(token) for token in tokens]
    except ValueError as exc:
        raise ValueError("A entrada deve conter apenas inteiros.") from exc

    if any(valor < 0 for valor in valores):
        raise ValueError("Todos os valores devem ser >= 0.")
    return valores


def main():
    try:
        entrada = input(
            "Digite um inteiro n ou uma lista de inteiros (ex.: 7 ou 10,100,500,1000): "
        )
        valores = ler_lista_inteiros(entrada)
    except ValueError as erro:
        print(f"Erro: {erro}")
        raise SystemExit(1) from erro

    # Ajusta limite de recursão só quando precisar.
    maior_valor = max(valores)
    limite_necessario = maior_valor + 50
    if limite_necessario > sys.getrecursionlimit():
        sys.setrecursionlimit(limite_necessario)

    print("\nResultados:")
    print(f"{'n':>6} {'n!':>20} {'tempo (s)':>12} {'qtd. dígitos':>13}")
    for n in valores:
        n_med, resultado, tempo, digitos = medir_tempo(n)
        print(f"{n_med:>6} {resultado:>20} {tempo:>12.10f} {digitos:>13}")



if __name__ == "__main__":
    main()



# Recorrência da função fatorial recursiva:
#   T(n) = T(n - 1) + O(1)
# Cada chamada faz trabalho constante e chama para n-1,
# então o tempo cresce linearmente com n:
#   Complexidade assintótica: O(n)
#
# Tempos medidos (variam a cada execução):
#   n = 10   -> 0.0000025000 s
#   n = 100  -> 0.0000166000 s
#   n = 500  -> 0.0001224000 s
#   n = 1000 -> 0.0003565000 s
