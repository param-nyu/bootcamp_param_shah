import streamlit as st
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10
from bokeh.models.widgets import Select
from bokeh.layouts import column

# === Load Data ===
data = pd.DataFrame({
    "scenario": ["baseline", "alt_impute", "alt_outlier"],
    "return": [0.12, 0.11, 0.135],
    "volatility": [0.18, 0.185, 0.19],
    "sharpe": [0.56, 0.49, 0.61],
    "assumption": ["imputation", "imputation", "outlier_rule"],
    "value": ["median", "mean", "3sigma"],
    "Category": ["Z", "Y", "X"],
    "MetricA": [58.80, 67.47, 72.47],
    "MetricB": [146.75, 195.34, 170.50],
    "Date": pd.to_datetime(["2025-02-01", "2025-02-02", "2025-02-03"])
})

source = ColumnDataSource(data)

# === Executive Summary ===
st.title("Scenario Analysis Dashboard")
st.subheader("Executive Summary")
st.write("""
- Baseline delivers a balanced profile (Sharpe ~0.56).  
- Alt-impute lowers risk-adjusted return (Sharpe ~0.49).  
- Alt-outlier shows strongest Sharpe (0.61) but with higher volatility.  
""")

# === Visualizations ===
st.subheader("Visualizations")

# --- Bar chart: Return by Scenario ---
p1 = figure(x_range=data["scenario"], height=350, title="Return by Scenario",
            toolbar_location=None, tools="")
p1.vbar(x='scenario', top='return', width=0.6, source=source,
        fill_color=factor_cmap('scenario', palette=Category10[3], factors=data["scenario"]))
p1.yaxis.axis_label = "Return"
st.bokeh_chart(p1, use_container_width=True)

# --- Scatter: Risk-Return Tradeoff ---
p2 = figure(height=350, title="Risk-Return Tradeoff",
            x_axis_label='Volatility', y_axis_label='Return', tools="pan,wheel_zoom,box_zoom,reset,hover")
p2.circle(x=data['volatility'], y=data['return'],
          size=[s*30 for s in data['sharpe']],
          color=Category10[3], fill_alpha=0.6)

hover = p2.select_one(HoverTool)
hover.tooltips = [
    ("Scenario", "@scenario"),
    ("Return", "@return"),
    ("Volatility", "@volatility"),
    ("Sharpe", "@sharpe")
]
st.bokeh_chart(p2, use_container_width=True)

# --- Line chart: MetricB over time ---
p3 = figure(x_axis_type='datetime', height=350, title="MetricB over Time",
            x_axis_label='Date', y_axis_label='MetricB')
for scenario in data["scenario"]:
    subset = data[data["scenario"] == scenario]
    p3.line(subset['Date'], subset['MetricB'],
            line_width=2, legend_label=scenario)
    p3.circle(subset['Date'], subset['MetricB'], size=8)
st.bokeh_chart(p3, use_container_width=True)

# === Assumptions & Risks ===
st.subheader("Assumptions & Risks")
st.write("""
- **Baseline** assumes median imputation of missing data.  
- **Alt-impute** assumes mean imputation, which can distort if outliers exist.  
- **Alt-outlier** removes >3σ outliers, improving Sharpe but risking data loss.  

*Risks*: Overfitting scenario choice to historical noise, limited sample size, and assumption-driven bias.
""")

# === Sensitivity Analysis ===
st.subheader("Sensitivity Analysis")
selected = st.selectbox("Choose scenario to stress-test",
                        data["scenario"].unique())

base_row = data[data["scenario"] == "baseline"].iloc[0]
sel_row = data[data["scenario"] == selected].iloc[0]

st.write(f"Comparing **Baseline** vs **{selected}**:")
st.write(f"- Return: {base_row['return']:.3f} → {sel_row['return']:.3f}")
st.write(
    f"- Volatility: {base_row['volatility']:.3f} → {sel_row['volatility']:.3f}")
st.write(f"- Sharpe: {base_row['sharpe']:.3f} → {sel_row['sharpe']:.3f}")

# === Decision Implications ===
st.subheader("Decision Implications")
st.write("""
- If you prefer **stability**, baseline is safest.  
- If you want **higher Sharpe**, outlier-adjusted scenario looks best.  
- Mean imputation underperforms and may be less reliable.  

➡️ **Recommendation**: Consider using outlier-adjusted data but validate robustness with larger samples.
""")
