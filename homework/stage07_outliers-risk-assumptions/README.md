# Reflection

## Methods
- **IQR detection** with k=1.5
- **Z-score detection** with threshold=3.0
- **Winsorizing** at 5th/95th percentiles

## Results
- No change in **mean**, **median**, or **std dev** after filtering
- Winsorizing capped extremes: **min** -0.026→-0.021, **max** 0.021→0.016
- **Regression results identical** across filtering methods

## Risks
- Removing **real market events**
- Z-score unreliable if **non-normal data**
- Winsorizing may **underestimate volatility**
- Missing **structural breaks** in data