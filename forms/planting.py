class PlantingWindow(tk.Toplevel):
    def _generate(self):
        region = self._region.get()
        data   = svc.generate(region) 

        self._txt.configure(state="normal")
        self._txt.delete("1.0", "end")

        # Insert coloured lines
        self._txt.insert("end", "Region:  ",    "heading")
        self._txt.insert("end", data["region"] + "\n")
        self._txt.insert("end", "Variety:  ",   "heading")
        self._txt.insert("end", data["variety"] + "\n")
        self._txt.insert("end", "Season:  ",    "heading")
        self._txt.insert("end", data["season"] + "\n")
        self._txt.insert("end", "Soil Tips:\n", "subhead")
        self._txt.insert("end", data["soil_tips"])

        self._txt.configure(state="disabled")