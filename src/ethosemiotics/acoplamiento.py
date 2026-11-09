"""Coeficiente de acoplamiento Φ: las primitivas aritméticas.

La construcción de los vectores (qué hallazgo va en qué dimensión, con qué
peso ln(LR)) pertenece a holonmed, porque depende de sus infones y de sus
protocolos. Aquí vive sólo la aritmética que holonmed aplica a esos
vectores, para que la fórmula esté escrita en un único sitio.

Cada función reproduce exactamente el comportamiento de
`holonmed/core/acoplamiento.py` v0.5.0. Las pruebas lo fijan; si una de
las dos cambia, la otra tiene que cambiar en el mismo ciclo.

Atribución: la fórmula vectorial −1/+1 es original de HolonMed; la idea
de acoplamiento con la realidad es pragmatista y deriva de Peirce.
"""

import math
from collections.abc import Sequence
from enum import Enum

from .errores import MedidaImposible

# Bandas de lectura. Son convenciones de presentación, no parte de la
# métrica: Φ es continuo. Mismos valores que holonmed v0.5.0.
UMBRAL_ARMONIA = 0.60
UMBRAL_ACOPLAMIENTO = 0.20
UMBRAL_DESARMONIA = -0.60
UMBRAL_FRICCION = -0.20


class Banda(str, Enum):
    ARMONIA = "armonia"
    ACOPLAMIENTO_PARCIAL = "acoplamiento_parcial"
    INERCIA = "inercia"
    FRICCION = "friccion"
    DESARMONIA = "desarmonia"


def _recortar(valor: float) -> float:
    return max(-1.0, min(1.0, valor))


def coseno(esperado: Sequence[float], observado: Sequence[float]) -> float:
    """cos(h, e) entre el caso de libro y el caso real.

    Si cualquiera de los dos vectores es nulo devuelve 0: no hay evidencia
    que acople, y eso es inercia, no contradicción. Se recorta a [−1, +1]
    para absorber el error de coma flotante.
    """
    if len(esperado) != len(observado):
        raise MedidaImposible(
            f"Los vectores tienen dimensiones distintas: {len(esperado)} y {len(observado)}"
        )
    for valor in (*esperado, *observado):
        if not math.isfinite(valor):
            raise MedidaImposible("Un componente del vector no es un número finito")
    producto = sum(h * e for h, e in zip(esperado, observado, strict=True))
    norma_h = math.sqrt(sum(h * h for h in esperado))
    norma_e = math.sqrt(sum(e * e for e in observado))
    if norma_h == 0 or norma_e == 0:
        return 0.0
    return _recortar(producto / (norma_h * norma_e))


def phi_categorico(suma: int, dimensiones: int, medidos: int, resto: int = 0) -> float:
    """Φ categórico: el coseno con pesos ±1, escrito sin cancelar.

        Φ_cat = Σeᵢ / √(D · (medidos + r))

    Si no se ha medido nada devuelve 0, igual que holonmed.
    """
    if dimensiones <= 0:
        raise MedidaImposible("Sin dimensiones declaradas no hay espacio donde medir Φ")
    if medidos < 0 or resto < 0:
        raise MedidaImposible("Los conteos no pueden ser negativos")
    if abs(suma) > medidos:
        raise MedidaImposible("La suma de contribuciones ±1 no puede exceder lo medido")
    if medidos == 0:
        return 0.0
    return suma / math.sqrt(dimensiones * (medidos + resto))


def anclaje(confianza: float, procedencia: float, fuente: float) -> float:
    """α: media geométrica de tres factores en [0, 1].

    Geométrica para que el colapso de uno solo baste: un argumento
    impecable sobre likelihood ratios sin fuente no es medio verdadero, es
    irrelevante.
    """
    for nombre, valor in (
        ("confianza", confianza),
        ("procedencia", procedencia),
        ("fuente", fuente),
    ):
        if not math.isfinite(valor) or valor > 1.0:
            raise MedidaImposible(
                f"El factor {nombre} debe estar en [0, 1]; vale {valor}"
            )
    producto = max(confianza, 0.0) * max(procedencia, 0.0) * max(fuente, 0.0)
    return float(producto ** (1 / 3))


def phi(coseno_hipotesis: float, alfa: float) -> float:
    """Φ = cos(h, e) · α, recortado a [−1, +1]."""
    if not -1.0 <= coseno_hipotesis <= 1.0:
        raise MedidaImposible("El coseno debe estar en [−1, +1]")
    if not 0.0 <= alfa <= 1.0:
        raise MedidaImposible("El anclaje α debe estar en [0, 1]")
    return _recortar(coseno_hipotesis * alfa)


def banda(valor_phi: float) -> Banda:
    """Lectura por bandas de un Φ continuo."""
    if valor_phi >= UMBRAL_ARMONIA:
        return Banda.ARMONIA
    if valor_phi >= UMBRAL_ACOPLAMIENTO:
        return Banda.ACOPLAMIENTO_PARCIAL
    if valor_phi <= UMBRAL_DESARMONIA:
        return Banda.DESARMONIA
    if valor_phi <= UMBRAL_FRICCION:
        return Banda.FRICCION
    return Banda.INERCIA
