import datetime
from data_preprocessing import global_load_and_prepare_data

def main(file_path='data/weatherAUS.csv', city="Albury"):
    df = global_load_and_prepare_data(file_path)


if __name__ == "__main__":
    main()
