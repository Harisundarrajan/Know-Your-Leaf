import cv2
import numpy as np

disease_db = {
    "tomato": {
        "yellow": "Tomato Yellow Leaf Curl Virus - Apply neem oil spray weekly",
        "brown": "Late Blight - Remove affected leaves, apply copper fungicide",
        "white": "Powdery Mildew - Apply sulfur-based fungicide",
        "green": "Healthy - No action needed"
    },
    "potato": {
        "brown": "Potato Late Blight - Apply Mancozeb, remove infected plants",
        "yellow": "Potato Leafhopper damage - Apply insecticide spray",
        "white": "Powdery Mildew - Apply potassium bicarbonate spray",
        "green": "Healthy - No action needed"
    },
    "grape": {
        "brown": "Grape Black Rot - Prune affected areas, apply fungicide",
        "yellow": "Nutrient deficiency - Apply iron chelate fertilizer",
        "white": "Downy Mildew - Apply copper-based fungicide",
        "green": "Healthy - No action needed"
    },
    "apple": {
        "brown": "Apple Scab - Apply sulfur spray in spring",
        "yellow": "Chlorosis - Check soil pH, apply iron supplement",
        "white": "Powdery Mildew - Prune for airflow, apply fungicide",
        "green": "Healthy - No action needed"
    },
    "banana": {
        "brown": "Banana Leaf Spot - Apply copper oxychloride",
        "yellow": "Mosaic Virus - Remove infected plants immediately",
        "white": "Curl Mite damage - Apply miticide spray",
        "green": "Healthy - No action needed"
    }
}

plant_list = ["tomato", "potato", "grape", "apple", "banana"]
color_list = ["green", "yellow", "brown", "white"]


def predict(plant_name, leaf_color):
    plant = plant_name.lower().strip()
    color = leaf_color.lower().strip()
    if plant in disease_db and color in disease_db[plant]:
        return disease_db[plant][color]
    return "No match found. Try a different plant or color."


def detect_dominant_color(image_path):
    """Read an image and return the dominant color name."""
    img = cv2.imread(image_path)
    if img is None:
        return "unknown"
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h = np.mean(hsv[:, :, 0])
    s = np.mean(hsv[:, :, 1])
    v = np.mean(hsv[:, :, 2])
    if s < 40:
        return "white"
    if 40 <= h < 70:
        return "yellow"
    if 70 <= h < 170:
        return "green"
    if 5 <= h < 40:
        return "brown"
    return "green"


def chat_response(message):
    """Parse a chat message and return a response."""
    msg = message.lower().strip()
    plant_found = None
    color_found = None
    for p in plant_list:
        if p in msg:
            plant_found = p
    for c in color_list:
        if c in msg:
            color_found = c
    if plant_found and color_found:
        return predict(plant_found, color_found)
    elif plant_found:
        return f"Tell me the leaf color of your {plant_found} (green, yellow, brown, or white)."
    elif color_found:
        return f"Which plant has the {color_found} leaf? (tomato, potato, grape, apple, banana)"
    else:
        return "Ask me about a plant! Example: 'What is wrong with my brown tomato leaf?'"   