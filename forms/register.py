class RegisterWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("460x560")
        self.grab_set()  # modal
        self._build()

    def _build(self):
        # Full Name, Phone, Password,
        self._role = ttk.Combobox(body,
            values=[r.value for r in UserRole],
            state="readonly")
        self._role.set(UserRole.FARMER.value)

    def _submit(self):
        if not self._name.get() or not self._phone.get():
            messagebox.showwarning("Validation",
                "Fill all required fields.")
            return
        if self._pw.get() != self._conf.get():
            messagebox.showwarning("Validation",
                "Passwords do not match.")
            return
        ok, msg = auth.register(
            self._name.get(), self._phone.get(),
            self._pw.get(), UserRole(self._role.get()),
            self._region.get())
        if ok:
            self.destroy()  # close and return to login