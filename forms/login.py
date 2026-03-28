import tkinter as tk
from tkinter import messagebox
from utils import theme
import utils.session as session
import services.auth_service as auth

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AgriSmart Advisor")
        self.geometry("440x540")
        self.resizable(False, False)
        self.configure(bg=theme.BG)
        self._build()

    def _build(self):
        # Green header bar
        hdr = tk.Frame(self, bg=theme.GREEN_DARK, height=120)
        hdr.pack(fill="x")
        tk.Label(hdr, text="AgriSmart Advisor",
                 font=theme.FONT_TITLE, bg=theme.GREEN_DARK,
                 fg=theme.WHITE).place(x=20, y=22)
        # Phone + password fields, login button,
        # register button, demo hint label…
        self.bind("<Return>", lambda _: self._do_login())

    def _do_login(self):
        ok, user, msg = auth.login(
            self._phone.get().strip(), self._pw.get())
        if ok:
            session.set_user(user)
            self.destroy()
            from forms.dashboard import DashboardWindow
            DashboardWindow().mainloop()
        else:
            messagebox.showwarning("Login Failed", msg)