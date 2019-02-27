from sklearn.preprocessing import LabelEncoder


COLUMNS = ["Sex", "Embarked"]


def label(df):
    _df = df.copy()
    le = LabelEncoder()
    for col in COLUMNS:
        # Not NaN index
        idx = ~_df[col].isna()
        _df.loc[idx, col] \
            = le.fit(_df.loc[idx, col]).transform(_df.loc[idx, col])
    return _df
