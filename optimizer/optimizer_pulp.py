import pandas as pd
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, value
from .fetch_prices import fetch_prices

def optimize_shopping(items, data=None, budget=None, allow_partial=True):
    """
    Optimize shopping cost using PuLP linear programming.
    Chooses the cheapest available store per item given a budget.
    """
    # Fetch live data if not provided
    if data is None:
        fetched = fetch_prices(items)
        data = pd.DataFrame(fetched)

    # --- Ensure required columns exist ---
    expected_cols = {'item', 'store', 'price', 'link'}
    if not expected_cols.issubset(set(data.columns)):
        raise ValueError(f"Data missing required columns: {expected_cols - set(data.columns)}")

    # --- Filter for only requested items ---
    data = data[data['item'].isin(items)].copy()
    if data.empty:
        return {"error": "No matching items found in dataset."}

    # --- Define optimization problem ---
    model = LpProblem("SmartShopping", LpMinimize)
    choices = {}

    # Create decision variables
    for _, row in data.iterrows():
        var_name = f"x_{row['item']}_{row['store']}"
        choices[(row['item'], row['store'])] = LpVariable(var_name, 0, 1, LpBinary)

    # --- Objective: minimize total cost ---
    model += lpSum(row['price'] * choices[(row['item'], row['store'])] for _, row in data.iterrows())

    # --- Constraint: pick one store per item (<= 1 for partial) ---
    for item in items:
        item_stores = [choices[(item, s)] for s in data[data['item'] == item]['store']]
        if not item_stores:
            continue
        if allow_partial:
            model += lpSum(item_stores) <= 1
        else:
            model += lpSum(item_stores) == 1

    # --- Optional: Budget constraint ---
    if budget:
        model += lpSum(row['price'] * choices[(row['item'], row['store'])] for _, row in data.iterrows()) <= budget

    # --- Solve optimization ---
    model.solve()

    # --- Collect selected results ---
    selected = []
    for _, row in data.iterrows():
        if value(choices[(row['item'], row['store'])]) == 1:
            selected.append({
                "item": row['item'],
                "store": row['store'],
                "price": row['price'],
                "link": row['link']
            })

    total_cost = sum(item['price'] for item in selected)
    return {"chosen": selected, "total_cost": total_cost}
