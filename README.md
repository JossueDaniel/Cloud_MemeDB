# Imagga Project AWS
Proyecto utiliza el servicio SaaS de Imagga para anlizar imágenes y describir las etiquetas identificadas, además de usar los servicios S3 , RDS y EC2 de AWS para lamcenar y ejecutar la aplicación.

## Características
- Usa APIs endpoint para analizar imágenes y devolver resultados de mayor confianza.

## Requisitos previos
- python 3.10 o superior
- Django
- docker
- doker-compose

## Configuración y ejecución
### 1. Clonar repositorio
```bash
git clone https://github.com/JossueDaniel/Cloud_MemeDB.git
```

```bash
cd Cloud_MemeDB
```

### 2. Construir y levantar los contenedores
```bash
docker compose up --build
```

### 3. Ingresar a la aplicación
http://localhost:8000/
