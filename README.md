# Know Your Leaf

Know Your Leaf is a simple web application that helps users understand the basic health condition of plant leaves.

The project combines **Python, Flask, image processing, and a simple chatbot** to provide plant and leaf-related information.

## What this project does

* Allows users to select a plant and leaf condition.
* Allows users to upload a leaf image.
* Analyzes the leaf image based on its color.
* Provides basic information about possible leaf conditions.
* Includes a chatbot for asking common questions about plants and leaves.
* Uses a simple knowledge base to provide responses.

## Technologies Used

* **Python**
* **Flask**
* **OpenCV**
* **NumPy**
* **HTML/CSS**

## How It Works

The application has three main parts:

### 1. Leaf Image Analysis

The user can upload an image of a leaf.

```text
Leaf Image
    ↓
Image Processing
    ↓
Color Analysis
    ↓
Leaf Information
```

The application processes the image and checks the leaf color to provide related information.

### 2. Plant Information

The user can select a plant and provide information about the leaf.

The application then checks the available data and provides the related plant-health information.

### 3. Chatbot

The project also includes a simple chatbot.

Users can ask common questions related to plants and leaves, and the chatbot provides responses using the information available in the project.

## Project Structure

```text
Know-Your-Leaf/
│
├── app.py
├── model.py
├── requirements.txt
├── .gitignore
│
└── templates/
    └── index.html
```

### `app.py`

Handles the Flask application, web pages, user requests, and image uploads.

### `model.py`

Contains the main processing and plant-health information used by the application.

### `templates/`

Contains the HTML files used for the web interface.

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/Harisundarrajan/Know-Your-Leaf.git
cd Know-Your-Leaf
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

The application will run locally using Flask.

## What I Learned

Through this project, I learned about:

* Python programming
* Flask web development
* Image processing using OpenCV
* Working with image data
* Connecting frontend and backend
* Handling user uploads
* Building a simple chatbot
* Using a knowledge base for application responses
* Organizing a Python web project

## Future Improvements

Some improvements I would like to make in the future:

* Add more plant varieties.
* Improve leaf image analysis.
* Add a larger plant-health dataset.
* Improve the chatbot's responses.
* Add machine-learning-based disease detection.
* Deploy the application online.

## Done By:

**Hari S**

GitHub: https://github.com/Harisundarrajan
