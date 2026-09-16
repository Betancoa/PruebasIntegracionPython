
# Introducción a Pruebas de Integración (Python) — 4 partes

Este repositorio contiene un ejercicio práctico en **Python** para evidenciar 4 tipos de integración:

1) **Por capas** (Controller → Service → Repository in-memory)  
2) **Modular** (un módulo usa a otro)  
3) **Con API externa** (cliente HTTP real contra servidor simulado)  
4) **Con base de datos** (SQLite en memoria)

En las cuatro actividades estamos haciendo pruebas de integración. Lo único que cambia es quién se está comunicando con quién.

## Requisitos
- Python 3.11+
- `pip install -r requirements.txt`

## Ejecutar
```bash
pytest -q
```
O por parte:
```bash
pytest -q tests/test_part1_layers.py
pytest -q tests/test_part2_modules.py
pytest -q tests/test_part3_external_api.py
pytest -q tests/test_part4_database.py
```

## Estructura
```
src/
  layers/ (modelo, repositorio in-memory, servicio, controlador)
  modules/ (discount, order)
  external/ (cliente http)
  db/ (repositorio sqlite)
```

## Pregunta
- Explique qué componentes se están integrando en este código y justifique por qué este es un caso de prueba de integración y no una prueba unitaria.
- Proponga una aserción adicional que fortalezca la prueba de cada tipo de integración.
- Proponer un fallo posible.

