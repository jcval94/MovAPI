# Movilidad Social MX · Frontend GitHub Pages

Este paquete contiene un frontend estático listo para GitHub Pages.

## Archivos

- `index.html`: aplicación pública móvil-first para consumir la API de Cloud Run.
- `cors_fastapi_patch.py`: snippet de referencia para habilitar CORS en FastAPI.

## Despliegue en GitHub Pages

1. Crea un repositorio nuevo, por ejemplo `movilidad-social-web`.
2. Sube `index.html` a la raíz del repositorio.
3. Ve a `Settings → Pages`.
4. En `Build and deployment`, selecciona `Deploy from a branch`.
5. Selecciona `main` y carpeta `/root`.
6. Guarda.

GitHub Pages publicará el sitio en una URL parecida a:

```text
https://jcval94.github.io/movilidad-social-web/
```

## CORS

El frontend ya llama la API con:

```js
mode: "cors",
credentials: "omit",
headers: { "Content-Type": "application/json" }
```

Pero CORS se habilita en el backend, no en el HTML. Si desde navegador falla y desde curl funciona, aplica el patch de `cors_fastapi_patch.py`, reconstruye la imagen y redespliega Cloud Run.

Para producción, cambia `MSMX_CORS_ORIGINS` por tu URL real de GitHub Pages en lugar de `*`.
