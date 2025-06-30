import os
import joblib
import numpy as np
from django.conf import settings

class TeslaPricePredictor:
    def __init__(self):
        self.model_path = os.path.join(settings.BASE_DIR, 'ml_predictor/models/')
        self.load_models()
    
    def load_models(self):
        """Load all trained models and encoders"""
        try:
            self.rf_model = joblib.load(os.path.join(self.model_path, 'tesla_random_forest_model.pkl'))
            self.model_encoder = joblib.load(os.path.join(self.model_path, 'tesla_model_encoder.pkl'))
            self.country_encoder = joblib.load(os.path.join(self.model_path, 'tesla_country_encoder.pkl'))
            self.purchase_encoder = joblib.load(os.path.join(self.model_path, 'tesla_purchase_encoder.pkl'))
            self.feature_columns = joblib.load(os.path.join(self.model_path, 'tesla_feature_columns.pkl'))
            print("✅ Tesla ML models loaded successfully")
        except Exception as e:
            print(f"❌ Error loading models: {e}")
    
    def predict_price(self, model_name, country, purchase_type, year=2024, quarter=1):
        """Make Tesla price prediction"""
        try:
            # Encode inputs
            model_encoded = self.model_encoder.transform([model_name])[0]
            country_encoded = self.country_encoder.transform([country])[0]
            purchase_encoded = self.purchase_encoder.transform([purchase_type])[0]
            
            # Create feature array
            features = [
                year,
                quarter,
                year + (quarter-1)*0.25,
                model_encoded,
                country_encoded,
                purchase_encoded,
                1 if model_name in ['Model S', 'Model X'] else 0,
                1 if model_name in ['Model 3', 'Model Y'] else 0,
                1  # Major market assumption
            ]
            
            # Make prediction
            predicted_price = self.rf_model.predict([features])[0]
            
            return {
                'success': True,
                'predicted_price': round(predicted_price, 2),
                'confidence_range': '±$2,918.91',
                'model_accuracy': '95.4%',
                'inputs': {
                    'model': model_name,
                    'country': country,
                    'purchase_type': purchase_type,
                    'year': year,
                    'quarter': quarter
                }
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'predicted_price': 0
            }

# Initialize global predictor
tesla_predictor = TeslaPricePredictor()
