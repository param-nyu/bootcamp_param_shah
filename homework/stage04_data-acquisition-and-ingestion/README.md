# Stage 04 – Data Collection & Validation  

## 1. Overview  
In this stage, we focus on pulling data from external sources, parameterizing our workflow, and validating that the data meets expected quality standards before it’s stored or used downstream.  

---

## 2. Data Sources  
The following external sources/URLs were used:  
- **Yahoo Finance (via `yfinance`)** – for stock market & company-level data.  
- **PMS AIF World** ([Top PMS ranking](https://www.pmsaifworld.com/top-best-30-pmss-in-india-ranked-as-per-information-ratio/)) – scraped for PMS information ratio rankings.  
- (Add more URLs if you used others).  

---

## 3. Parameters  
Parameters are externalized in the `.env` file to avoid hardcoding. Example keys:  

```env
# Example .env (DO NOT COMMIT TO GIT)
YF_TICKER=ULTRATECH.NS  
SCRAPE_URL=https://www.pmsaifworld.com/top-best-30-pmss-in-india-ranked-as-per-information-ratio/  
DATA_DIR=./data  
