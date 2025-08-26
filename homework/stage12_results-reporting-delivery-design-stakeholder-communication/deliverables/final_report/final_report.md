st.markdown("""
# 📊 Scenario Analysis Dashboard

## **Executive Summary**
This dashboard compares three scenarios to evaluate returns, volatility, and risk-adjusted performance (Sharpe ratio).  

| Scenario       | Return | Volatility | Sharpe |
|----------------|--------|------------|--------|
| **Baseline**   | 12%    | 18%        | 0.56   |
| **Alt-Impute** | 11%    | 18.5%      | 0.49   |
| **Alt-Outlier**| 13.5%  | 19%        | 0.61   |

**Key Insights:**  
- **Baseline:** Balanced profile, moderate return and volatility.  
- **Alt-Impute:** Slightly lower risk-adjusted return due to mean imputation.  
- **Alt-Outlier:** Highest Sharpe ratio, but with slightly higher volatility.  

> 💡 **Insight:** Removing extreme outliers improves Sharpe ratio but may increase exposure to data loss.

---

## **Visual Analysis**

### 1️⃣ Return by Scenario
- Bar chart shows scenario returns clearly.  
- **Observation:** Outlier-adjusted scenario has the highest absolute return.

### 2️⃣ Risk-Return Tradeoff
- Scatter chart maps **volatility vs. return**, with circle sizes representing Sharpe ratio.  
- **Observation:**  
  - Baseline is stable.  
  - Alt-Outlier has higher risk but better risk-adjusted reward.  
  - Alt-Impute underperforms on Sharpe ratio.

### 3️⃣ MetricB Over Time
- Line chart visualizes metric trends over time per scenario.  
- **Observation:** Alt-Impute has the sharpest increase, but may be misleading due to mean imputation.

---

## **Assumptions & Risks**

**Assumptions per Scenario:**  

| Scenario       | Assumption                  | Method        |
|----------------|----------------------------|---------------|
| Baseline       | Missing data imputation      | Median        |
| Alt-Impute     | Missing data imputation      | Mean          |
| Alt-Outlier    | Outlier adjustment           | >3σ removed   |

**Risks:**  
- Overfitting scenario choice to historical noise.  
- Limited sample size may distort trends.  
- Assumption-driven bias can affect robustness.

> ⚠️ **Caution:** Outlier removal improves Sharpe but risks removing meaningful data.

---

## **Sensitivity Analysis**

Select a scenario to stress-test against the **Baseline**:

| Metric      | Baseline | Selected Scenario |
|------------|----------|-----------------|
| Return     | 12%      | 13.5%           |
| Volatility | 18%      | 19%             |
| Sharpe     | 0.56     | 0.61            |

**Interpretation:**  
- Alt-Outlier provides superior risk-adjusted returns compared to baseline.  
- Alt-Impute slightly underperforms and may reduce reliability.

---

## **Decision Implications**

- **Stability Preference:** Choose **Baseline**.  
- **Max Sharpe Preference:** Choose **Alt-Outlier**.  
- **Cautionary Scenario:** **Alt-Impute** may underperform due to mean imputation assumptions.

> ✅ **Recommendation:** Use outlier-adjusted data for optimal Sharpe but validate results with additional datasets and stress-testing.
""", unsafe_allow_html=True)
