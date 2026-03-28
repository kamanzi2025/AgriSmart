class FinanceWindow(tk.Toplevel):
    def _add(self):
        amt = float(self._amount.get().replace(",", ""))
        tx  = (TransactionType.REVENUE
               if self._tx_type.get() == "Revenue"
               else TransactionType.COST)
        ok, msg = svc.add_record(
            session.user_id(), self._season.get(),
            tx, self._cat.get(),
            self._desc.get().strip(), amt)
        if ok: self._refresh()

    def _show_summary(self):
        s = svc.get_season_summary(
            session.user_id(), self._season.get())
        rev, cost, net = (s["total_revenue"],
                          s["total_cost"],
                          s["net_profit"])
        verdict = ("PROFITABLE" if net >= 0
                   else "LOSS — review your costs")
        messagebox.showinfo("P&L Report",
            f"Revenue: {rev:,.0f} RWF\n"
            f"Cost:    {cost:,.0f} RWF\n"
            f"Net:     {net:,.0f} RWF\n\n{verdict}")