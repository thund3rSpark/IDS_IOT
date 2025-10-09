import pickle
import pandas as pd
import numpy as np

# Load the model and pipeline
with open("pipeline1.pickle", "rb") as file:
    pipeline = pickle.load(file)

with open("model.pickle", "rb") as file:
    model = pickle.load(file)

def predict_from_csv(file_path):
    # Load CSV
    df = pd.read_csv(file_path)
    
    # Preprocess using the pipeline
    processed_data = pipeline.transform(df.drop(columns=['Label'], errors='ignore'))

    # Make predictions
    predictions = model.predict(processed_data)
    
    # Attach predictions to timestamps if available
    if 'Timestamp' in df.columns:
        df['Predicted Label'] = predictions
        return df[['Timestamp', 'Predicted Label']]
    
    df['Predicted Label'] = predictions
    return df

# Example Usage
if __name__ == "__main__":
    result = predict_from_csv("test_data.csv")  # Replace with an actual file
    print(result.head())
