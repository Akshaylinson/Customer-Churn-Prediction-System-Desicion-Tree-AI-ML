# 🎯 Customer Churn Prediction System

A professional machine learning application that predicts customer churn using Decision Tree algorithms with an elegant web interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.2+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Web Interface](#web-interface)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project implements a comprehensive customer churn prediction system using machine learning. It helps businesses identify customers who are likely to discontinue their services, enabling proactive retention strategies.

The system uses a **Decision Tree Classifier** trained on customer behavioral data including demographics, service usage patterns, and billing information to predict churn probability with high accuracy.

## ✨ Features

- **🤖 AI-Powered Predictions**: Advanced Decision Tree algorithm for accurate churn prediction
- **🎨 Professional Web Interface**: Modern, responsive UI with real-time predictions
- **📊 Comprehensive Analytics**: Detailed probability scores and confidence levels
- **🔄 Real-time Processing**: Instant predictions through AJAX-powered interface
- **📱 Mobile Responsive**: Optimized for all device sizes
- **🛡️ Data Validation**: Robust input validation and error handling
- **📈 Model Persistence**: Trained models saved for consistent predictions

## 📁 Project Structure

```
decision_tree_churn_project/
├── 📂 src/                     # Source code
│   ├── 🐍 train.py            # Model training script
│   ├── 🔧 utils.py            # Dataset generation utilities
│   └── ⚙️ preprocess.py       # Data preprocessing functions
├── 📂 app/                     # Web application
│   └── 🌐 app.py              # Flask web server
├── 📂 data/                    # Generated datasets
│   └── 📊 churn_data.csv      # Training data
├── 📂 model/                   # Trained models
│   ├── 🧠 churn_model.pkl     # Decision Tree model
│   └── 🔤 encoder.pkl         # Label encoders
├── 📋 requirements.txt         # Python dependencies
└── 📖 README.md               # Project documentation
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd decision_tree_churn_project
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model**
   ```bash
   cd src
   python train.py
   ```

5. **Launch the web application**
   ```bash
   cd ../app
   python app.py
   ```

6. **Access the application**
   Open your browser and navigate to: `http://127.0.0.1:5000`

## 💻 Usage

### Training the Model
```bash
cd src
python train.py
```
This will:
- Generate synthetic customer data (1000 samples)
- Preprocess and encode categorical variables
- Train the Decision Tree classifier
- Save the model and encoders
- Display accuracy metrics

### Running the Web Application
```bash
cd app
python app.py
```
The web interface provides:
- Interactive form for customer data input
- Real-time churn prediction
- Probability scores and confidence levels
- Professional, responsive design

### Making Predictions
Fill out the customer information form with:
- **Demographics**: Age, tenure
- **Financial**: Monthly charges, total charges
- **Service Details**: Contract type, payment method
- **Features**: Internet service, online security, tech support

## 🧠 Model Details

### Algorithm: Decision Tree Classifier
- **Max Depth**: 5 (prevents overfitting)
- **Random State**: 42 (reproducible results)
- **Features**: 9 customer attributes
- **Target**: Binary churn classification (0: Stay, 1: Churn)

### Performance Metrics
- **Accuracy**: ~70.5%
- **Precision**: 0.78 (churn class)
- **Recall**: 0.52 (churn class)
- **F1-Score**: 0.62 (churn class)

### Feature Importance
The model considers these key factors:
1. Contract type (Month-to-month vs. long-term)
2. Monthly charges
3. Tenure duration
4. Online security services
5. Payment method
6. Internet service type
7. Tech support availability
8. Customer age
9. Total charges

## 🌐 Web Interface

### Design Features
- **Modern UI**: Clean, professional design with gradient backgrounds
- **Responsive Layout**: Optimized for desktop, tablet, and mobile
- **Interactive Elements**: Smooth animations and hover effects
- **Real-time Feedback**: Loading indicators and instant results
- **Error Handling**: User-friendly error messages
- **Accessibility**: ARIA labels and keyboard navigation

### Technology Stack
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Flask (Python)
- **Styling**: Custom CSS with Font Awesome icons
- **AJAX**: Asynchronous form submission

## 🔌 API Endpoints

### POST `/predict`
Predicts customer churn based on input data.

**Request Body** (Form Data):
```json
{
  "age": 35,
  "tenure": 24,
  "monthly_charges": 75.50,
  "total_charges": 1810.00,
  "contract_type": "Month-to-month",
  "payment_method": "Electronic check",
  "internet_service": "Fiber optic",
  "online_security": "No",
  "tech_support": "Yes"
}
```

**Response**:
```json
{
  "churn_prediction": "Will Churn",
  "churn_probability": "73.2%",
  "confidence": "High"
}
```

## 📊 Data Schema

### Input Features
| Feature | Type | Description | Values |
|---------|------|-------------|---------|
| age | Integer | Customer age | 18-100 |
| tenure | Integer | Months with service | 1-72 |
| monthly_charges | Float | Monthly bill amount | 20.0-120.0 |
| total_charges | Float | Total amount paid | 100.0-8000.0 |
| contract_type | String | Contract duration | Month-to-month, One year, Two year |
| payment_method | String | Payment method | Electronic check, Mailed check, Bank transfer, Credit card |
| internet_service | String | Internet service type | DSL, Fiber optic, No |
| online_security | String | Security service | Yes, No |
| tech_support | String | Tech support service | Yes, No |

## 🛠️ Development

### Adding New Features
1. **Data Features**: Modify `utils.py` to include new customer attributes
2. **Preprocessing**: Update `preprocess.py` for new data transformations
3. **Model**: Retrain using `train.py` with updated features
4. **UI**: Enhance `app.py` template for new input fields

### Model Improvements
- **Feature Engineering**: Create derived features (e.g., charges per month)
- **Algorithm Tuning**: Experiment with different hyperparameters
- **Ensemble Methods**: Combine multiple algorithms
- **Cross-Validation**: Implement k-fold validation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Scikit-learn**: For the machine learning algorithms
- **Flask**: For the web framework
- **Font Awesome**: For the beautiful icons
- **Decision Tree Algorithm**: For interpretable predictions

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](../../issues) page
2. Create a new issue with detailed description
3. Include error messages and system information

---

**Made with ❤️ for better customer retention strategies**
