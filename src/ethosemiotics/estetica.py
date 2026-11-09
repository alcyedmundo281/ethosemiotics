"""Ecuación vectorial de la estética: B = Φ · (S_int / N_int).

La eficiencia interna de un sistema (sintropía sobre entropía) no basta
para llamarlo bello: un tumor o una organización criminal tienen un orden
interno férreo. Φ, el acoplamiento con el entorno, decide el signo.
"""

import math
from enum import Enum

from .errores import MedidaImposible


class LecturaEstetica(str, Enum):
    SINTROPIA_LUMINOSA = "sintropia_luminosa"
    INERCIA_TRIVIAL = "inercia_trivial"
    SINTROPIA_OSCURA = "sintropia_oscura"


def belleza(phi: float, sintropia_interna: float, entropia_interna: float) -> float:
    """B = Φ · (S_int / N_int).

    Con entropía interna nula el cociente no está definido: no se devuelve
    infinito, se rechaza la medida.
    """
    if not -1.0 <= phi <= 1.0:
        raise MedidaImposible("Φ debe estar en [−1, +1]")
    if not math.isfinite(sintropia_interna) or sintropia_interna < 0:
        raise MedidaImposible("La sintropía interna debe ser finita y no negativa")
    if not math.isfinite(entropia_interna) or entropia_interna <= 0:
        raise MedidaImposible("La entropía interna debe ser finita y positiva")
    return phi * (sintropia_interna / entropia_interna)


def lectura_estetica(valor_b: float) -> LecturaEstetica:
    """El signo de B, que es el signo de Φ."""
    if valor_b > 0:
        return LecturaEstetica.SINTROPIA_LUMINOSA
    if valor_b < 0:
        return LecturaEstetica.SINTROPIA_OSCURA
    return LecturaEstetica.INERCIA_TRIVIAL
