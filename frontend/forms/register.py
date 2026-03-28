import tkinter as tk
from tkinter import ttk, messagebox
from utils import theme
from models import UserRole
import services.auth_service as auth


class RegisterWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Create Account")
        self.geometry("460x560")
        self.resizable(False, False)
        self.configure(bg=theme.BG)
        self.grab_set()  # modal
        self._build()

    def _build(self):
        hdr = tk.Frame(self, bg=theme.GREEN_DARK, height=70)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        tk.Label(hdr, text="Create Account", font=theme.FONT_HEADING,
                 bg=theme.GREEN_DARK, fg=theme.WHITE).place(x=20, y=20)

        body = tk.Frame(self, bg=theme.BG)
        body.pack(fill="both", expand=True, padx=30, pady=16)

        def field(label):
            tk.Label(body, text=label, font=theme.FONT_BOLD,
                     bg=theme.BG, fg=theme.TEXT).pack(anchor="w", pady=(10, 2))
            e = tk.Entry(body, font=theme.FONT_BODY, bd=1,
                         relief="solid", bg=theme.WHITE)
            e.pack(fill="x", ipady=7)
            return e

        self._name   = field("Full Name *")
        self._phone  = field("Phone Number *")
        self._pw     = field("Password *")
        self._pw.config(show="*")
        self._conf   = field("Confirm Password *")
        self._conf.config(show="*")

        tk.Label(body, text="Role", font=theme.FONT_BOLD,
                 bg=theme.BG, fg=theme.TEXT).pack(anchor="w", pady=(10, 2))
        self._role = ttk.Combobox(body,
            values=[r.value for r in UserRole],
            state="readonly", font=theme.FONT_BODY)
        self._role.set(UserRole.FARMER.value)
        self._role.pack(fill="x")

        tk.Label(body, text="Region", font=theme.FONT_BOLD,
                 bg=theme.BG, fg=theme.TEXT).pack(anchor="w", pady=(10, 2))
        self._region = ttk.Combobox(body,
            values=["Kigali", "Huye", "Musanze", "Rubavu",
                    "Nairobi", "Kampala", "Dar es Salaam"],
            state="readonly", font=theme.FONT_BODY)
        self._region.set("Kigali")
        self._region.pack(fill="x")

        tk.Button(body, text="Register", font=theme.FONT_BOLD,
                  bg=theme.GREEN_DARK, fg=theme.WHITE,
                  activebackground=theme.GREEN_MED, bd=0,
                  cursor="hand2", command=self._submit
                  ).pack(fill="x", pady=(20, 0), ipady=10)

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
            messagebox.showinfo("Success", msg)
            self.destroy()  # close and return to login
        else:
            messagebox.showwarning("Registration Failed", msg)
