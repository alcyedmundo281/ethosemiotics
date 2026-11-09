import math

import pytest

from ethosemiotics import (
    Banda,
    MedidaImposible,
    anclaje,
    banda,
    coseno,
    phi,
    phi_categorico,
)


def test_polos_del_coseno() -> None:
    h = [math.log(5.0), math.log(3.0)]
    assert coseno(h, h) == pytest.approx(1.0)
    assert coseno(h, [-x for x in h]) == pytest.approx(-1.0)
    assert coseno([1.0, 0.0], [0.0, 1.0]) == pytest.approx(0.0)


def test_vector_nulo_es_inercia_no_contradiccion() -> None:
    assert coseno([1.0, 2.0], [0.0, 0.0]) == 0.0


def test_dimensiones_distintas_fallan_cerrado() -> None:
    with pytest.raises(MedidaImposible):
        coseno([1.0], [1.0, 2.0])


def test_resto_no_simbolizado_baja_el_coseno_sin_castigo_ad_hoc() -> None:
    # Una dimensión extra con h = 0 y e ≠ 0 es ortogonal: sólo crece ‖e‖.
    completo = coseno([1.0, 1.0], [1.0, 1.0])
    con_resto = coseno([1.0, 1.0, 0.0], [1.0, 1.0, 1.0])
    assert con_resto < completo


def test_phi_categorico_y_el_polo_inalcanzable_con_resto() -> None:
    assert phi_categorico(2, 2, 2) == pytest.approx(1.0)
    assert phi_categorico(-2, 2, 2) == pytest.approx(-1.0)
    assert phi_categorico(2, 2, 2, resto=6) < 1.0
    assert phi_categorico(0, 3, 0) == 0.0


def test_anclaje_colapsa_si_falta_la_fuente() -> None:
    assert anclaje(1.0, 1.0, 0.0) == 0.0
    assert anclaje(1.0, 1.0, 1.0) == pytest.approx(1.0)
    assert anclaje(0.8, 0.6, 1.0) == pytest.approx((0.8 * 0.6) ** (1 / 3))


def test_sin_anclaje_phi_es_irrelevante_no_falso() -> None:
    assert phi(0.95, 0.0) == 0.0
    assert banda(phi(0.95, 0.0)) is Banda.INERCIA


@pytest.mark.parametrize(
    ("valor", "esperada"),
    [
        (0.60, Banda.ARMONIA),
        (0.20, Banda.ACOPLAMIENTO_PARCIAL),
        (0.0, Banda.INERCIA),
        (-0.20, Banda.FRICCION),
        (-0.60, Banda.DESARMONIA),
    ],
)
def test_bandas_iguales_a_holonmed(valor: float, esperada: Banda) -> None:
    assert banda(valor) is esperada
