from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Crop label to name mapping dictionary
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
    8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
    14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
    19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from form
        features = [float(request.form.get(k)) for k in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
        features_array = np.array([features])

        # Get prediction from model
        prediction = model.predict(features_array)

        # Use crop_dict to convert label to name
        
        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            result = f"{crop} is the best crop to be cultivated right there."
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."

        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
