# Executive Summary
In this study, we approximated SOXX using a sparse linear combination of semiconductor stocks based on daily returns from **2015–present**. The final **Smart ETF** held **10 names** with weights derived via LASSO and achieved **out-of-sample R² = 0.92**. Residual dynamics were modeled with an ARIMA(1,0,1), which indicates mild mean reversion in the tracking error. While concentration risk and survivorship bias are present, sensitivity checks suggest the tracker is reasonably stable across subperiods.

## Final Weights
| Ticker | Weight |
|-------:|-------:|
| TXN    | 0.1760 |
| LRCX   | 0.1494 |
| AVGO   | 0.1421 |
| QCOM   | 0.1187 |
| INTC   | 0.1159 |
| NVDA   | 0.1064 |
| TSM    | 0.0777 |
| MRVL   | 0.0709 |
| MU     | 0.0643 |
| AMD    | 0.0375 |

*Note: weights are the non-zero LASSO coefficients from the fitted model and represent the linear combination of daily returns used for the Smart ETF.*

## Risk & Limitations
- **Concentration risk:** Top names (e.g., TXN, LRCX, AVGO) carry significant weight, amplifying idiosyncratic moves.  
- **Survivorship / selection bias:** Holdings were curated/fixed rather than reconstructed from historical index membership.  
- **Operational omissions:** Transaction costs, slippage, and taxes are not modeled.  
- **Model fragility:** ARIMA diagnostics show heavy-tailed residuals and heteroskedasticity, implying occasional extreme errors.

## Next Steps
- Compute and report exact annualized tracking error, rolling tracking error, and cumulative performance gap using the ETF and SmartETF return series.  
- Add walk-forward retraining and weight-stability reporting (rolling LASSO).  
- Expand diagnostics: heteroskedasticity-robust inference, residual bootstraps, and stress tests for regime shifts.
