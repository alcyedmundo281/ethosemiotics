# ethosemiotics

Definiciones formales de la **Filosofía del Empeño** (PoE, *Philosophy of Endeavor*): la
capa normativa de la que dependen [holonmed](https://github.com/alcyedmundo281/holonmed) y
[medsemiotics-db](https://github.com/alcyedmundo281/medsemiotics-db).

| Módulo | Qué define |
| --- | --- |
| `acoplamiento` | Primitivas de Φ: coseno, Φ categórico, anclaje α, bandas |
| `ergon` | Vector de estado ⟨H, N, E⟩ y componentes de costo con procedencia obligatoria |
| `estetica` | B = Φ · (S_int / N_int) y su lectura |
| `falso_cumplimiento` | Intención alta sin anclaje en la evidencia |

Aritmética determinista, sin dependencias de ejecución. Ante un dato que no permite medir,
el paquete lanza `MedidaImposible` en lugar de aproximar.

```bash
pip install -e ".[dev]"
ruff check . && ruff format --check . && mypy && pytest -q
```

La especificación y el plan de integración están en [docs/ESPECIFICACION.md](docs/ESPECIFICACION.md).

Licencia AGPL-3.0-or-later.
