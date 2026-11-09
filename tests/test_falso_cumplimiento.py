import pytest

from ethosemiotics import MedidaImposible, evaluar_cumplimiento


def test_intencion_alta_sin_anclaje() -> None:
    assert evaluar_cumplimiento(0.9, 0.1).falso


def test_intencion_alta_con_anclaje() -> None:
    assert not evaluar_cumplimiento(0.9, 0.8).falso


def test_umbrales_configurables() -> None:
    assert evaluar_cumplimiento(0.5, 0.1, umbral_intencion=0.4).falso


def test_fuera_de_rango_falla_cerrado() -> None:
    with pytest.raises(MedidaImposible):
        evaluar_cumplimiento(1.2, 0.1)
