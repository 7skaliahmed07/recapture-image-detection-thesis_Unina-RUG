# 🌐 Image Recapture Detection
![image_alt](https://github.com/7skaliahmed07/recapture-image-detection-thesis_Unina-RUG/blob/52ed0ea656d6f0247302fd00a3d9f8fad3994eed/recapture.webp)


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

Thirteen experiments were conducted to systematically compare different approaches for recapture detection:

### 🔬 Stage 1: Basic Image Analysis
**1️⃣ Image-Analysis (Stage-1)**
- Used Fourier Transform and Laplacian filters
- Found that basic methods work well for smartphone recaptures but fail for professional DSLR recaptures
- **Key Finding**: Professional equipment minimizes artifacts, making detection harder

### 🔄 Stage 2: Frequency Domain Approaches
**2️⃣ Fourier CNN Model**
- Combined Fourier features with custom CNN
- **Result**: 50% accuracy - model failed to learn meaningful patterns
- **Insight**: Fourier features alone are insufficient for professional recaptures

**3️⃣ Fourier-MobileNetV2**
- Used MobileNetV2 with Fourier inputs
- **Result**: 50% accuracy - same failure pattern
- **Critical Conclusion**: Fast Fourier Transformation does not work for finely recaptured images

### 📸 Stage 3: Spatial Domain Approaches
**4️⃣ Laplacian-MobileNetV2**
- Used Laplacian sharpness features with MobileNetV2
- **Result**: 85% accuracy - first successful experiment
- **Breakthrough**: Spatial features work better than frequency features

**5️⃣ Hybrid MobileNetV2**
- Combined both Fourier and Laplacian features
- **Result**: 81% accuracy - good but not best
- **Insight**: Combination helps but has limitations

### 🎨 Stage 4: RGB-Based Approaches
**6️⃣ RGB-MobileNetV2**
- Used normal color images without special processing
- **Result**: 86% accuracy - excellent performance
- **Discovery**: Simple RGB images work very well

**7️⃣ RGB-EfficientNetB0**
- Used EfficientNetB0 with RGB images
- **Result**: 88% accuracy - new best performance
- **Advantage**: More balanced and consistent than MobileNetV2

**8️⃣ RGB + Laplacian EfficientNetB0**
- Dual-input model combining RGB and Laplacian features
- **Result**: 90% accuracy - best performance so far
- **Strength**: Perfect balance between precision and recall

### 📱 Stage 5: Multi-Device Experiments
**9️⃣ Merged Dataset with Android Photos**
- Combined NTU DSLR and Android phone images
- **Result**: Failed - model couldn't learn from mixed quality data
- **Problem**: Big quality differences between devices caused confusion

**🔟 Rebalanced Dataset with Android Oversampling**
- Added 8x oversampling of Android photos
- **Result**: 83% accuracy - successful improvement
- **Solution**: Dataset balancing enables mixed-device learning

**1️⃣1️⃣ Final Merged Model with F1 Optimization**
- Comprehensive mixed-dataset model with F1 optimization
- **Result**: 92% accuracy - best mixed-dataset performance
- **Achievement**: Proved mixed datasets can work with proper techniques

**1️⃣2️⃣ Robust 4-Device EfficientNetB0**
- Model trained for generalization across multiple devices
- Focused on cross-device compatibility

**1️⃣3️⃣ MobileNetV3 for 3 Mobile Devices**
- Specialized model for mobile-only images
- **Result**: 89% accuracy - excellent mobile performance
- **Key Insight**: Device-specific models avoid generalization problems

---

## 📊 Results Summary

### 🥇 **Top Performing Models**

**RGB-EfficientNetB0 (NTU-Android x8)** — **92% Accuracy**  
⭐ Best overall model with excellent generalization  
⭐ Perfect balance: Precision 0.92 | Recall 0.92 | F1 0.92  
⭐ Works reliably across different devices  

**RGB + Laplacian EfficientNetB0** — **90% Accuracy**  
⭐ Best dual-input model  
⭐ Combines RGB and edge information effectively  
⭐ High accuracy with good interpretability  

**MobileNetV3 (3 Mobile Devices)** — **89% Accuracy**  
⭐ Best device-specific model  
⭐ Excellent for mobile-only applications  
⭐ Avoids cross-device generalization issues  

### 🎯 **Key Findings**

1. **RGB images work better** than specialized features for professional recaptures
2. **EfficientNetB0 outperforms** MobileNetV2 for this task
3. **Device-specific models** work better than universal models
4. **Dataset balancing** is crucial for mixed-device training
5. **Fourier Transform fails** for high-quality professional recaptures

### 📈 **Performance Evolution**
- Basic methods: 50% accuracy (failed)
- Single features: 85% accuracy 
- Combined features: 90% accuracy
- Optimized models: 92% accuracy

---

## 🚀 Live Demo
Try the recapture detection system here:  
**https://huggingface.co/spaces/UzerDeveloper07/screen-recapture-detection**

The demo allows you to upload images and test whether they are original or recaptured from screens using our best-performing models.

---

## 💡 Conclusion

This research demonstrates that:
- **Simple approaches often work best** - RGB images outperform complex feature extraction
- **Device specialization matters** - Different models work best for different device types
- **Dataset quality is crucial** - Balanced, well-structured data enables better learning
- **Real-world deployment is achievable** - Models can be optimized for practical use

The project successfully identified effective strategies for recapture detection and produced models suitable for real-world security applications.
