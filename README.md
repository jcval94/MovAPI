# Movilidad Social MX · Frontend GitHub Pages

Este paquete contiene un frontend estático listo para GitHub Pages.

## Archivos

- `index.html`: aplicación pública responsive para consumir la API de Cloud Run, con layout móvil y layout de escritorio diferenciados.
- `cors_fastapi_patch.py`: snippet de referencia para habilitar CORS en FastAPI.

## Despliegue automático en GitHub Pages

El repositorio incluye el workflow `.github/workflows/deploy-pages.yml`, que publica el sitio automáticamente cuando se hace `push` a `main` con cambios en `index.html` o en el propio workflow.

Para activarlo por primera vez:

1. Ve a `Settings → Pages` en GitHub.
2. En `Build and deployment`, selecciona `GitHub Actions` como fuente.
3. Sube los cambios a la rama `main`.
4. GitHub Actions empaquetará `index.html` en un artefacto estático y lo desplegará en Pages.

También puedes ejecutar el workflow manualmente desde `Actions → Deploy GitHub Pages → Run workflow`.

GitHub Pages publicará el sitio en una URL parecida a:

```text
https://TU_USUARIO.github.io/movilidad-social-web/
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
