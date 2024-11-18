# 🍽️ DinnerTonight Bio Generator

## 📝 Project Description
DinnerTonight Bio Generator is a web application that helps users create engaging dating profile bios using AI-powered text generation. By inputting career, personality traits, interests, and relationship goals, users can quickly generate unique and personalized dating profiles.

## ✨ Features
- Interactive web interface
- Multiple career options
- Diverse personality trait selection
- Wide range of interests
- Various relationship goal choices
- AI-powered bio generation using Hugging Face's Falcon-7b-instruct model

## 🛠️ Technologies Used
- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- AI Model: Hugging Face Falcon-7b-instruct
- API Integration: Requests library

## 📦 Prerequisites
- Python 3.8+
- pip
- Flask
- requests library
- Hugging Face account (for API access)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/dinnertonight-bio-generator.git
cd dinnertonight-bio-generator
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install flask requests
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root and add:
```
HUGGINGFACE_API_TOKEN=your_hugging_face_api_token
```

### 5. Run the Application
```bash
python app.py
```

## 🌐 Accessing the Application
Open a web browser and navigate to `http://localhost:5000`

## 📋 How to Use
1. Select your career
2. Choose personality traits
3. Pick your interests
4. Define relationship goals
5. Click "Generate My Bio"
6. View your personalized bio!

## 🔒 Security Note
- Replace the Hugging Face API token in `app.py` with your own
- Do not commit sensitive tokens to version control

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

## 🙌 Acknowledgments
- [Hugging Face](https://huggingface.co/) for the AI model
- [Flask](https://flask.palletsprojects.com/) Web Framework
