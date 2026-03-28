from models import FinancialRecord, TransactionType

_records: list[FinancialRecord] = []
_next_id = 1

def add_record(user_id, season, tx_type,
               category, description, amount):
    """Returns (success: bool, message: str)."""
    global _next_id
    if amount <= 0:
        return False, "Amount must be greater than zero."
    if not description.strip():
        return False, "Description is required."
    _records.append(FinancialRecord(
        record_id=_next_id, user_id=user_id,
        season=season, transaction_type=tx_type,
        category=category, description=description,
        amount=amount))
    _next_id += 1
    return True, "Record saved."

def get_records(user_id):
    return [r for r in _records if r.user_id == user_id]

def get_season_summary(user_id, season):
    """Returns {total_revenue, total_cost, net_profit}."""
    rows = [r for r in _records
            if r.user_id == user_id and r.season == season]
    rev  = sum(r.amount for r in rows
               if r.transaction_type == TransactionType.REVENUE)
    cost = sum(r.amount for r in rows
               if r.transaction_type == TransactionType.COST)
    return {"total_revenue": rev,
            "total_cost":    cost,
            "net_profit":    rev - cost}

def get_seasons(user_id):
    seen = []
    for r in _records:
        if r.user_id == user_id and r.season not in seen:
            seen.append(r.season)
    return sorted(seen)