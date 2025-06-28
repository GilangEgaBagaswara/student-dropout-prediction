#!/usr/bin/env python3
"""
Script to fix model compatibility issues for Streamlit Cloud deployment
"""

import pandas as pd
import numpy as np
import pickle
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import warnings
warnings.filterwarnings('ignore')

def load_and_prepare_data():
    """Load and prepare the dataset"""
    try:
        # Load dataset
        df = pd.read_csv('data.csv')
        print(f"Data loaded successfully: {df.shape}")
        
        # Basic preprocessing
        # Remove non-numeric columns that might cause issues
        numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
        
        # If 'Target' column exists, separate it
        if 'Target' in df.columns:
            X = df.drop('Target', axis=1)
            y = df['Target']
        elif 'Dropout' in df.columns:
            X = df.drop('Dropout', axis=1)
            y = df['Dropout']
        else:
            # Assume last column is target
            X = df.iloc[:, :-1]
            y = df.iloc[:, -1]
        
        # Convert to numeric and handle missing values
        X = X.select_dtypes(include=[np.number])
        X = X.fillna(X.median())
        
        # Encode target if needed
        if y.dtype == 'object':
            le = LabelEncoder()
            y = le.fit_transform(y)
        
        return X, y
        
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

def create_compatible_model(X, y):
    """Create a new model with better compatibility"""
    try:
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Scale features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Create model with explicit random_state for compatibility
        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            n_jobs=1  # Avoid multiprocessing issues
        )
        
        # Train model
        model.fit(X_train_scaled, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test_scaled)
        
        # Calculate metrics
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='weighted'),
            'recall': recall_score(y_test, y_pred, average='weighted'),
            'f1_score': f1_score(y_test, y_pred, average='weighted')
        }
        
        print(f"Model Performance:")
        for metric, value in metrics.items():
            print(f"  {metric}: {value:.4f}")
        
        return model, scaler, X.columns.tolist(), metrics
        
    except Exception as e:
        print(f"Error creating model: {e}")
        return None, None, None, None

def save_compatible_model(model, scaler, feature_names, metrics):
    """Save model with better compatibility"""
    try:
        # Save model with protocol 4 for better compatibility
        joblib.dump(model, 'model/student_dropout_model.pkl', protocol=4)
        print("✅ Model saved successfully")
        
        # Save feature names
        with open('model/feature_names.pkl', 'wb') as f:
            pickle.dump(feature_names, f, protocol=4)
        print("✅ Feature names saved successfully")
        
        # Save model metrics
        with open('model/model_metrics.pkl', 'wb') as f:
            pickle.dump(metrics, f, protocol=4)
        print("✅ Model metrics saved successfully")
        
        # Save scaler for consistency
        with open('model/scaler.pkl', 'wb') as f:
            pickle.dump(scaler, f, protocol=4)
        print("✅ Scaler saved successfully")
        
        return True
        
    except Exception as e:
        print(f"Error saving model: {e}")
        return False

def main():
    """Main function to fix model compatibility"""
    print("🔧 Fixing model compatibility for Streamlit Cloud...")
    
    # Load data
    X, y = load_and_prepare_data()
    if X is None:
        print("❌ Failed to load data")
        return
    
    # Create compatible model
    model, scaler, feature_names, metrics = create_compatible_model(X, y)
    if model is None:
        print("❌ Failed to create model")
        return
    
    # Save compatible model
    if save_compatible_model(model, scaler, feature_names, metrics):
        print("🎉 Model compatibility fixed successfully!")
        print("📤 Ready to push to GitHub and redeploy to Streamlit Cloud")
    else:
        print("❌ Failed to save model")

if __name__ == "__main__":
    main()
