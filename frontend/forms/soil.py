import tkinter as tk
from tkinter import ttk
from utils import theme


FERTILITY_TEXT = """\
Soil Fertility Guide
====================
• Beans fix atmospheric nitrogen — they can reduce fertilizer costs.
• Apply DAP (18-46-0) at planting: 50 kg/ha placed in the furrow.
• Top-dress with CAN (26% N) at first-flower stage if leaves are pale.
• Organic matter: incorporate compost or farmyard manure (5 t/ha)
  to improve water retention and soil structure.
• Conduct a soil test every 2–3 seasons to avoid over-fertilisation.
"""

ROTATION_TEXT = """\
Crop Rotation Principles
========================
• Never plant beans after beans on the same plot within 2 seasons.
  This breaks pest and disease cycles (e.g. Angular Leaf Spot, Root Rot).

Recommended rotation sequence:
  Season A  →  Beans
  Season B  →  Maize or Sorghum
  Season A  →  Leafy vegetables / root crops
  Season B  →  Beans (return)

• Benefits: reduces soil-borne diseases, improves soil structure,
  lowers input costs over time.
"""

PH_TEXT = """\
Soil pH and Liming
==================
• Optimal pH range for beans: 6.0 – 7.0
• Below pH 5.5: aluminium toxicity stunts roots and reduces yield.

Liming guide:
  pH 5.0–5.4  →  Apply 2.0 t/ha agricultural lime
  pH 5.5–5.9  →  Apply 1.0 t/ha agricultural lime
  pH 6.0+     →  No lime needed

• Incorporate lime 4–6 weeks before planting for best effect.
• Re-test soil pH one season after liming.
• Dolomitic lime (CaMg(CO₃)₂) also supplies magnesium — useful on
  sandy soils that are commonly Mg-deficient.
"""


class SoilWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Soil Management")
        self.geometry("560x480")
        self.resizable(False, False)
        self.configure(bg=theme.BG)
        self.grab_set()
        self._build()

    def _build(self):
        hdr = tk.Frame(self, bg=theme.ORANGE_DARK, height=70)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        tk.Label(hdr, text="🌍  Soil Management",
                 font=theme.FONT_HEADING, bg=theme.ORANGE_DARK,
                 fg=theme.WHITE).place(x=16, y=18)

        body = tk.Frame(self, bg=theme.BG)
        body.pack(fill="both", expand=True, padx=4, pady=8)

        nb = ttk.Notebook(body)
        nb.pack(fill="both", expand=True)

        for title, content in [
            ("Soil Fertility", FERTILITY_TEXT),
            ("Crop Rotation",  ROTATION_TEXT),
            ("pH and Liming",  PH_TEXT),
        ]:
            tab = tk.Frame(nb, bg=theme.WHITE)
            nb.add(tab, text=title)
            txt = tk.Text(tab, font=theme.FONT_MONO,
                          wrap="word", state="normal",
                          padx=12, pady=10, bd=0)
            txt.insert("1.0", content)
            txt.configure(state="disabled")
            txt.pack(fill="both", expand=True)
