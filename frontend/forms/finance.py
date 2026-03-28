import tkinter as tk
from tkinter import ttk, messagebox
from utils import theme
from models import TransactionType
import utils.session as session
import services.financial_service as svc


SEASONS  = ["2025A", "2025B", "2026A", "2026B"]
CATEGORIES = ["Seeds", "Fertiliser", "Labour", "Transport",
              "Crop Sales", "Other"]


class FinanceWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Farm Finance Tracker")
        self.geometry("580x560")
        self.resizable(False, False)
        self.configure(bg=theme.BG)
        self.grab_set()
        self._build()

    def _build(self):
        hdr = tk.Frame(self, bg=theme.BLUE_DARK, height=70)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        tk.Label(hdr, text="💰  Farm Finance Tracker",
                 font=theme.FONT_HEADING, bg=theme.BLUE_DARK,
                 fg=theme.WHITE).place(x=16, y=18)

        body = tk.Frame(self, bg=theme.BG)
        body.pack(fill="both", expand=True, padx=20, pady=14)

        # ── Entry form ──────────────────────────────────────────────
        form = tk.LabelFrame(body, text=" New Transaction ",
                             font=theme.FONT_SMALL, bg=theme.BG,
                             fg=theme.TEXT, bd=1, relief="solid")
        form.pack(fill="x")

        def lbl(parent, text, col, row):
            tk.Label(parent, text=text, font=theme.FONT_BOLD,
                     bg=theme.BG, fg=theme.TEXT
                     ).grid(row=row, column=col, sticky="w",
                            padx=(8, 4), pady=4)

        lbl(form, "Season",      0, 0)
        self._season = ttk.Combobox(form, values=SEASONS,
                                    state="readonly", width=10)
        self._season.set(SEASONS[0])
        self._season.grid(row=0, column=1, padx=4, pady=4, sticky="w")

        lbl(form, "Type", 2, 0)
        self._tx_type = ttk.Combobox(form,
            values=[t.value for t in TransactionType],
            state="readonly", width=10)
        self._tx_type.set(TransactionType.REVENUE.value)
        self._tx_type.grid(row=0, column=3, padx=4, pady=4, sticky="w")

        lbl(form, "Category",    0, 1)
        self._cat = ttk.Combobox(form, values=CATEGORIES,
                                 state="readonly", width=14)
        self._cat.set(CATEGORIES[0])
        self._cat.grid(row=1, column=1, columnspan=3,
                       padx=4, pady=4, sticky="w")

        lbl(form, "Description", 0, 2)
        self._desc = tk.Entry(form, font=theme.FONT_BODY,
                              bd=1, relief="solid", bg=theme.WHITE, width=30)
        self._desc.grid(row=2, column=1, columnspan=3,
                        padx=4, pady=4, sticky="w")

        lbl(form, "Amount (RWF)", 0, 3)
        self._amount = tk.Entry(form, font=theme.FONT_BODY,
                                bd=1, relief="solid", bg=theme.WHITE, width=14)
        self._amount.grid(row=3, column=1, padx=4, pady=4, sticky="w")

        btn_row = tk.Frame(form, bg=theme.BG)
        btn_row.grid(row=4, column=0, columnspan=4, pady=8, padx=8, sticky="w")
        tk.Button(btn_row, text="Add Record", font=theme.FONT_BOLD,
                  bg=theme.BLUE_DARK, fg=theme.WHITE, bd=0,
                  cursor="hand2", command=self._add
                  ).pack(side="left", ipady=5, ipadx=10)
        tk.Button(btn_row, text="P&L Summary", font=theme.FONT_BOLD,
                  bg=theme.GREEN_DARK, fg=theme.WHITE, bd=0,
                  cursor="hand2", command=self._show_summary
                  ).pack(side="left", padx=(10, 0), ipady=5, ipadx=10)

        # ── Records list ────────────────────────────────────────────
        tk.Label(body, text="Records", font=theme.FONT_BOLD,
                 bg=theme.BG, fg=theme.TEXT).pack(anchor="w", pady=(12, 4))
        cols = ("Season", "Type", "Category", "Description", "Amount")
        self._tree = ttk.Treeview(body, columns=cols,
                                  show="headings", height=8)
        for c in cols:
            self._tree.heading(c, text=c)
        self._tree.column("Season",      width=60,  anchor="center")
        self._tree.column("Type",        width=70,  anchor="center")
        self._tree.column("Category",    width=90,  anchor="center")
        self._tree.column("Description", width=180)
        self._tree.column("Amount",      width=90,  anchor="e")
        self._tree.pack(fill="both", expand=True)
        self._refresh()

    def _add(self):
        try:
            amt = float(self._amount.get().replace(",", ""))
        except ValueError:
            messagebox.showwarning("Validation", "Amount must be a number.")
            return
        tx = (TransactionType.REVENUE
              if self._tx_type.get() == "Revenue"
              else TransactionType.COST)
        ok, msg = svc.add_record(
            session.user_id(), self._season.get(),
            tx, self._cat.get(),
            self._desc.get().strip(), amt)
        if ok:
            self._amount.delete(0, "end")
            self._desc.delete(0, "end")
            self._refresh()
        else:
            messagebox.showwarning("Error", msg)

    def _refresh(self):
        for row in self._tree.get_children():
            self._tree.delete(row)
        for r in svc.get_records(session.user_id()):
            self._tree.insert("", "end", values=(
                r.season,
                r.transaction_type.value,
                r.category,
                r.description,
                f"{r.amount:,.0f}",
            ))

    def _show_summary(self):
        s = svc.get_season_summary(
            session.user_id(), self._season.get())
        rev, cost, net = (s["total_revenue"],
                          s["total_cost"],
                          s["net_profit"])
        verdict = ("PROFITABLE" if net >= 0
                   else "LOSS — review your costs")
        messagebox.showinfo("P&L Report",
            f"Season:  {self._season.get()}\n"
            f"Revenue: {rev:,.0f} RWF\n"
            f"Cost:    {cost:,.0f} RWF\n"
            f"Net:     {net:,.0f} RWF\n\n{verdict}")
