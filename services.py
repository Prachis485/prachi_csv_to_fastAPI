import pandas as pd

df = None

def load_data():
    global df
    if df is None:
        df = pd.read_csv("data/students_complete.csv")
        df = df.fillna("")  # handle missing values
    return df


def get_all_data():
    return load_data().to_dict(orient="records")


def get_data_by_id(student_id: str):
    data = load_data()
    
    # assuming column name is 'student_id'
    result = data[data['student_id'] == student_id]

    if result.empty:
        return None
    
    return result.iloc[0].to_dict()