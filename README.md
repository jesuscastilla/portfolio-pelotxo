# DiploTech — Portfolio & CV de Jesús Castilla

Sitio web personal, portfolio profesional y currículum vitae de **Jesús Castilla**, desarrollador de software y fundador de **DiploTech** en Salobreña (Granada).

[![Website](https://img.shields.io/badge/Website-diplotech.es-70B060?style=flat-square&logo=googlechrome&logoColor=white)](https://diplotech.es)
[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub%20Pages-informational?style=flat-square&logo=githubactions&logoColor=white)](https://diplotech.es)
[![Stack](https://img.shields.io/badge/Stack-HTML5%20%7C%20CSS3%20%7C%20JS-orange?style=flat-square)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

---

## 🌐 Enlaces públicos

- **Dominio principal:** [https://diplotech.es](https://diplotech.es)
- **GitHub Pages:** [https://jesuscastilla.github.io/portfolio-pelotxo/](https://jesuscastilla.github.io/portfolio-pelotxo/)
- **Currículum Vitae (Web A4 ES):** [https://diplotech.es/curriculum.html](https://diplotech.es/curriculum.html)
- **Currículum Vitae (Web A4 EN):** [https://diplotech.es/curriculum-en.html](https://diplotech.es/curriculum-en.html)
- **Currículum Vitae (PDF):** [https://diplotech.es/curriculum.pdf](https://diplotech.es/curriculum.pdf)

---

## 🚀 Características

- **Diseño sin dependencias:** Desarrollado íntegramente con HTML5 semántico, CSS3 moderno y Vanilla JavaScript. Sin frameworks pesados, librerías externas innecesarias ni pasos de compilación complejos.
- **Bilingüe (Español / Inglés):** Rutas independientes y selector de idioma (`index.html` / `index-en.html`, `contacto.html` / `contacto-en.html`).
- **Currículum A4 maquetado:** Vista web imprimible (`curriculum.html`) optimizada para impresión real con `@page { size: A4; margin: 0 }` y versión descargable en PDF.
- **Optimización SEO y metadatos:**
  - Marcado estructurado JSON-LD (`Person` y `Organization`).
  - Metadatos completos Open Graph y Twitter Cards.
  - Etiquetas canónicas y directivas `hreflang` para indexación bilingüe.
  - Archivos `sitemap.xml` y `robots.txt` configurados.
- **Páginas legales integradas:** Cumplimiento de transparencia con `aviso-legal.html` y `privacidad.html`.
- **Paleta visual DiploTech:** Identidad sobria y natural basada en papel cálido (`#F7F5EF`), tinta profunda (`#1A231A`) y verde vegetal (`#4E8A3E`, `#70B060`).

---

## 📁 Estructura del proyecto

```text
portfolio-pelotxo/
├── index.html            # Portada principal en español
├── index-en.html         # Portada principal en inglés
├── contacto.html         # Página de contacto (ES)
├── contacto-en.html      # Página de contacto (EN)
├── styles.css            # Hoja de estilos global del portfolio
├── curriculum.html       # Currículum vitae en formato A4 imprimible (ES)
├── curriculum-en.html    # Currículum vitae en formato A4 imprimible (EN)
├── curriculum.css        # Estilos específicos del currículum A4
├── curriculum.pdf        # Documento PDF generado del CV
├── aviso-legal.html      # Información legal y titularidad
├── privacidad.html       # Política de protección de datos
├── proyectos.json        # Datos y descripción de proyectos destacados
├── sitemap.xml           # Mapa del sitio para motores de búsqueda
├── robots.txt            # Reglas de indexación
├── CNAME                 # Dominio personalizado (diplotech.es)
└── assets/               # Logotipos DiploTech, iconos y recursos gráficos
```

---

## 💻 Desarrollo local

Al tratarse de una web estática pura, no requiere instalación de dependencias `npm`:

```bash
# Servir con Python
python -m http.server 8000

# O con cualquier servidor local (Node http-server, Live Server en VS Code, etc.)
# Abrir en el navegador: http://localhost:8000
```

---

## 🚢 Despliegue

El sitio se despliega automáticamente en **GitHub Pages** mediante GitHub Actions con cada push a la rama principal:

1. El workflow publica todos los ficheros estáticos, incluyendo `CNAME`, `sitemap.xml` y `curriculum.pdf`.
2. Las DNS del dominio `diplotech.es` apuntan a los servidores de GitHub Pages con certificado SSL/TLS gestionado de forma automática.

---

## 📬 Contacto

- **Web:** [diplotech.es](https://diplotech.es)
- **LinkedIn:** [linkedin.com/in/jesuscastillalacal](https://www.linkedin.com/in/jesuscastillalacal)
- **GitHub:** [@jesuscastilla](https://github.com/jesuscastilla)
- **Email:** [hola@diplotech.es](mailto:hola@diplotech.es)

---

<p align="center">
  <sub>© 2026 Jesús Castilla · DiploTech</sub>
</p>
