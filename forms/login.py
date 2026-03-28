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
        hdr.pack_propagate(False)
        tk.Label(hdr, text="AgriSmart Advisor",
                 font=theme.FONT_TITLE, bg=theme.GREEN_DARK,
                 fg=theme.WHITE).place(x=20, y=22)
        tk.Label(hdr, text="Smart farming, better harvests",
                 font=theme.FONT_SMALL, bg=theme.GREEN_DARK,
                 fg=theme.WHITE).place(x=20, y=70)

        body = tk.Frame(self, bg=theme.BG)
        body.pack(fill="both", expand=True, padx=30, pady=20)

        tk.Label(body, text="Phone Number", font=theme.FONT_BOLD,
                 bg=theme.BG, fg=theme.TEXT).pack(anchor="w", pady=(10, 2))
        self._phone = tk.Entry(body, font=theme.FONT_BODY, bd=1,
                               relief="solid", bg=theme.WHITE)
        self._phone.pack(fill="x", ipady=8)

        tk.Label(body, text="Password", font=theme.FONT_BOLD,
                 bg=theme.BG, fg=theme.TEXT).pack(anchor="w", pady=(14, 2))
        self._pw = tk.Entry(body, font=theme.FONT_BODY, bd=1,
                            relief="solid", bg=theme.WHITE, show="*")
        self._pw.pack(fill="x", ipady=8)

        tk.Button(body, text="Login", font=theme.FONT_BOLD,
                  bg=theme.GREEN_DARK, fg=theme.WHITE,
                  activebackground=theme.GREEN_MED, bd=0,
                  cursor="hand2", command=self._do_login
                  ).pack(fill="x", pady=(24, 0), ipady=10)

        tk.Button(body, text="Create Account", font=theme.FONT_BODY,
                  bg=theme.BG, fg=theme.GREEN_DARK,
                  activeforeground=theme.GREEN_MED, bd=0,
                  cursor="hand2", command=self._open_register
                  ).pack(fill="x", pady=(8, 0))

        tk.Label(body,
                 text="Demo — Farmer: +250700000001 / farmer123",
                 font=theme.FONT_SMALL, bg=theme.BG,
                 fg=theme.TEXT_LIGHT).pack(pady=(20, 0))

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

    def _open_register(self):
        from forms.register import RegisterWindow
        RegisterWindow(self)
