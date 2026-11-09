"""Ergon: el costo de sostener el estado actual.

Dos pacientes con los mismos signos vitales pueden no estar igual: uno los
mantiene solo y otro con ventilación mecánica y vasopresores. El vector de
estado sintrópico ⟨H, N, E⟩ separa la señal (H), el ruido (N) y el costo
(E) que se paga para sostener esa señal.

Este módulo fija la forma de los datos y una regla: **un costo sin
procedencia no se suma**. Qué escalas clínicas alimentan cada componente
(puntaje vasoactivo-inotrópico, soporte ventilatorio, carga alostática)
es una decisión pendiente de la especificación, no de este código.
"""

import math
from collections.abc import Sequence
from dataclasses import dataclass

from .errores import MedidaImposible


@dataclass(frozen=True)
class ComponenteErgon:
    """Una fuente de costo, con la cita que justifica su escala."""

    nombre: str
    valor: float
    unidad: str
    fuente: str

    def __post_init__(self) -> None:
        if not self.nombre.strip():
            raise MedidaImposible("Un componente del ergon necesita nombre")
        if not math.isfinite(self.valor) or self.valor < 0:
            raise MedidaImposible(
                f"El componente '{self.nombre}' debe ser finito y no negativo"
            )
        if not self.fuente.strip():
            raise MedidaImposible(
                f"El componente '{self.nombre}' no cita fuente: "
                "un costo sin procedencia es un número inventado"
            )


@dataclass(frozen=True)
class EstadoSintropico:
    """⟨H, N, E⟩: sintropía (señal), entropía (ruido) y ergon (costo)."""

    sintropia: float
    entropia: float
    ergon: float

    def __post_init__(self) -> None:
        for nombre in ("sintropia", "entropia", "ergon"):
            valor = getattr(self, nombre)
            if not math.isfinite(valor) or valor < 0:
                raise MedidaImposible(f"{nombre} debe ser finito y no negativo")


def ergon_total(componentes: Sequence[ComponenteErgon]) -> float:
    """Suma de componentes en una misma unidad.

    Sumar unidades distintas sería inventar una escala común; se rechaza.
    """
    if not componentes:
        raise MedidaImposible("Sin componentes no hay ergon que medir")
    unidades = {c.unidad for c in componentes}
    if len(unidades) > 1:
        raise MedidaImposible(f"Unidades incompatibles en el ergon: {sorted(unidades)}")
    return sum(c.valor for c in componentes)
