import tkinter as tk
from datetime import datetime
from utils import theme
import utils.session as session


class DashboardWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AgriSmart — Dashboard")
        self.geometry("500x480")
        self.resizable(False, False)
        self.configure(bg=theme.BG)
        self._build()

    def _build(self):
        # Header
        hdr = tk.Frame(self, bg=theme.GREEN_DARK, height=80)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        name = session.current_user.full_name if session.current_user else "Farmer"
        tk.Label(hdr, text=f"Welcome, {name}",
                 font=theme.FONT_HEADING, bg=theme.GREEN_DARK,
                 fg=theme.WHITE).place(x=20, y=14)
        tk.Button(hdr, text="Logout", font=theme.FONT_SMALL,
                  bg=theme.GREEN_MED, fg=theme.WHITE, bd=0,
                  cursor="hand2", command=self._logout
                  ).place(relx=1.0, x=-20, y=24, anchor="ne")

        # Season alert banner
        month = datetime.now().month
        alert_txt = "Season A active (Long Rains)" if month <= 6 \
                    else "Season B active (Short Rains)"
        tk.Label(self, text=f"  {alert_txt}",
                 font=theme.FONT_SMALL, bg=theme.AMBER,
                 fg=theme.TEXT, anchor="w").pack(fill="x")

        # Tile grid
        grid = tk.Frame(self, bg=theme.BG)
        grid.pack(expand=True, pady=20)

        tiles = [
            ("🌾", "PLANTING\nAdvisory",  theme.GREEN_DARK,  self._open_planting),
            ("🐛", "PESTS\nDiagnosis",    theme.RED_DARK,    self._open_pest),
            ("🌍", "SOIL\nManagement",    theme.ORANGE_DARK, self._open_soil),
            ("💰", "FINANCE\nTracker",    theme.BLUE_DARK,   self._open_finance),
        ]
        for i, (emoji, title, color, cmd) in enumerate(tiles):
            r, c = divmod(i, 2)
            frame = tk.Frame(grid, bg=color, width=220, height=150,
                             cursor="hand2")
            frame.grid(row=r, column=c, padx=10, pady=10)
            frame.grid_propagate(False)
            tk.Label(frame, text=emoji, font=("Helvetica Neue", 36),
                     bg=color, fg=theme.WHITE).place(relx=0.5, y=30, anchor="n")
            tk.Label(frame, text=title, font=theme.FONT_BOLD,
                     bg=color, fg=theme.WHITE, justify="center"
                     ).place(relx=0.5, y=95, anchor="n")
            # Bind click on frame and all child labels
            for w in [frame] + list(frame.winfo_children()):
                w.bind("<Button-1>", lambda e, fn=cmd: fn())

    def _open_planting(self):
        from forms.planting import PlantingWindow
        PlantingWindow(self)

    def _open_pest(self):
        from forms.pest import PestWindow
        PestWindow(self)

    def _open_soil(self):
        from forms.soil import SoilWindow
        SoilWindow(self)

    def _open_finance(self):
        from forms.finance import FinanceWindow
        FinanceWindow(self)

    def _logout(self):
        session.clear()
        self.destroy()
        from forms.login import LoginWindow
        LoginWindow().mainloop()
