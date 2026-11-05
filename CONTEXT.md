# Contexto del Proyecto - Portfolio de Jesús Castilla

Este archivo contiene el contexto técnico necesario para retomar, modificar o ampliar el trabajo en el portfolio de Jesús Castilla sin pérdida de información.

---

## Propósito del Proyecto

El objetivo de este proyecto es servir como un portfolio / currículum vitae web formal para Jesús Castilla, documentando su perfil como **Desarrollador de Software**. 

**Premisa (2026-10-11):** el portfolio se reposiciona como **CV profesional** orientado a LinkedIn. Tono formal y enfoque en productos reales en producción. La marca personal es **DiploTech**.

---

## Arquitectura y Tecnologías

- **Tipo de proyecto:** Web estática clásica (HTML5, CSS3, Vanilla JS). Sin frameworks, sin npm, sin build step.
- **Enfoque técnico:** Máxima simplicidad, compatibilidad y facilidad de despliegue (GitHub Pages + NAS Synology).
- **Identidad (2026-10-11):** rediseño profesional como CV para LinkedIn, con branding **DiploTech**. Paleta: papel cálido (`#F7F5EF`), tinta verde‑negro (`#1A231A`) y verde de marca (`#5F9A4B`). Tipografías **Fraunces** (títulos) y **Manrope** (cuerpo). Logo en `assets/` (transparente + versión blanca).

---

## Estructura de Archivos

```text
portfolio-pelotxo/
├── index.html        # Inicio (ES): héroe, sobre mí, stack, proyectos, CTA de contacto
├── index-en.html     # Inicio (EN)
├── contacto.html     # Contacto (ES): enlaces + formulario
├── contacto-en.html  # Contacto (EN)
├── styles.css        # Hoja de estilos global (rediseño 2026)
├── curriculum.html   # Currículum A4 imprimible (ES) — añadido 2026-10-26
├── curriculum.css    # Estilos del currículum A4 (paleta y tipografías del sitio)
├── curriculum.pdf    # Exportación PDF A4 (generada con Chrome headless)
├── assets/           # Logo DiploTech, favicon y apple-touch-icon
└── CONTEXT.md        # Documentación técnica (este archivo)
```

---

## Detalles del Contenido

### 1. `index.html` (Proyectos)
La página se divide semánticamente por **Lenguajes y Tecnologías**, basándose en el historial real del desarrollador:
- **Kotlin & Android Development:** App Barrioteca v2, Calendario Lebeche.
- **TypeScript, React & Frontend Web:** Frontend Web/PWA de Barrioteca, Lebeche Web Oficial.
- **Swift & iOS:** App wrapper nativo de iOS para Barrioteca.
- **PHP & Bases de Datos:** Backend SLiMS de Barrioteca.
- **Sistemas, Shell Scripting y Linux:** Creación del sistema operativo DiplodocOS, configuración de Nginx en Synology.

### 2. `contacto.html` (Contacto y Enlaces)
Se incluyen enlaces y vías de contacto directos:
- **LinkedIn:** [https://www.linkedin.com/in/jesuscastillalacal](https://www.linkedin.com/in/jesuscastillalacal)
- **GitHub:** [https://github.com/jesuscastilla](https://github.com/jesuscastilla)
- **WhatsApp (DiploTech):** `+34687407347` (Enlace directo vía `wa.me`)
- Un **formulario de contacto** maquetado (actualmente sin backend configurado, usa `action="#"`).

---

## Despliegue en el NAS (Instrucciones)

Este proyecto está diseñado para alojarse en el NAS Synology de Jesús (`pelotxo.synology.me`), utilizando **Web Station** (Nginx/Apache). El dominio dedicado es `corrientelebeche.es` (ver `LEBECHE/docs/GUIA_DOMINIO_CORRIENTELEBECHE.md`).

### Pasos de despliegue local manual (Red interna)
1. Acceder al NAS a través de la red local mediante SMB: `\\192.168.50.94\web\` (o la ruta correspondiente al volumen web).
2. Crear la carpeta `/Portfolio/` (o copiar la carpeta `portfolio-pelotxo` entera) dentro de la carpeta compartida web.
3. Copiar el contenido (`index.html`, `contacto.html`, `styles.css`) en dicha carpeta.
4. El servidor Web Station servirá directamente el contenido HTML a través de la IP local o del dominio en el subdirectorio correspondiente (p.ej. `https://www.corrientelebeche.es/portfolio/`).

---

## Directrices para futuros cambios

1. **Mantener la formalidad:** El tono del texto debe ser siempre profesional, directo y formal.
2. **Tono profesional:** el texto debe reflejar un perfil profesional de desarrollador (sin el antiguo descargo de «hobby no comercial»), manteniendo la autenticidad.

---

## [26-10-2026] — Currículum A4 imprimible (ES)

- **Tipo:** Vista
- **Cambio:** añadida una vista de currículum vitae en A4 real (210×297 mm) compuesta por `curriculum.html` + `curriculum.css`, con `@page { size: A4; margin: 0 }`, paleta del sitio (`#F7F5EF`, `#1A231A`, `#70B060`, `#4E8A3E`, `#1F3320`, `#EAF3E3`), tipografías Fraunces/Manrope y logo DiploTech (`assets/logo-blanco.png`). Dos páginas: (1) perfil, experiencia técnica DiploTech 2026–Actualidad y stack; (2) voluntariado (Cibervoluntarios, San Juan de Dios, ACOGr, Federación Arco Iris, Amnistía Internacional, Greenpeace), formación autodidacta y otros proyectos. Incluye un código QR (`assets/qr-web.png`, 256×256, enlace al portfolio) en la cabecera de la página 1.
- **Impacto:** solo los archivos nuevos `curriculum.{html,css,pdf}`; no modifica `index.html`, `styles.css` ni las páginas existentes.
- **Datos del titular (verificados con el interesado):** teléfono `+34 644 707 327` (prevalece sobre el `+34687407347` que consta en la sección de contacto de este documento) e inglés nivel C1.


---

## [30-10-2026] — Dominio propio diplotech.es (migración GitHub Pages)

- **Tipo:** Configuración
- **Cambio:** dominio `diplotech.es` (registrado en Piensa Solutions) preparado para servir el portfolio desde GitHub Pages. Añadidos `CNAME`, `robots.txt`, `sitemap.xml` (5 URLs) y `404.html` con identidad DiploTech. SEO completo en las 5 páginas (canonical, Open Graph, Twitter Cards, hreflang ES/EN y JSON-LD Person/Organization en inicio ES/EN). El workflow `pages.yml` ahora publica además `curriculum.{html,css,pdf}`, `CNAME`, `404.html`, `robots.txt` y `sitemap.xml`. QR del currículum y enlaces actualizados a `https://diplotech.es/`; `curriculum.pdf` regenerado (2 páginas A4, 515 KB).
- **Impacto:** todo el sitio. **Aplicado (05-11-2026):** DNS en Piensa Solutions (4 registros A de GitHub Pages + CNAME `www`), dominio personalizado activado en GitHub Pages, HTTPS con certificado emitido y desplegado el commit `1976d91` (CNAME + SEO + currículum + QR). Pendiente del usuario: marcar **Enforce HTTPS** en GitHub Settings → Pages. El correo (MX `mx.buzondecorreo.com` + SPF) no se ve afectado.
