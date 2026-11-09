"""El único error del paquete.

Fallo cerrado: ante un dato que no permite medir, se detiene y explica por
qué. Nunca completa ni aproxima para poder devolver un número.
"""


class MedidaImposible(ValueError):
    """Los datos recibidos no permiten calcular la cantidad pedida."""
