# Know Your Leaf 🍃

A lightweight **Python-Flask web application for plant leaf health analysis**, combining image processing, rule-based classification, and an interactive chatbot into a single web interface.

The project demonstrates practical software-development skills including **Python programming, Flask web development, REST-style endpoints, image processing with OpenCV, input handling, modular code organization, and frontend-backend integration**.

---

## Overview

**Know Your Leaf** was developed to provide users with a simple way to analyze plant leaves and obtain basic information about possible leaf conditions.

The application supports three primary workflows:

1. **Leaf health lookup** based on plant type and leaf color.
2. **Image-based leaf color detection** using OpenCV.
3. **Interactive chatbot** for plant and leaf-related queries.

The application uses a lightweight rule-based knowledge base rather than claiming to perform full disease recognition through a trained machine-learning model.

---

## Key Features

### 🌿 Plant Health Analysis

Users can provide:

* Plant type
* Leaf color

The application uses the supplied information to retrieve the corresponding plant-health information from its predefined knowledge base.

### 📷 Image Processing

Users can upload a leaf image.

The application processes the image using **OpenCV** and performs color analysis to determine the dominant leaf color.

Processing flow:

```text
Leaf Image
    ↓
Image Upload
    ↓
OpenCV Processing
    ↓
Color Analysis
    ↓
Leaf Color Classification
    ↓
Plant Health Information
```

### 💬 Interactive Chatbot

The application includes a lightweight chatbot that accepts natural-language-style questions.

The chatbot identifies supported:

* Plant names
* Leaf colors

and uses them to retrieve relevant information from the application's knowledge base.

Example:

```text
User:
What is wrong with my brown tomato leaf?

Application:
Identifies → Tomato + Brown
             ↓
Retrieves corresponding information
             ↓
Returns response
```

---

## Technology Stack

| Technology     | Usage                                 |
| -------------- | ------------------------------------- |
| **Python**     | Application logic                     |
| **Flask**      | Web application framework             |
| **OpenCV**     | Image processing and color analysis   |
| **NumPy**      | Numerical operations                  |
| **HTML/CSS**   | User interface                        |
| **Jinja2**     | Server-side template rendering        |
| **Git/GitHub** | Version control and source management |

---

## System Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Web Interface     │
                    │    HTML / Jinja     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Flask Server     │
                    │       app.py        │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
                 ▼             ▼             ▼
          Plant Analysis   Image Upload   Chatbot
                 │             │             │
                 │             ▼             │
                 │        OpenCV            │
                 │        Processing        │
                 │             │             │
                 └─────────────┼─────────────┘
                               ▼
                    ┌─────────────────────┐
                    │    model.py         │
                    │                     │
                    │ Rule-based Analysis │
                    │ Color Detection     │
                    │ Chatbot Logic       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Response        │
                    └─────────────────────┘
```

---

## Project Structure

```text
Know-Your-Leaf/
│
├── app.py                  # Flask application and routes
├── model.py                # Analysis, color detection and chatbot logic
├── requirements.txt        # Python dependencies
├── .gitignore
│
└── templates/
    └── index.html          # Web interface
```

### `app.py`

Responsible for:

* Initializing the Flask application
* Handling HTTP requests
* Managing application routes
* Receiving user input
* Handling image uploads
* Connecting frontend requests with backend processing

### `model.py`

Contains the application's core processing logic, including:

* Plant-health knowledge base
* Plant/leaf-color analysis
* Image color detection
* Chatbot processing

### `templates/index.html`

Provides the browser-based user interface through which users interact with the application.

---

## Application Workflow

### 1. User Input

The user can either:

```text
Select Plant + Leaf Color
```

or:

```text
Upload Leaf Image
```

or:

```text
Ask the Chatbot
```

### 2. Backend Processing

The Flask application receives the request and passes the relevant information to the processing functions.

### 3. Image Processing

For uploaded images, OpenCV is used to process the image and estimate the dominant color.

### 4. Knowledge-Base Lookup

The detected/provided information is matched against the predefined plant-health knowledge base.

### 5. Response

The application returns the corresponding information through the web interface.

---

## Supported Plant Analysis

The current implementation contains predefined information for multiple plants, including:

* Tomato
* Potato
* Grape
* Apple
* Banana

The application can associate supported plants with different leaf-color conditions through its rule-based knowledge base.

---

## Installation

### Prerequisites

* Python 3.x
* pip
* Git

### Clone the repository

```bash
git clone https://github.com/Harisundarrajan/Know-Your-Leaf.git
cd Know-Your-Leaf
```

### Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open the local Flask URL displayed in the terminal.

---

## Engineering Concepts Demonstrated

This project demonstrates several concepts relevant to practical software development:

### Backend Development

* Python
* Flask
* HTTP request handling
* Route design
* Form/input processing

### Image Processing

* Image loading
* Color-space conversion
* HSV-based color analysis
* Basic image feature extraction

### Software Design

* Separation of application and processing logic
* Reusable Python functions
* Frontend/backend integration
* Input validation and processing

### Development Practices

* Git-based source control
* Dependency management using `requirements.txt`
* Modular project structure
* Local development and testing

---

## Limitations

The current implementation is intentionally lightweight.

It primarily uses:

```text
Plant + Leaf Color
        ↓
Rule-Based Knowledge Base
        ↓
Result
```

Therefore, it should **not be interpreted as a production-grade plant disease detection system or a trained deep-learning model**.

Image analysis is primarily focused on color information and does not perform comprehensive disease classification based on visual symptoms.

---

## Future Improvements

Potential extensions include:

* [ ] Train a CNN-based plant disease classifier
* [ ] Add a larger and validated plant-disease dataset
* [ ] Add image segmentation for better leaf isolation
* [ ] Introduce confidence scores
* [ ] Expand plant and disease coverage
* [ ] Add automated unit and integration testing
* [ ] Add structured logging and error handling
* [ ] Containerize the application with Docker
* [ ] Add CI/CD using GitHub Actions
* [ ] Deploy the application to a cloud environment
* [ ] Improve chatbot intent detection using NLP
* [ ] Add an API documentation layer
* [ ] Add monitoring and application health checks

---

## Why This Project

The project was built to explore the integration of **Python backend development, web applications, image processing, and conversational interfaces** into a single application.

It provided practical experience in taking user input, processing data on the backend, integrating an image-processing workflow, and returning results through a web interface.

---

## Author

**Harisundarrajan**

GitHub:
https://github.com/Harisundarrajan

Repository:
https://github.com/Harisundarrajan/Know-Your-Leaf

---

## Disclaimer

This application is intended for educational and demonstration purposes. Its results should not be treated as professional agricultural or plant-disease diagnosis.
