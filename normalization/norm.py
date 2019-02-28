CONF = {
    "Fare": 10000,
}


def norm(df):
    _df = df.copy()
    for k, v in CONF.items():
        _df[k] *= v

    return _df
