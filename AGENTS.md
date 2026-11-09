# ethosemiotics — contrato de ingeniería

## Alcance

ethosemiotics define, en un único lugar, las cantidades normativas de la Filosofía del
Empeño (PoE): el acoplamiento Φ, el vector de estado ⟨H, N, E⟩ con su ergon, la nitidez
estética B y el falso cumplimiento. Es aritmética determinista sin dependencias de
ejecución. No conoce pacientes, no llama a modelos de lenguaje y no persiste nada.

holonmed y medsemiotics-db dependen de este paquete; nunca al revés.

## Reglas no negociables

1. **Nada de datos identificables ni de credenciales en el repositorio.** Los casos de
   prueba son sintéticos.
2. **Fallo cerrado.** Ante un dato que no permite medir, se lanza `MedidaImposible` con el
   motivo. Nunca se completa, aproxima ni devuelve un valor por defecto para continuar.
3. **Toda cifra con procedencia.** Un componente de ergon o un umbral sin cita no entra.
4. **Paridad con holonmed.** Las primitivas de Φ reproducen `holonmed/core/acoplamiento.py`.
   Un cambio en una exige el cambio en la otra en el mismo ciclo, con su prueba.
5. **Los umbrales son configuración** con valor por defecto explícito.
6. **Fuera del repositorio:** las simulaciones sobre ΔΦ y el umbral ε.

## Gates de calidad

Ninguna rama se fusiona sin que las cuatro pasen, en CI y en local:

```bash
ruff check . && ruff format --check . && mypy && pytest -q
```

`mypy` corre en modo estricto: el paquete es pequeño y no tiene excusa.
