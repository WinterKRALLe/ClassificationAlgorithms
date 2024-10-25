import pandas as pd
from sklearn.preprocessing import LabelEncoder

def global_load_and_prepare_data(file_path):
    df = pd.read_csv(file_path)
    
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    else:
        print("Upozornění: Sloupec 'Date' nebyl nalezen v datasetu.")
    
    selected_features = [
        'MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed',
        'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
        'Pressure9am', 'Pressure3pm', 'Temp9am', 'Temp3pm'
    ]
    
    for feature in selected_features:
        if feature not in df.columns:
            print(f"Upozornění: Sloupec '{feature}' nebyl nalezen v datasetu.")
    
    df = df[selected_features + ['RainTomorrow']].dropna()
    
    le = LabelEncoder()
    df['RainTomorrow'] = le.fit_transform(df['RainTomorrow'])

    return df