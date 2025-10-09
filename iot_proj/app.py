from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# Define the custom transformer class FIRST
class dropcol(BaseEstimator, TransformerMixin):
    def __init__(self, columns_drop):
        self.columns_drop = columns_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.drop(self.columns_drop, axis=1, errors="ignore")

app = Flask(__name__)

# Load the model and pipeline (keep your original paths)
pipeline_path = r"C:\Users\K.Murugesh\Education\Final\pipeline1.pickel"
model_path = r"C:\Users\K.Murugesh\Downloads\Telegram Desktop\model_LCR.pickel"

try:
    with open(pipeline_path, "rb") as file:
        pipeline = pickle.load(file)
    print("Pipeline loaded successfully!")
    
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading models: {str(e)}")
    raise

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Validate file exists
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    
    # Validate file is CSV
    if not file.filename.lower().endswith('.csv'):
        return jsonify({"error": "Only CSV files are supported"}), 400

    try:
        # Read CSV with error handling
        df = pd.read_csv(file)
        
        # Check required columns exist
        required_cols = ['Timestamp', 'IP_Address', 'Dst_IP']  # Add other required columns
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            return jsonify({"error": f"Missing required columns: {', '.join(missing_cols)}"}), 400

        # Preserve metadata
        metadata = df[['Timestamp', 'IP_Address', 'Dst_IP']].copy()
        
        # Process through pipeline
        processed_data = pipeline.transform(df.drop(columns=['Label'], errors='ignore'))
        predictions = model.predict(processed_data)

        # Prepare response with metadata
        results = metadata.copy()
        results['Prediction'] = predictions
        results['Label'] = results['Prediction'].map({
            0: 'Benign',
            1: 'DoS',
            2: 'DDoS',
            3: 'Bot',
            4: 'Brute Force',
            5: 'Infiltration'
        })

        return jsonify({
            "data": results.to_dict(orient='records'),
            "stats": {
                "total": len(results),
                "benign": int((predictions == 0).sum()),
                "threats": int((predictions != 0).sum())
            }
        })

    except pd.errors.EmptyDataError:
        return jsonify({"error": "The CSV file is empty"}), 400
    except pd.errors.ParserError:
        return jsonify({"error": "Error parsing CSV file"}), 400
    except Exception as e:
        return jsonify({"error": f"Processing error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)