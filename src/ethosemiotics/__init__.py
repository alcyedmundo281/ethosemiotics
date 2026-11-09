"""ethosemiotics — la capa normativa de la Filosofía del Empeño (PoE).

holonmed construye los vectores a partir de los infones de un paciente y
medsemiotics-db define los signos. Este paquete define, en un solo lugar,
las cantidades con las que se juzga una práctica: el acoplamiento Φ, el
ergon, la nitidez estética B y el falso cumplimiento.

Es aritmética determinista y sin dependencias. No conoce pacientes, no
llama a ningún modelo y no persiste nada.
"""

from .acoplamiento import (
    Banda,
    anclaje,
    banda,
    coseno,
    phi,
    phi_categorico,
)
from .ergon import ComponenteErgon, EstadoSintropico, ergon_total
from .errores import MedidaImposible
from .estetica import LecturaEstetica, belleza, lectura_estetica
from .falso_cumplimiento import Cumplimiento, evaluar_cumplimiento

__version__ = "0.1.0"

__all__ = [
    "Banda",
    "ComponenteErgon",
    "Cumplimiento",
    "EstadoSintropico",
    "LecturaEstetica",
    "MedidaImposible",
    "anclaje",
    "banda",
    "belleza",
    "coseno",
    "ergon_total",
    "evaluar_cumplimiento",
    "lectura_estetica",
    "phi",
    "phi_categorico",
]
