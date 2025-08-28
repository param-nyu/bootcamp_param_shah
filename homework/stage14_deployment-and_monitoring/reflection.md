# Stage 14: Deployment & Monitoring (Reflection)

Deploying the SOXX mimic model carries several concrete risks. First, **data issues** could arise if Yahoo Finance fails to provide complete or timely daily prices for SOXX or its constituents. Missing data or delayed updates could lead to inaccurate predictions. Second, **model degradation** is possible because correlations between the ETF and the selected subset of constituents may change over time, reducing replication accuracy. Third, **system-level risks** include API downtime or server failures that prevent the model from serving predictions. Fourth, **business impact** could occur if predictions consistently misalign with the ETF, leading to misinformed strategy decisions.

Monitoring should cover four layers:

1. **Data:** Track missing values, date alignment, and freshness. Threshold: no more than 5% missing data per day; daily updates must complete by 5 PM EST. Alerts to the analyst if thresholds are exceeded.  
2. **Model:** Track rolling R² between predicted and actual ETF returns, and tracking error over a 14-day window. Thresholds: R² < 0.80 or tracking error > 2% triggers review. Retraining occurs when correlations drift substantially.  
3. **Hypthetical System:** Monitor API uptime and response latency. Thresholds: 99% uptime per week, p95 latency < 1 second. Alerts sent to the platform on-call.  
4. **Hypthetical Business:** Track cumulative deviation between mimic and ETF. If deviation exceeds 2% over two weeks, notify the analyst for review.

**Hypthetical Ownership:** Analysts maintain model monitoring and decide on retraining; data engineers handle ingestion issues; platform team manages server/API reliability. All incidents are logged in a shared repository with timestamps, and a brief runbook guides the first response. This ensures the model remains usable, reliable, and interpretable in production.
