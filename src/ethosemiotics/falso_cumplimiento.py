"""Falso cumplimiento: alta intención (pathos) sin validez (logos).

Un acto movido por una intención moral alta pero sin anclaje en la
evidencia —un fármaco ineficaz, un traslado fútil por presión mediática—
es visible y consume recursos que el trabajo humilde necesitaba.

La validez se lee con el mismo anclaje α que usa Φ. Los umbrales son
configuración con valor por defecto explícito, no constantes ocultas.
"""

from dataclasses import dataclass, field

from .errores import MedidaImposible

UMBRAL_INTENCION_ALTA = 0.60
UMBRAL_ANCLAJE_BAJO = 0.20


@dataclass(frozen=True)
class Cumplimiento:
    falso: bool
    traza: list[str] = field(default_factory=list)


def evaluar_cumplimiento(
    intencion: float,
    alfa: float,
    *,
    umbral_intencion: float = UMBRAL_INTENCION_ALTA,
    umbral_anclaje: float = UMBRAL_ANCLAJE_BAJO,
) -> Cumplimiento:
    """Marca falso cumplimiento cuando la intención es alta y α es bajo."""
    for nombre, valor in (
        ("intención", intencion),
        ("α", alfa),
        ("umbral de intención", umbral_intencion),
        ("umbral de anclaje", umbral_anclaje),
    ):
        if not 0.0 <= valor <= 1.0:
            raise MedidaImposible(f"{nombre} debe estar en [0, 1]; vale {valor}")
    intencion_alta = intencion >= umbral_intencion
    anclaje_bajo = alfa <= umbral_anclaje
    traza = [
        f"intención = {intencion:.2f} (alta si ≥ {umbral_intencion:.2f})",
        f"α = {alfa:.2f} (bajo si ≤ {umbral_anclaje:.2f})",
    ]
    falso = intencion_alta and anclaje_bajo
    traza.append(
        "Falso cumplimiento: intención alta sin anclaje en la evidencia"
        if falso
        else "Sin falso cumplimiento"
    )
    return Cumplimiento(falso=falso, traza=traza)
