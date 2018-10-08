from collections import namedtuple
import math

Parametros = namedtuple("Parametros", ["p", "o", "w", "a", "y", "pi", "d", "e",
                                       "x", "n", "k", "v", "q", "h"])

def definir_parametros():
    p = 0.04   #p: probabilidad de que llegue un nuevo cliente
    o = 1   #θ (theta): formula de apuesta del cliente
    w = 1   #w: probabilidad de que un dealer descubra a alguien
    a = 1   #α (alfa): probabilidad de tragamonedas
    y = 1   #γ (gamma): rango de números en la ruleta
    pi = math.pi    #π (pi): duración de cada actividad
    d = 1   #δ (delta): minutos que esperará un cliente para hablar
    e = 1   #ε (épsilon): % de disminución de ansiedad al hablar
    x = 1   #χ (ji): aumento en deshonestidad al hablar
    n = 1   #η (eta): aumento en la probabilidad de irse (afecta stamina)
    k = 1   #κ (cappa): % de aumento en la probabilidad de ganar (mafia)
    v = 1   #v: cantidad de rondas a predecir
    q = 0.3   #psi: % de aumento en la probabilidad de ganar al predecir
    h = 10 #cantidad de pasos que da un cliente por instante
    return p, o, w, a, y, pi, d, e, x, n, k, v, q, h


parametros = Parametros(*definir_parametros())








