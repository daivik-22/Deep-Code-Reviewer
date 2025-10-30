# DeepCode Reviewer

## 🔍 AI-Powered Code Analysis Partner

DeepCode Reviewer is a web-based tool that leverages the Gemini API to provide intelligent code reviews. Paste your code, and get instant feedback on quality, performance, best practices, and security.

## ✨ Features

-   **AI-Powered Code Review**: Get comprehensive feedback on your code using Google's Gemini AI.
-   **Light and Dark Themes**: Switch between a comfortable light and dark interface.
-   **Easy to Use**: Simple web interface for quick code analysis.

## 🚀 Setup and Installation

Follow these steps to get the DeepCode Reviewer up and running on your local machine.

### Prerequisites

-   Python 3.8+
-   `pip` (Python package installer)
-   A Google Gemini API Key

### 1. Clone the Repository (if applicable)

If you haven't already, clone the project repository:

```bash
git clone <repository_url>
cd DeepCode-Reviewer
```

### 2. Install Dependencies

Navigate to the project directory and install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API Key

Create a `.env` file in the root of the project directory (if one doesn't exist) and add your Gemini API key:

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
```

Replace `YOUR_GEMINI_API_KEY_HERE` with your actual API key obtained from the Google AI Studio.

### 4. Run the Application

Start the Flask development server:

```bash
python app.py
```

The application will typically run on `http://127.0.0.1:5000/`. Open this URL in your web browser.

## 💡 Usage

1.  **Open your browser** to the address provided in the terminal (e.g., `http://127.0.0.1:5000/`).
2.  **Paste your code** into the provided text area.
3.  Click the **"Review Code"** button to get an AI-powered review.
4.  Use the **"Switch to Dark Mode" / "Switch to Light Mode"** button to toggle themes.
5.  Click **"Clear"** to clear the code input and review results.

## 📁 Project Structure

```
DeepCode-Reviewer/
├── app.py              # Main Flask application file
├── reviewer.py         # Core logic for interacting with Gemini API
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (e.g., GEMINI_API_KEY)
├── static/             # Static assets (CSS, JS, images)
│   ├── style.css       # Light theme CSS
│   ├── style_dark.css  # Dark theme CSS
│   └── .placeholder    # Placeholder file
└── templates/          # HTML templates
    ├── index.html      # Original index (might be deprecated or for reference)
    ├── index_light.html # HTML for the light theme
    ├── index_dark.html  # HTML for the dark theme
    └── .placeholder    # Placeholder file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details. (Note: A `LICENSE` file is not included in this example, but would typically be present.)
