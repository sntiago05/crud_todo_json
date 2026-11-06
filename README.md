# Gestor de notas en JSON

Aplicación de consola en **Python** para crear, listar, buscar, actualizar y eliminar notas. Las notas se guardan en `data/notes.json`.

## Estructura por capas
- `handler/` menú y manejo de opciones
- `service/` lógica de negocio
- `repository/` lectura y escritura del JSON
- `model/` estructura de datos de las notas
- `utils/` lectura segura de valores de entrada

## Cómo ejecutar
```bash
python main.py
```

## Proyecto de aprendizaje
Práctica de arquitectura por capas en Python y persistencia en JSON.
