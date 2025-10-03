**Plant Leaf Disease Detection using Machine Learning**

**Project Description**

This project focuses on detecting plant leaf diseases using Convolutional Neural Networks (CNN).  
The system is trained on a dataset of plant leaf images and can classify whether a leaf is healthy or affected by specific diseases.  
It also provides a simple GUI for testing and predicting results.

**Dataset Preparation**
1. Create a folder named `dataset`.  
2. Inside `dataset`, create two subfolders:  
   - `train`  
   - `test`  
3. Download images from [Plant Disease Dataset (Kaggle)](https://www.kaggle.com/datasets/emmarex/plantdisease).  
4. Collect at least **50 images for each disease class** and arrange them into separate folders for each category:  
   - Apple Black Rot  
   - Apple Scab  
   - Cedar Apple Rust  
   - Grape Black Rot  
   - Healthy  
   - Potato Early Blight  
   - Potato Late Blight  
   - Strawberry Leaf Scorch  
   - Tomato Septoria Leaf Spot  
   - Tomato Yellow Leaf Curl Virus

Your folder structure should look like this:  

```text
dataset/
├── train/
│   ├── Apple Black Rot/
│   ├── Apple Scab/
│   ├── Cedar Apple Rust/
│   ├── Grape Black Rot/
│   ├── Healthy/
│   ├── Potato Early Blight/
│   ├── Potato Late Blight/
│   ├── Strawberry Leaf Scorch/
│   ├── Tomato Septoria Leaf Spot/
│   ├── Tomato Yellow Leaf Curl Virus/
│
└── test/
    ├── Apple Black Rot/
    ├── Apple Scab/
    ├── Cedar Apple Rust/
    ├── Grape Black Rot/
    ├── Healthy/
    ├── Potato Early Blight/
    ├── Potato Late Blight/
    ├── Strawberry Leaf Scorch/
    ├── Tomato Septoria Leaf Spot/
    ├── Tomato Yellow Leaf Curl Virus/

```
**How to Run**

**1. Download or clone this repository:**
   git clone https://github.com/Ambikau26/Plant-Leaf-Disease-Detection.git
   
   cd Plant-Leaf-Disease-Detection
   
**2. Install required dependencies:** pip install -r requirements.txt

**3. Train the model:** python Training3.py

**4. Test the model:** python Testing3.py

**5. Run the GUI for predictions:** python GUICNN3.py

**Technologies Used**
- Python
- TensorFlow / Keras
- Tkinter (for GUI)
- CNN model

**Features**
- Train and test CNN model for plant disease classification
- Predict disease from uploaded leaf images
- GUI-based interface for easy interaction

**Future Enhancements**
- Increase dataset size for better accuracy
- Add more plant disease categories
- Deploy model as a web or mobile application
