import pytest

from ethosemiotics import ComponenteErgon, EstadoSintropico, MedidaImposible, ergon_total


def test_costo_sin_fuente_no_se_admite() -> None:
    with pytest.raises(MedidaImposible):
        ComponenteErgon("soporte vasoactivo", 10.0, "puntos", "  ")


def test_unidades_incompatibles_no_se_suman() -> None:
    a = ComponenteErgon("a", 1.0, "puntos", "cita A")
    b = ComponenteErgon("b", 2.0, "horas", "cita B")
    with pytest.raises(MedidaImposible):
        ergon_total([a, b])


def test_suma_en_una_misma_unidad() -> None:
    a = ComponenteErgon("a", 1.5, "puntos", "cita A")
    b = ComponenteErgon("b", 2.5, "puntos", "cita B")
    assert ergon_total([a, b]) == 4.0


def test_estado_rechaza_negativos() -> None:
    with pytest.raises(MedidaImposible):
        EstadoSintropico(sintropia=1.0, entropia=-0.1, ergon=0.0)
