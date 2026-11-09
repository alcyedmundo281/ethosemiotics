# Especificación — ethosemiotics 0.1.0

## 1. Dirección de dependencia

```
ethosemiotics            definiciones formales (este repositorio)
   ├── medsemiotics-db   vocabulario de signos y sus fuentes
   └── holonmed          tokens del paciente: Bayes + Φ en la práctica
```

ethosemiotics no importa a ninguno de los dos. Se distribuye como paquete Python con
versión fija; holonmed y medsemiotics-db lo declaran como dependencia.

## 2. Reparto de responsabilidades

| Pregunta | Dueño |
| --- | --- |
| ¿Qué fórmula convierte dos vectores en Φ? | ethosemiotics |
| ¿Qué hallazgo va en qué dimensión y con qué peso ln(LR)? | holonmed |
| ¿Qué signos existen y qué fuente los respalda? | medsemiotics-db |
| ¿Cómo se presenta (P, Φ) al clínico? | holonmed |

## 3. Contenido de la versión 0.1.0

- `acoplamiento`: `coseno`, `phi_categorico`, `anclaje`, `phi`, `banda`. Reproducen
  holonmed v0.5.0, incluidos los casos límite (vector nulo → 0; sin medidos → 0).
- `ergon`: `ComponenteErgon` (rechaza un costo sin fuente), `EstadoSintropico`,
  `ergon_total` (rechaza unidades mezcladas).
- `estetica`: `belleza` y `lectura_estetica`.
- `falso_cumplimiento`: `evaluar_cumplimiento` con umbrales configurables.

## 4. Ciclos de integración

1. **Ciclo 1 (este):** crear el repositorio con el paquete, sus pruebas y CI. Sin tocar
   holonmed.
2. **Ciclo 2:** holonmed declara `ethosemiotics` como dependencia y su
   `MedidorDeAcoplamiento` delega en las primitivas (`_coseno`, la media geométrica de
   `_anclaje`, `_veredicto`, la fórmula de `_categorico`). Criterio de aceptación: toda la
   suite actual de holonmed pasa sin modificar ningún valor esperado.
3. **Ciclo 3:** medsemiotics-db usa `ComponenteErgon` para validar en CI que todo
   componente de costo declarado cite su fuente.

## 5. Decisiones abiertas

- Qué escalas clínicas alimentan el ergon (puntaje vasoactivo-inotrópico, soporte
  ventilatorio, carga alostática) y en qué unidad común, si alguna.
- Cómo se mide la «intención» del falso cumplimiento: declarada por el clínico, inferida
  del contexto, o ambas.
- Cómo se definen S_int y N_int de una hipótesis para calcular B en la práctica clínica.
- Distribución: instalación desde git con etiqueta de versión o publicación en PyPI.
