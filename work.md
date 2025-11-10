
---

## 🧰 How to Use

All code is written in **Google Colab**.

1️⃣ Open any notebook from the `src` folder.
2️⃣ Install the required libraries listed in `requirements.txt`.
3️⃣ Run all the cells to train and test the models.

---

## 🎓 Credits

**Faculty of Science and Engineering**

**Information Systems — Bernoulli Institute**

**Master’s Thesis by:**
👨‍🎓 **Uzer Ahmed**

**Affiliations:**
🏛 **PRISMA Research Lab, University of Groningen, The Netherlands**

🏛 **Department of Electrical EngineeringFmt and Information Technology, University of Naples Federico II, Italy**

**Supervisors:**
👨‍🏫 **Prof. George Azzopardi** — University of Groningen, The Netherlands

👨‍🏫 **Dr. Guru Swaroop Bennabhatkula** — University of Groningen, The Netherlands

---

This project focuses only on **images taken from digital screens** such as **laptops, smartphones, and tablets** — not from paper or printed copies.

-------------------------------------------------------------------------------------------

1. **Image-Analysis (Stage-1)**  
   Performed initial exploratory data analysis on NTU-Roselab dataset.  
   Visualized originals vs recaptures using histograms, edges, and frequency domain.

2. **Fourier CNN Model**  
   Applied 2D FFT to images and trained a custom CNN on magnitude spectrum.  
   Aimed to detect moiré patterns typical in screen recaptures.

3. **Fourier-MobileNetV2**  
   Preprocessed images with FFT and fed log-magnitude to MobileNetV2.  
   Lightweight model for frequency-based recapture detection.

4. **Laplacian-MobileNetV2**  
   Enhanced edge information using Laplacian filter before MobileNetV2.  
   Focused on sharpness differences between original and recaptured images.

5. **FFT & Laplacian-MobileNetV2**  
   Combined FFT (frequency) and Laplacian (edges) as 2-channel input.  
   Multi-domain feature fusion for improved recapture classification.

6. **RGB-MobileNetV2**  
   Trained MobileNetV2 directly on raw RGB images (no preprocessing).  
   Baseline spatial-domain model using transfer learning.

7. **RGB-EfficientNetB0**  
   Used EfficientNetB0 on RGB input for higher accuracy and efficiency.  
   Stronger backbone for learning complex visual patterns.

8. **RGB-EfficientNetB0-Laplacian**  
   Concatenated RGB and Laplacian channels (4-channel input).  
   Hybrid model leveraging both color and edge sharpness cues.

9. **RGB-EfficientNetB0-Laplacian (Roselab + Android-captured)**  
   Merged NTU-Roselab with real Android-captured recaptures. Laplacian filter was applied but did not improve performance significantly.

10. **RGB-EfficientNetB0 (Roselab + Android-captured)**  
    Trained on merged dataset using only RGB (removed Laplacian). Model showed bias toward NTU-Roselab images. ~82% val accuracy.

11. **RGB-EfficientNetB0 (NTU-Android x8) + iPhone testing**  
    Multiplied Android-captured images by 8 (1600 total) to balance NTU-Roselab (2400). Trained on RGB only. Excellent generalization; tested successfully on unseen iPhone recaptures. Achieved 92% accuracy.