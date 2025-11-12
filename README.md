# 🌐 Image Recapture Detection

## 💡 Introduction

This project studies how to tell if an image is **original** or a **recaptured photo**.
A recaptured image is a photo taken of a **digital screen** such as a **laptop, tablet, or smartphone**.
The goal is to detect small visual clues that show whether an image was taken from a screen or is an original digital file.

---

## 🔍 What is Recapture Detection

Recapture detection helps computers find out if a photo was taken from another screen.
When a person takes a picture of a monitor, tiny marks appear because of **screen pixels**, **light reflections**, or **camera focus**.
These small changes help identify a recaptured image.

---

## 🔒 Why It Is Important

1️⃣ Helps prevent the stealing of important digital data.
2️⃣ Useful in finding **fake screenshots** or **fake ID photos**.
3️⃣ Supports **digital security** and **forensic investigations**.

---

## 📚 Papers Studied

Before building the models, six main research papers were reviewed.
Each used different ideas like **chromaticity maps**, **adversarial learning**, and **attention networks**.
These papers helped decide the right direction for this project.

### Main Ideas from the Papers

✨ Studying how colors change when screens are photographed.
✨ Using neural networks that can tell clean and recaptured images apart.
✨ Observing light reflections and pixel patterns.
✨ Mixing local and global details for better results.

---

## 🧠 Technical Words Explained

🎞 **Moiré Pattern** – Wavy lines that appear when a screen is photographed.

🎨 **Color Artifacts** – Unnatural colors near edges in screen photos.

🔊 **Fourier Transform** – Looks at frequency patterns in an image.

✂️ **Laplacian Filter** – Highlights edges and small details.

🔁 **Transfer Learning** – Using a pre-trained model to improve accuracy and save time.

---

## ⚙️ Method Used

### 🔸 Step 1: Image Feature Extraction

Two image processing methods were used:

📈 **Fourier Transform**

* Changes the image into frequency form.
* Finds repeating patterns like moiré lines.

🧩 **Laplacian Filter**

* Detects edges and fine details.
* Helps find blur and unnatural sharpness from screen photos.

---

### 🔸 Step 2: Custom CNN Model

A simple **Convolutional Neural Network (CNN)** was built to classify images as *original* or *recaptured*.
It includes:

* Four convolution layers
* Global average pooling
* Batch normalization
* Dropout for regularization
* Dense output layer with sigmoid activation

This model is lightweight and easy to train on medium datasets.

---

### 🔸 Step 3: Transfer Learning Models

Two advanced models were also used to improve accuracy.

📱 **MobileNetV2**

* Fast and small model.
* Works well with limited data.
* Suitable for real-world mobile applications.

⚡ **EfficientNet**

* High accuracy with fewer parameters.
* Keeps fine image textures.
* Great for detailed recapture detection tasks.

---

## 🧪 Experiments Conducted

Eleven experiments were done using different models, datasets, and preprocessing combinations:

1️⃣ Basic image analysis and preprocessing

2️⃣ CNN on Fourier images

3️⃣ MobileNetV2 on Fourier images

4️⃣ MobileNetV2 on Laplacian images

5️⃣ MobileNetV2 on both Fourier and Laplacian images

6️⃣ MobileNetV2 on RGB (normal) images

7️⃣ EfficientNet on RGB images

8️⃣ EfficientNet on both Laplacian and RGB images

9️⃣ RGB-EfficientNetB0-Laplacian (Roselab + Android-captured)

🔟 RGB-EfficientNetB0 (Roselab + Android-captured)

1️⃣1️⃣ RGB-EfficientNetB0 (NTU-Android x8) + Testing on iPhone

---

## 📊 Results

🥇 **RGB-EfficientNetB0 (NTU-Android x8) + iPhone test** — **92% Accuracy**  
⭐ New best model with excellent balance and real-world generalization  
⭐ Precision 0.92 | Recall 0.92 | F1 0.92  
⭐ Works reliably on both Android-captured and iPhone test images  

🥈 **RGB + Laplacian EfficientNetB0** — 90% Accuracy  
⭐ Best overall model with balanced precision and recall  
⭐ Combines both RGB and Laplacian image inputs  
⭐ High accuracy but uses more parameters (8.4M)

🥉 **RGB EfficientNetB0** — 87.7% Accuracy  
⭐ Strong single-stream model using only RGB images  
⭐ Balanced performance and lower complexity

4️⃣ **RGB MobileNetV2** — 85.7% Accuracy  
⭐ Very lightweight model  
⭐ Ideal for mobile or real-time use

5️⃣ **Laplacian MobileNetV2** — 84.6% Accuracy  
⭐ Uses only edge information  
⭐ Most efficient model for low-resource systems

🚀 Live Demo
Try it here: https://huggingface.co/spaces/UzerDeveloper07/screen-recapture-detection
