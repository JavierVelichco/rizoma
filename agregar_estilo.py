from pathlib import Path

# Ruta a tu carpeta con los archivos HTML
carpeta = Path(r"C:\xampp\htdocs\rizoma")

# Archivos HTML a modificar
archivos_html = ["index.html"] + [f"pagina{i}.html" for i in range(1, 21)]

# Línea de estilo con la ruta relativa correcta
linea_estilo = '<link rel="stylesheet" href="css/estilo.css">'

# Agregar el enlace a cada archivo HTML
for nombre in archivos_html:
    ruta = carpeta / nombre
    if ruta.exists():
        contenido = ruta.read_text(encoding="utf-8")
        if linea_estilo not in contenido:
            contenido = contenido.replace("<head>", f"<head>\n  {linea_estilo}")
            ruta.write_text(contenido, encoding="utf-8")
            print(f"✅ Modificado: {nombre}")
        else:
            print(f"ℹ️ Ya estaba incluido: {nombre}")
    else:
        print(f"❌ No encontrado: {nombre}")
