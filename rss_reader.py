import feedparser

def obtener_noticias(feed_urls):
    noticias = []
    for url in feed_urls:
        try:
            feed = feedparser.parse(url)
            for entrada in feed.entries[:5]:  # Limitar a 5 noticias por feed
                noticias.append({
                    'titulo': entrada.title,
                    'resumen': entrada.get('summary', 'Sin resumen'),
                    'enlace': entrada.link
                })
        except Exception as e:
            print(f"Error al leer feed {url}: {e}")
    return noticias