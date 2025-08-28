# app.py inside Jupyter (Flask test)
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# ---- your results ----
weights = {
    "TXN": 0.1760,
    "LRCX": 0.1494,
    "AVGO": 0.1421,
    "QCOM": 0.1187,
    "INTC": 0.1159,
    "NVDA": 0.1064,
    "TSM": 0.0777,
    "MRVL": 0.0709,
    "MU": 0.0643,
    "AMD": 0.0375,
}

summary = {
    "Executive Summary": "Smart ETF using LASSO, R²=0.92, residual ARIMA(1,0,1) with mild mean reversion.",
    "Risks": [
        "Concentration risk",
        "Survivorship bias",
        "No costs/slippage/taxes",
        "Residual heteroskedasticity"
    ],
    "Next Steps": [
        "Compute tracking error metrics",
        "Walk-forward retraining",
        "Robust diagnostics and stress tests"
    ]
}

# ---- routes ----


@app.route("/")
def home():
    # super simple HTML view
    html = """
    <h1>Smart ETF Tracker (SOXX)</h1>
    <h2>Executive Summary</h2>
    <p>{{ summary["Executive Summary"] }}</p>
    
    <h2>Final Weights</h2>
    <table border="1" cellpadding="5">
    <tr><th>Ticker</th><th>Weight</th></tr>
    {% for t, w in weights.items() %}
        <tr><td>{{ t }}</td><td>{{ "%.4f"|format(w) }}</td></tr>
    {% endfor %}
    </table>

    <h2>Risks</h2>
    <ul>
    {% for r in summary["Risks"] %}
        <li>{{ r }}</li>
    {% endfor %}
    </ul>

    <h2>Next Steps</h2>
    <ul>
    {% for n in summary["Next Steps"] %}
        <li>{{ n }}</li>
    {% endfor %}
    </ul>
    """
    return render_template_string(html, weights=weights, summary=summary)


@app.route("/api/weights")
def api_weights():
    return jsonify(weights)


@app.route("/api/summary")
def api_summary():
    return jsonify(summary)


# only run if not in Jupyter
if __name__ == "__main__":
    app.run(debug=True, port=5000)
