import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_and_prepare_data(city=None):
    """Načte dataset a připraví jej pro analýzu, s volitelným filtrováním podle města."""
    df = pd.read_csv('data/weatherAUS.csv')

    # Převod sloupce 'Date' na datetime
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    else:
        print("Sloupec 'Date' nebyl nalezen v datasetu.")

    selected_features = [
        'MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed',
        'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
        'Pressure9am', 'Pressure3pm', 'Temp9am', 'Temp3pm'
    ]

    missing_features = [feature for feature in selected_features if feature not in df.columns]
    for feature in missing_features:
        print(f"Sloupec '{feature}' nebyl nalezen v datasetu.")

    available_features = [feature for feature in selected_features if feature in df.columns]
    required_columns = available_features + ['RainTomorrow']

    df = df[required_columns].dropna()

    if 'RainTomorrow' in df.columns:
        le = LabelEncoder()
        df['RainTomorrow'] = le.fit_transform(df['RainTomorrow'])
    else:
        print("Upozornění: Sloupec 'RainTomorrow' nebyl nalezen v datasetu.")

    return df
