import pandas as pd


def load_dataset(file_name):
    """
    Load the CSV file into a Pandas DataFrame.
    """

    try:
        df = pd.read_csv(file_name)
        print("Dataset loaded successfully.")
        return df

    except FileNotFoundError:
        print("Error: The file was not found.")
        print("Make sure the CSV file is in the same folder as main.py.")
        return None


def clean_dataset(df):
    """
    Convert important columns into numeric values.
    """

    df = df.copy()

    numeric_columns = [
        "loan_amount",
        "income",
        "interest_rate",
        "property_value"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    return df


def show_dataset_overview(df):
    """
    Display basic information about the dataset.
    """

    print("\n" + "=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)

    print(f"Number of rows: {len(df)}")
    print(f"Number of columns: {len(df.columns)}")

    selected_columns = [
        "applicant_age",
        "loan_amount",
        "income",
        "action_taken"
    ]

    print("\nFirst five rows of selected columns:")
    print(df[selected_columns].head())
