# Backend sistema de gestion de ayudantias

## Requirements

-   Python3.10+
-   Docker
-   MongoDB

## Iniciar proyecto

1. Crear a venv

```bash
python3 -m venv ./venv
```

2. Activar entorno venv

```bash
source ./venv/bin/active || source ./venv/bin/activate
```

3. Instalar dependencias

```bash
pip3 install -r requirements.txt
```

4. Run

```bash
sudo docker compose up app --attach app
```

### Docker

`Dockerfile.dev`
`Dockerfile.prod`

Puerto expuesto (en ambos Dockerfiles): `6060`

## API Reference (Swagger)

#### Swagger ui

```
  GET /api/v1/docs
```

#### Redoc

```
  GET /api/v1/redoc
```
