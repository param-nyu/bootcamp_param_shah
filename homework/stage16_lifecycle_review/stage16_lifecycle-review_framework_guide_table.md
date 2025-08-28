# Applied Financial Engineering — Framework Guide Template

This Framework Guide is a structured reflection tool.  
Fill it in as you progress through the course or at the end of your project.  
It will help you connect each stage of the **Applied Financial Engineering Lifecycle** to your own project, and create a portfolio-ready artifact.

---

## How to Use
- Each row corresponds to one stage in the lifecycle.  
- Use the prompts to guide your answers.  
- Be concise but specific - 2-4 sentences per cell is often enough.  
- This is **not a test prep sheet**. It’s a way to *document, reflect, and demonstrate* your process.

---
# Applied Financial Engineering - Framework Guide

## Framework Guide Table

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
| **1. Problem Framing & Scoping** | Defined project as building a pipeline to ingest SOXX ETF data, train a model, and serve predictions. Goal was educational, not alpha generation. | Ambiguity in scope: whether to focus on data engineering or modeling. | Scoped to an end-to-end prototype with emphasis on reproducibility. | Next time, define success metrics (MAE, AUC) earlier and tie them to business utility. |
| **2. Tooling Setup** | Used Python, pandas, scikit-learn, Flask, and basic logging. Jupyter notebooks for iteration. | Environment mismatches between notebook and Flask app. | Used virtualenv + requirements.txt. | Containerize with Docker for consistent deployment. |
| **3. Python Fundamentals** | Practiced basic loop and vectorized functions. | Initially mixed exploratory and production code. | Refactored into separate scripts and modules. | Strengthen testing practices and add type hints. |
| **4. Data Acquisition / Ingestion** | Mock ingestion of SOXX ETF prices data (CSV/JSON). | Data gaps and schema drift potential. | Designed idempotent ingestion step with checkpoints. | Automate data freshness checks and schema validation. |
| **5. Data Storage** | Stored cleaned datasets as JSON and models as parquet. | Tradeoff between simplicity and scalability. | Chose lightweight local storage. | Explore databases or object storage for larger scale. |
| **6. Data Preprocessing** | Basic cleaning: handling nulls, ensuring consistent schema. | Risk of silent data corruption. | Added logging of rows in/out per step. | Add validation rules and profiling tools. |
| **7. Outlier Analysis** | Basic detection of price anomalies using thresholds. | Distinguishing market shocks vs data errors. | Chose to keep outliers but flag them. | Add rolling statistical tests or domain-based filters. |
| **8. Exploratory Data Analysis (EDA)** | Generated plots of returns, moving averages. | Limited insight due to mock data scale. | Focused on high-level trends. | Expand EDA with correlation heatmaps and factor analysis. |
| **9. Feature Engineering** | Created lag features, moving averages. | Feature usefulness uncertain with small dataset. | Validated with simple regression benchmarks. | Incorporate volatility and sector-level indicators. |
| **10. Modeling (Regression / Time Series / Classification)** | Trained a simple regression model on price/returns. | Overfitting risk, limited validation. | Kept model simple and interpretable. | Test time-series models (ARIMA, LSTM). |
| **11. Evaluation & Risk Communication** | Used MSE/MAE as core metrics. | Hard to judge significance on limited data. | Communicated model as prototype, not production-ready. | Add rolling backtests and confidence intervals. |
| **12. Results Reporting, Delivery Design & Stakeholder Communication** | Output via notebook charts and text reports. | Hard to explain limitations of toy model. | Emphasized transparency about scope. | Build dashboards (e.g., Streamlit). |
| **13. Productization** | Saved final model as pickle; added Flask API endpoint. | Packaging and dependency issues. | Wrote minimal `app.py` for serving predictions. | Add CI/CD pipeline and versioning. |
| **14. Deployment & Monitoring** | Mock deployment plan with metrics across data, model, system, business. | Hard to simulate real drift in mock project. | Proposed PSI checks, latency monitoring, business KPIs. | Implement actual alerting + dashboards. |
| **15. Orchestration & System Design** | Broke pipeline into DAG: ingest → clean → train/score → report. | Managing dependencies and checkpoints. | Used DataFrames to define tasks, logging plan. | Automate with Prefect/Airflow when scale requires. |
| **16. Lifecycle Review & Reflection** | Learned full lifecycle from scoping to orchestration. | Hardest part: balancing breadth vs depth. | Consistency and modularity paid off across stages. | Next time, spend more time on evaluation and monitoring. |

---

## Reflection Prompts

- **Most difficult stage:** Deployment & Monitoring - designing realistic monitoring for a toy model was abstract.  
- **Most rewarding stage:** Orchestration & System Design - seeing the pieces connect into a coherent DAG was satisfying.  
- **Connections:** Early scoping decisions constrained later modeling depth; focusing on end-to-end delivery shaped design tradeoffs.  
- **If repeated:** I would define evaluation metrics earlier and implement better validation pipelines.  
- **Skills to strengthen:** Time-series modeling, and automated monitoring/orchestration frameworks.  
