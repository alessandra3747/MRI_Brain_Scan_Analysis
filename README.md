# 🧠 MRI Brain Scan Analysis with Python, FastAPI, React & Power BI

This full-stack project provides a complete solution for analyzing MRI brain scans related to Alzheimer’s disease. It integrates:

- 🧮 A **Python pipeline** for feature extraction from MRI images  
- 🚀 A **FastAPI backend** for real-time predictions  
- 🌐 A **React frontend** for user interaction  
- 📊 A **Power BI dashboard** for data storytelling and insights  

---

## 📌 Project Overview

This solution was built using multiclass MRI datasets labeled as:
- `NonDemented`  
- `VeryMildDemented`  
- `MildDemented`  
- `ModerateDemented`  

Key components of the project:

- Raw `.zip` image datasets are processed directly in Python
- Extracted image features include:
  - Mean pixel intensity  
  - Standard deviation  
  - Shannon entropy  
  - Edge density (Sobel filter)  
  - Center brightness  
- Features are saved into a clean, labeled `.csv` file
- A rule-based classifier simulates diagnostic logic
- Power BI dashboard allows for deep visual exploration
- FastAPI backend processes new scans for classification
- Frontend enables drag-and-drop uploads and live prediction

---

## 🧪 Technologies Used

### 🌐 Frontend
- **Vite** – modern web bundler for fast development  
- **React** – interactive user interface  
- **TypeScript** – type-safe frontend logic  
- **Tailwind CSS** – utility-first styling  
- **Axios** – sending image data to backend  
- **CORS** – middleware support for cross-origin requests  

### 🧪 Backend
- **Python 3.8+** – backend language  
- **FastAPI** – fast, modern API framework  
- **Uvicorn** – ASGI web server  
- **Pillow (PIL)** – for image processing  
- **NumPy** – for array-based calculations  
- **scikit-image** – edge detection, entropy, filters  
- **tqdm** – progress bars for batch processing  
- **CORS Middleware** – to enable frontend-backend communication  

### 📊 Dashboard & Data
- **Power BI** – interactive business intelligence dashboard  
- **Excel** – used to preview and clean `.csv` files  
- **Pandas** – for tabular data handling  
- **CSV** – exported image features for BI analysis  

---

## 📁 Datasets

The project uses publicly available MRI datasets:

- [🧠 Augmented Alzheimer MRI Dataset](https://www.kaggle.com/datasets/uraninjo/augmented-alzheimer-mri-dataset)  
- [🧠 Multiclass Alzheimer Dataset (equal & augmented)](https://www.kaggle.com/datasets/aryansinghal10/alzheimers-multiclass-dataset-equal-and-augmented)  

These contain thousands of MRI images labeled according to dementia severity.

---

## ⚙️ Application Workflow

1. **Python Pipeline**  
   - Loads and processes `.zip` files of MRI images  
   - Extracts image-based features  
   - Saves results into `.csv`  

2. **FastAPI Server**  
   - Accepts `.jpg`, `.jpeg`, `.png` uploads  
   - Processes and classifies images  
   - Returns predicted dementia level  

3. **React Frontend**  
   - Users drag-and-drop brain scan images  
   - Frontend sends file to API  
   - Displays prediction and confidence  

4. **Power BI Dashboard**  
   - Visualizes the distribution of extracted features  
   - Highlights class imbalances, patterns, and augmentation  
   - Interactive filters for deeper analysis  

---

## 📈 Dashboard Highlights

The Power BI dashboard includes:

- 📊 Dementia class distribution  
- 🧮 Feature comparison across classes  
- 🔍 Augmentation detection  
- 🎛️ Interactive filters for image types and categories  

Designed for technical and non-technical audiences in the healthcare field.

---

## 🎯 Project Goals

This project demonstrates skills in:

- 🧠 Processing medical imaging data at scale  
- 🧬 Extracting structured data from raw `.jpg` inputs  
- 🛠️ Building a clean and maintainable backend in FastAPI  
- 🌍 Integrating a modern React-based frontend  
- 📊 Communicating insights via interactive dashboards in Power BI  
- 🔗 Bridging ML, backend, and BI into one cohesive solution  

---

## 📸 Preview

![Preview](images/preview.png)
![Preview](images/previewApp.png)
---

## 🚀 Run Locally

### Run RunAppService.bat file and in a browser go to -> http://localhost:5173/

### Backend (FastAPI) and Frontend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload

cd frontend
npm install
npm run dev

