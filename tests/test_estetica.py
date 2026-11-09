import pytest

from ethosemiotics import LecturaEstetica, MedidaImposible, belleza, lectura_estetica


def test_el_signo_lo_decide_el_acoplamiento() -> None:
    # Mismo orden interno, acoplamiento opuesto: el tumor y el bosque.
    assert lectura_estetica(belleza(1.0, 9.0, 1.0)) is LecturaEstetica.SINTROPIA_LUMINOSA
    assert lectura_estetica(belleza(-1.0, 9.0, 1.0)) is LecturaEstetica.SINTROPIA_OSCURA
    assert lectura_estetica(belleza(0.0, 9.0, 1.0)) is LecturaEstetica.INERCIA_TRIVIAL


def test_entropia_nula_no_devuelve_infinito() -> None:
    with pytest.raises(MedidaImposible):
        belleza(0.5, 1.0, 0.0)
