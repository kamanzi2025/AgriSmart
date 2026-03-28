class DashboardWindow(tk.Tk):
    def _build(self):
        # Season alert banner
        month = datetime.now().month
        alert_txt = ("Season A active" if month <= 6
                     else "Season B active")

        tiles = [
            ("🌾", "PLANTING", theme.GREEN_DARK,  self._open_planting),
            ("🐛", "PESTS",    theme.RED_DARK,    self._open_pest),
            ("🌍", "SOIL",     theme.ORANGE_DARK, self._open_soil),
            ("💰", "FINANCE",  theme.BLUE_DARK,   self._open_finance),
        ]
        for i, (emoji, title, color, cmd) in enumerate(tiles):
            r, c = divmod(i, 2)
            frame = tk.Frame(grid, bg=color, width=220, height=150)
            frame.grid(row=r, column=c, padx=10, pady=10)
            for w in (frame,) + frame.winfo_children():
                w.bind("<Button-1>", lambda e, fn=cmd: fn())