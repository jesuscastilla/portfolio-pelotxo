# -*- coding: utf-8 -*-
"""Genera la sección de proyectos de index.html e index-en.html a partir de
proyectos.json y de la API pública de GitHub (descripción, estrellas, etc.)."""
import json
import os
import re
import sys
import urllib.request

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN = os.environ.get("GITHUB_TOKEN", "")

INICIO = "        <!-- PROYECTOS:INICIO -->"
FIN = "        <!-- PROYECTOS:FIN -->"


def api_repo(user, repo):
    url = f"https://api.github.com/repos/{user}/{repo}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "diplotech-generador",
        "Accept": "application/vnd.github+json",
    })
    if TOKEN:
        req.add_header("Authorization", "Bearer " + TOKEN)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as e:
        print(f"  ! API {repo}: {e}")
        return {}


def render(p, num, lang, data):
    tag = p.get("tag_" + lang) or ""
    titulo = p.get("titulo_" + lang) or p.get("repo") or ""
    desc = p.get("desc_" + lang)
    if not desc and data:
        desc = data.get("description") or ""
    stars = (data or {}).get("stargazers_count", 0)
    enlaces = []
    vivo = p.get("en_vivo")
    if vivo:
        label = "En vivo ↗" if lang == "es" else "Live ↗"
        enlaces.append(f'<a class="flecha" href="{vivo}" target="_blank" rel="noopener">{label}</a>')
    if p.get("repo"):
        gh = f'https://github.com/{USER}/{p["repo"]}'
        label = "GitHub" + (f" ★ {stars}" if stars else "") + " ↗"
        enlaces.append(f'<a class="flecha" href="{gh}" target="_blank" rel="noopener">{label}</a>')
    ehtml = f'            <div class="proyecto__enlaces">{"".join(enlaces)}</div>\n' if enlaces else ""
    return (
        f'          <article class="proyecto aparecer">\n'
        f'            <div class="proyecto__top"><span class="proyecto__tag">{tag}</span><span class="proyecto__num">{num:02d}</span></div>\n'
        f'            <h3 class="proyecto__titulo">{titulo}</h3>\n'
        f'            <p class="proyecto__texto">{desc}</p>\n'
        f'{ehtml}'
        f'          </article>'
    )


def build(lang):
    arts = []
    for i, p in enumerate(PROYECTOS, 1):
        data = api_repo(USER, p["repo"]) if p.get("repo") else {}
        arts.append(render(p, i, lang, data))
    return INICIO + "\n" + "\n".join(arts) + "\n" + FIN


def main():
    global USER, PROYECTOS
    with open(os.path.join(BASE, "proyectos.json"), "r", encoding="utf-8") as f:
        cfg = json.load(f)
    USER = cfg["github_user"]
    PROYECTOS = cfg["proyectos"]

    check = "--check" in sys.argv
    cambia = False
    for lang, archivo in (("es", "index.html"), ("en", "index-en.html")):
        p = os.path.join(BASE, archivo)
        with open(p, "r", encoding="utf-8") as f:
            s = f.read()
        m = re.search(re.escape(INICIO) + r".*?" + re.escape(FIN), s, re.S)
        if not m:
            print("!! Marcadores no encontrados en", archivo)
            sys.exit(2)
        nuevo = build(lang)
        if m.group(0) == nuevo:
            print(archivo, "sin cambios")
            continue
        cambia = True
        if check:
            print(archivo, "requiere actualización")
            continue
        s = s[:m.start()] + nuevo + s[m.end():]
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(s)
        print(archivo, "regenerado")
    if check and cambia:
        sys.exit(1)
    print("FIN")


if __name__ == "__main__":
    main()
