## Data Storage Layer

### Folder Structure
- `data/raw/`: raw ingested data, saved as CSV .
- `data/processed/`: processed/clean data, saved as Parquet (efficient, compressed, preserves schema).

### Formats
- **CSV**: human-readable, widely supported.
- **Parquet**: efficient columnar format, smaller storage, better for analytics.

### Environment Variables
- `DATA_DIR_RAW` = data/raw
- `DATA_DIR_PROCESSED` = data/processed

Loaded from `.env` so paths are reproducible across environments.

### Utility Functions
- `write_df(df, path)` → routes to `.csv` or `.parquet` automatically.
- `read_df(path)` → reloads with error handling for missing files/engines.

### Validation
- Confirms CSV and Parquet reloads have same shape, columns, and dtypes for critical columns.
