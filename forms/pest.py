import tkinter as tk
from utils import theme
import services.pest_service as svc


class PestWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pest Diagnosis")
        self.geometry("560x520")
        self.resizable(False, False)
        self.configure(bg=theme.BG)
        self.grab_set()
        self._build()

    def _build(self):
        hdr = tk.Frame(self, bg=theme.RED_DARK, height=70)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        tk.Label(hdr, text="🐛  Pest Diagnosis",
                 font=theme.FONT_HEADING, bg=theme.RED_DARK,
                 fg=theme.WHITE).place(x=16, y=18)

        body = tk.Frame(self, bg=theme.BG)
        body.pack(fill="both", expand=True, padx=20, pady=16)

        # Search row
        search_row = tk.Frame(body, bg=theme.BG)
        search_row.pack(fill="x")
        tk.Label(search_row, text="Search:", font=theme.FONT_BOLD,
                 bg=theme.BG, fg=theme.TEXT).pack(side="left", padx=(0, 8))
        self._search = tk.Entry(search_row, font=theme.FONT_BODY,
                                bd=1, relief="solid", bg=theme.WHITE)
        self._search.pack(side="left", fill="x", expand=True, ipady=6)
        self._search.bind("<Return>", lambda _: self._diagnose())
        tk.Button(search_row, text="Diagnose", font=theme.FONT_BOLD,
                  bg=theme.RED_DARK, fg=theme.WHITE, bd=0,
                  cursor="hand2", command=self._diagnose
                  ).pack(side="left", padx=(8, 0), ipady=4)

        # Listbox of known pests
        list_frame = tk.Frame(body, bg=theme.BG)
        list_frame.pack(fill="x", pady=(12, 0))
        tk.Label(list_frame, text="Known pests (click to select):",
                 font=theme.FONT_SMALL, bg=theme.BG,
                 fg=theme.TEXT_LIGHT).pack(anchor="w")
        self._listbox = tk.Listbox(list_frame, font=theme.FONT_SMALL,
                                   height=4, bd=1, relief="solid",
                                   selectbackground=theme.RED_DARK,
                                   selectforeground=theme.WHITE)
        self._listbox.pack(fill="x")
        for name in svc.get_all_pest_names():
            self._listbox.insert("end", name)
        self._listbox.bind("<<ListboxSelect>>", self._on_list_select)

        # Result area
        tk.Label(body, text="Diagnosis Result:",
                 font=theme.FONT_BOLD, bg=theme.BG,
                 fg=theme.TEXT).pack(anchor="w", pady=(14, 4))
        self._txt = tk.Text(body, font=theme.FONT_MONO, wrap="word",
                            bd=1, relief="solid", bg=theme.WHITE,
                            state="disabled", padx=10, pady=10)
        self._txt.pack(fill="both", expand=True)
        self._txt.tag_config("name",   font=theme.FONT_BOLD,
                             foreground=theme.RED_DARK)
        self._txt.tag_config("label",  font=theme.FONT_BOLD,
                             foreground=theme.ORANGE_DARK)
        self._txt.tag_config("tlabel", font=theme.FONT_BOLD,
                             foreground=theme.BLUE_DARK)
        self._txt.tag_config("plabel", font=theme.FONT_BOLD,
                             foreground=theme.GREEN_DARK)
        self._txt.tag_config("error",  foreground=theme.RED_DARK)

    def _on_list_select(self, _):
        sel = self._listbox.curselection()
        if not sel:
            return
        name = self._listbox.get(sel[0])
        # Use first word as search keyword
        self._search.delete(0, "end")
        self._search.insert(0, name.split("(")[0].strip())
        self._diagnose()

    def _diagnose(self):
        self._txt.configure(state="normal")
        self._txt.delete("1.0", "end")

        result = svc.diagnose(self._search.get())
        if result is None:
            self._txt.insert("end", "No match found.\n", "error")
            self._txt.configure(state="disabled")
            return

        self._txt.insert("end", result["name"] + "\n\n", "name")
        self._txt.insert("end", "Symptoms:\n",   "label")
        self._txt.insert("end", result["symptoms"] + "\n\n")
        self._txt.insert("end", "Treatment:\n",  "tlabel")
        self._txt.insert("end", result["treatment"] + "\n\n")
        self._txt.insert("end", "Prevention:\n", "plabel")
        self._txt.insert("end", result["prevention"])
        self._txt.configure(state="disabled")
