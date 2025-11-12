import tkinter as tk
from tkinter import filedialog, messagebox
from rss_reader import obtener_noticias
from podcast_generator import generar_guion, texto_a_audio

class RSSPodcastApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Podcast desde RSS")
        self.feeds = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Introduce URLs de feeds RSS (una por línea):").pack(pady=5)
        self.text_feeds = tk.Text(self.root, height=10, width=60)
        self.text_feeds.pack(padx=10, pady=5)

        tk.Button(self.root, text="Generar Podcast", command=self.generar_podcast).pack(pady=10)

    def generar_podcast(self):
        feed_text = self.text_feeds.get("1.0", tk.END).strip()
        if not feed_text:
            messagebox.showwarning("Sin feeds", "Por favor, introduce al menos un feed RSS.")
            return

        feeds = [line.strip() for line in feed_text.splitlines() if line.strip()]
        noticias = obtener_noticias(feeds)
        if not noticias:
            messagebox.showerror("Sin noticias", "No se pudieron obtener noticias de los feeds.")
            return

        guion = generar_guion(noticias)
        archivo = "output/podcast.mp3"
        texto_a_audio(guion, archivo)
        messagebox.showinfo("Éxito", f"Podcast generado en: {archivo}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RSSPodcastApp(root)
    root.mainloop()