from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import numpy as np
from skimage.filters import sobel
from skimage.measure import shannon_entropy

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def extract_features_from_image(file_bytes):
    img = Image.open(io.BytesIO(file_bytes)).convert('L')
    img_np = np.array(img)

    mean_pixel = np.mean(img_np)
    std_pixel = np.std(img_np)
    entropy = shannon_entropy(img_np)
    edges = sobel(img_np)
    edge_density = np.mean(edges)
    h, w = img_np.shape
    ch, cw = h // 4, w // 4
    center = img_np[h//2 - ch//2:h//2 + ch//2, w//2 - cw//2:w//2 + cw//2]
    center_brightness = np.mean(center)

    return [mean_pixel, std_pixel, entropy, edge_density, center_brightness]


def simple_rule_based_classifier(features):
    mean_pixel, std_pixel, entropy, edge_density, center_brightness = features

    if entropy > 5.5 and edge_density > 0.05:
        return "Moderate Demented"
    elif entropy > 4.5:
        return "Mild Demented"
    elif entropy > 3:
        return "Very Mild Demented"
    else:
        return "Non Demented"


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if file.content_type not in ["image/png", "image/jpeg", "image/jpg"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    bytes_data = await file.read()

    try:
        features = extract_features_from_image(bytes_data)
        label = simple_rule_based_classifier(features)

        return {"label": label}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {e}")
