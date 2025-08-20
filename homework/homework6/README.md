# Stage 06 – Data Preprocessing

This stage focuses on preparing the raw dataset for downstream modeling and analysis.  
The key tasks include data loading, cleaning, and the creation of missingness mechanism (MCAR) for experimentation.  

---

## Dataset

The dataset contains performance and risk statistics of investment strategies with columns such as:

- `Strategy`
- `AUM`
- `Relative Alpha (1Y)`
- `% of +ve months (Fund Data)`
- `Alpha (1Y)`
- `Beta (1Y)`
- `SD (1Y)`
- `Sharpe Ratio (1Y)`
- `Alpha (SI)`
- `Info Ratio (SI)`
- `Consistency Ratio`

---

## Cleaning Strategy

1. **Loading Raw Data**  
   - The raw CSV is loaded from the `data/` directory.  
   - All columns are preserved in their original format.  

2. **Handling Missingness**  
   To simulate real-world scenarios, three types of missing data mechanisms are introduced:

   - **MCAR (Missing Completely at Random):**  
     Randomly set ~10% of values in selected numerical columns to `NaN`.

   - **MAR (Missing at Random):**  
     Introduce missingness in `Alpha (1Y)` when `AUM` is below the median.  
     This simulates cases where missingness depends on other observable variables.

   - **MNAR (Missing Not at Random):**  
     Introduce missingness in `Sharpe Ratio (1Y)` when the value itself is low (e.g., `< 0.8`).  
     This simulates bias where poor-performing data is less likely to be reported.  

3. **Output Format**  
   - All variants (original, MCAR) are stored **side by side** in a single CSV file.  
   - Column suffixes `_MCAR` indicate the missingness mechanism.  

   Example:  
   - `Alpha (1Y)` (original)  
   - `Alpha (1Y)_MCAR`  

