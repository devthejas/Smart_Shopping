from flask import Flask, render_template, request, jsonify
import pandas as pd
from optimizer.optimizer_pulp import optimize_shopping
from optimizer.fetch_prices import fetch_prices

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_prices', methods=['POST'])
def get_prices():
    items_raw = request.form.get('items', '')
    budget_raw = request.form.get('budget', '')
    allow_partial = request.form.get('allow_partial', 'false').lower() in ('true', '1', 'on')

    items = [i.strip() for i in items_raw.split(',') if i.strip()]
    budget = float(budget_raw) if budget_raw else None

    if not items:
        return jsonify({"error": "No items provided"}), 400

    # --- Fetch live or mock prices ---
    try:
        fetched = fetch_prices(items)  # from APIs
        data = pd.DataFrame(fetched)
    except Exception as e:
        print("⚠️ Falling back to sample_data.csv due to API error:", e)
        try:
            data = pd.read_csv('data/sample_data.csv')
        except Exception as e2:
            return jsonify({"error": f"Failed to fetch data and fallback file missing: {str(e2)}"}), 500

    # --- Run optimization ---
    try:
        result = optimize_shopping(items, data, budget=budget, allow_partial=allow_partial)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Optimization failed: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
