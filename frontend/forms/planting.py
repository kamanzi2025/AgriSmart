import tkinter as tk
from tkinter import ttk
from utils import theme
import services.planting_service as svc


REGIONS = ["Kigali", "Huye", "Musanze", "Rubavu",
           "Nairobi", "Kampala", "Dar es Salaam"]


class PlantingWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Planting Advisory")
        self.geometry("520x460")
        self.resizable(False, False)
        self.configure(bg=theme.BG)
        self.grab_set()
        self._build()

    def _build(self):
        hdr = tk.Frame(self, bg=theme.GREEN_DARK, height=70)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        tk.Label(hdr, text="🌾  Planting Advisory",
                 font=theme.FONT_HEADING, bg=theme.GREEN_DARK,
                 fg=theme.WHITE).place(x=16, y=18)

        body = tk.Frame(self, bg=theme.BG)
        body.pack(fill="both", expand=True, padx=20, pady=16)

        row = tk.Frame(body, bg=theme.BG)
        row.pack(fill="x")
        tk.Label(row, text="Select Region:", font=theme.FONT_BOLD,
                 bg=theme.BG, fg=theme.TEXT).pack(side="left", padx=(0, 10))
        self._region = ttk.Combobox(row, values=REGIONS,
                                    state="readonly", font=theme.FONT_BODY,
                                    width=20)
        self._region.set("Kigali")
        self._region.pack(side="left")
        tk.Button(row, text="Generate", font=theme.FONT_BOLD,
                  bg=theme.GREEN_DARK, fg=theme.WHITE, bd=0,
                  cursor="hand2", command=self._generate
                  ).pack(side="left", padx=(12, 0), ipady=4)

        self._txt = tk.Text(body, font=theme.FONT_MONO, wrap="word",
                            bd=1, relief="solid", bg=theme.WHITE,
                            state="disabled", padx=10, pady=10)
        self._txt.pack(fill="both", expand=True, pady=(14, 0))
        self._txt.tag_config("heading", font=theme.FONT_BOLD,
                             foreground=theme.GREEN_DARK)
        self._txt.tag_config("subhead", font=theme.FONT_BOLD,
                             foreground=theme.ORANGE_DARK)

        # Generate immediately for the default region
        self._generate()

    def _generate(self):
        region = self._region.get()
        data = svc.generate(region)

        self._txt.configure(state="normal")
        self._txt.delete("1.0", "end")

        self._txt.insert("end", "Region:          ", "heading")
        self._txt.insert("end", data["region"] + "\n")
        self._txt.insert("end", "Variety:         ", "heading")
        self._txt.insert("end", data["recommended_variety"] + "\n")
        self._txt.insert("end", "Season:          ", "heading")
        self._txt.insert("end", data["season"] + "\n")
        self._txt.insert("end", "Planting Window: ", "subhead")
        self._txt.insert("end", data["planting_window"] + "\n")

        self._txt.configure(state="disabled")
