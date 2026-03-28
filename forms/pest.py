class PestWindow(tk.Toplevel):
    def _build(self):
        # Search field with Enter key binding
        self._search.bind("<Return>", lambda _: self._diagnose())

        # Clickable listbox of all 6 known pests
        for name in svc.get_all_pest_names():
            self._listbox.insert("end", name)
        self._listbox.bind("<<ListboxSelect>>",
                           self._on_list_select)

    def _diagnose(self):
        result = svc.diagnose(self._search.get())
        if result is None:
            self._txt.insert("end", "No match found.", "error")
            return
        self._txt.insert("end", result["name"] + "\n", "name")
        self._txt.insert("end", "Symptoms:\n",   "label")
        self._txt.insert("end", result["symptoms"] + "\n")
        self._txt.insert("end", "Treatment:\n",  "tlabel")
        self._txt.insert("end", result["treatment"] + "\n")
        self._txt.insert("end", "Prevention:\n", "plabel")
        self._txt.insert("end", result["prevention"])