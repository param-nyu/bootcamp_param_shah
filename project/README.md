# SmartETF: Sparse Replication of SOXX

## Summary
This project replicates the **iShares Semiconductor ETF (SOXX)** using a **sparse linear combination of constituent stocks**.  
We combine **LASSO regression** (for portfolio selection) with **ARIMA modeling** (for residual dynamics).  
The objective: track SOXX performance with fewer names, while keeping accuracy high.

---

## Method
1. **Data**: Daily returns for SOXX and its constituents.  
2. **LASSO Regression**: Identify key holdings that explain SOXX returns.  
3. **Residual Modeling**: Apply ARIMA(1,0,1) to capture tracking error structure.  
4. **Validation**: Out-of-sample performance measured by R² and tracking error.

---

## Results
- Final portfolio holds **10 stocks**.  
- Out-of-sample **R² = 0.92**.  
- Tracking error shows mild mean reversion with a tracking error of around 9.96%.  

### Portfolio Weights
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

---

## Risks & Limitations
- Slight concentration in a few names.  
- Survivorship bias in data.  
- No trading costs, slippage, or taxes included.  

