class SoilWindow(tk.Toplevel):
    def _build(self):
        nb = ttk.Notebook(body)
        nb.pack(fill="both", expand=True)

        # Three tabs
        for title, content in [
            ("Soil Fertility", FERTILITY_TEXT),
            ("Crop Rotation",  ROTATION_TEXT),
            ("pH and Liming",  PH_TEXT),
        ]:
            tab = tk.Frame(nb, bg=theme.WHITE)
            nb.add(tab, text=title)
            txt = tk.Text(tab, font=("Menlo", 10),
                          wrap="word", state="normal")
            txt.insert("1.0", content)
            txt.configure(state="disabled")
            txt.pack(fill="both", expand=True)