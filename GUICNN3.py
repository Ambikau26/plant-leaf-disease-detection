import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import *
from PIL import ImageTk, Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import pyttsx3
#pip install pyttsx3
#initialize the TTS engine


# Initialize tkinter window
np.set_printoptions(suppress=True)
top = tk.Tk()
top.geometry('1000x1000')
top.title('Plant Leaf Disease Detection')
img = PhotoImage(file='wallpaper1.png', master=top)
img_label= Label(top,image=img)
img_label.place(x=0, y=0)

engine = pyttsx3.init()
#set properties
engine.setProperty('rate', 150) #speed of speech
engine.setProperty('volume', 4.0) #volume

# Remedy dictionary (you can expand this as needed)
remedies = {
    "Apple Scab": "Remove infected leaves and avoid overhead watering.",
    "Apple Black Rot": "Remove infected plant parts and disinfect tools after use.",
    "Cedar Apple Rust": "Prune infected branches and use fungicides.",
    "Healthy": "No treatment required, your plant is healthy.",
    "Tomato Yellow Leaf Curl Virus": "Remove infected plants, and avoid pest exposure.",
    "Grape Black Rot": "Prune and remove infected parts, and apply fungicides.",
    "Potato Early Blight": "Remove affected leaves and apply copper-based fungicides.",
    "Potato Late Blight": "Use resistant varieties and fungicides, and ensure good drainage.",
    "Strawberry Leaf Scorch": "Remove infected leaves and improve air circulation.",
    "Tomato Septoria leaf spot": "Prune affected leaves, avoid overhead watering, and use fungicides."
}

# Function to classify and show remedies
def classify(file_path):
    try:
        model = tf.keras.models.load_model('keras_Model.h5')
    except Exception as e:
        messagebox.showerror("Error", "Error loading model: " + str(e))
        return

    try:
        # Load label names
        with open('labels.txt', 'r') as f:
            label_names = f.read().splitlines()

        # Load and preprocess the image
        img = image.load_img(file_path, target_size=(150, 150))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = x / 255.0

        # Predict the class
        predictions = model.predict(x)
        class_index = np.argmax(predictions[0])
        class_name_predicted = label_names[class_index]

        # Check if the plant is healthy or not
        if class_name_predicted == "Healthy":
            status = "Healthy"
            status_color = "white"  # Healthy = white color
            remedy = remedies["Healthy"]
        else:
            status = "Unhealthy"
            status_color = "white"  # Unhealthy = white color
            remedy = remedies.get(class_name_predicted, "No remedy available.")

        # Display predicted status, disease name, and remedy
        status_label.configure(foreground=status_color, text=f"Status: {status}")
        label.configure(foreground="white", text=f"Disease: {class_name_predicted}")
        messagebox.showinfo("Prediction Result", f"Predicted Disease: {class_name_predicted}\nRemedy: {remedy}")

        # Update the remedy label with the remedy information
        remedy_label.configure(foreground="white", text=f"Remedy: {remedy}")
        remedy_label.place(relx=0.5, rely=0.70, anchor="center")  # Adjusted placement


    except Exception as e:
        messagebox.showerror("Error", "Error during classification: " + str(e))

    # say something
    engine.say("Detected disease is:"+class_name_predicted)
    # run the speech
    engine.runAndWait()

# Show classify button after image is uploaded
def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=20, pady=10)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 12, 'bold'), relief=SOLID, bd=2)
    classify_b.place(relx=0.79, rely=0.46)


# Upload image function
def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        if not file_path.lower().endswith(('.png', '.jpg', '.jpeg')):  # Only allow valid image formats
            messagebox.showerror("Invalid File", "Please upload a valid image file (jpg, jpeg, png).")
            return

        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))  # Resize for the window
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')  # Clear previous class prediction
        remedy_label.configure(text='')  # Clear remedy label
        status_label.configure(text='')  # Clear status label
        show_classify_button(file_path)
    except Exception as e:
        messagebox.showerror("Error", "Error uploading image: " + str(e))



# Heading label with larger and bolder font
heading = Label(top, text="Plant Leaf Disease Detection", pady=20, font=('arial', 24, 'bold'))
heading.configure(background='black', foreground='white')
heading.pack()

# Display the uploaded image with rounded corners effect
sign_image = Label(top, background='#007f0e')
sign_image.pack(side=BOTTOM, expand=True)

# Label to show the plant health status (Healthy/Unhealthy) with improved styling
status_label = Label(top, font=('arial', 14, 'italic'), background='#007f0e')
status_label.place(relx=0.5, rely=0.36, anchor="center")  # Status label placed above disease name

# Label to show the predicted class (disease name) with improved styling
label = Label(top, font=('arial', 14, 'bold'), background='#007f0e')
label.place(relx=0.5, rely=0.40, anchor="center")  # Disease name label placed below the status

# Remedy label with improved styling, transparent background, and centered
remedy_label = Label(top, font=('arial', 14, 'italic'), background='#007f0e')
remedy_label.place(relx=0.5, rely=0.46,  anchor="center")  # Placed below disease name

# Upload button with improved design and hover effect
upload = Button(top, text="Upload Image", padx=20, pady=10)
upload.configure(background='#364156', foreground='white', command=upload_image, font=('arial', 14, 'bold'), relief=SOLID, bd=2)
upload.pack(side=BOTTOM, pady=50)

top.mainloop()