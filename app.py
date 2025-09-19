from flask import Flask, render_template, request, jsonify
from model import predict_crop

# Initialize Flask app
app = Flask(__name__)

# Root should show auth first
@app.route('/')
def root_auth():
    return render_template('auth.html')

# Backward-compatible HTML routes
@app.route('/start.html')
def start_html():
    return render_template('start.html')

# Route for authentication page
@app.route('/auth')
def auth():
    return render_template('auth.html')

@app.route('/auth.html')
def auth_html():
    return render_template('auth.html')

# Route for start page (landing after auth)
@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/home.html')
def home_html():
    return render_template('home.html')

# Route for AI assistant page (after start)
@app.route('/ai-assistant')
def ai_assistant():
    return render_template('ai-assistant.html')

@app.route('/ai-assistant.html')
def ai_assistant_html():
    return render_template('ai-assistant.html')

# Crop recommendation form page
@app.route('/crop-recommendation')
def crop_recommendation():
    return render_template('crop_recommend.html')

@app.route('/crop_recommendation.html')
def crop_recommendation_html():
    return render_template('crop_recommendation.html')

@app.route('/scan')
def scan():
    return render_template('scan.html')

@app.route('/scan.html')
def scan_html():
    return render_template('scan.html')

# Route for weather page
@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/weather.html')
def weather_html():
    return render_template('weather.html')

# Route for market page
@app.route('/market')
def market():
    return render_template('market.html')

@app.route('/market.html')
def market_html():
    return render_template('market.html')

# API endpoint for crop prediction
@app.route('/predict_crop', methods=['POST'])
def predict_crop_api():
    try:
        data = request.get_json()
        
        # Extract parameters
        N = float(data.get('N'))
        P = float(data.get('P'))
        K = float(data.get('K'))
        temperature = float(data.get('temperature'))
        humidity = float(data.get('humidity'))
        ph = float(data.get('ph'))
        rainfall = float(data.get('rainfall'))
        
        # Get prediction
        crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
        
        if crop:
            return jsonify({'crop': crop})
        else:
            return jsonify({'error': 'Could not make prediction'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)