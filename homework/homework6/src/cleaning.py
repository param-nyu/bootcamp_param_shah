import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def fill_missing_median(df: pd.DataFrame, columns: list = None) -> pd.DataFrame:
    if columns is None:
        columns = df.select_dtypes(include="number").columns
    for col in columns:
        df[col] = df[col].fillna(df[col].median())
    return df


def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    missing_ratio = df.isna().mean()
    cols_to_drop = missing_ratio[missing_ratio > threshold].index
    return df.drop(columns=cols_to_drop)


def normalize_data(df: pd.DataFrame, columns: list = None) -> pd.DataFrame:
    scaler = MinMaxScaler()
    if columns is None:
        columns = df.select_dtypes(include="number").columns
    df[columns] = scaler.fit_transform(df[columns])
    return df
