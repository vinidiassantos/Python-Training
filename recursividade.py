# 4! = * 3 * 2 * 1 = 24

def fatorial(numero):
        if numero == 0 or numero == 1:
                return 1
        else:
                return numero * fatorial(numero - 1)