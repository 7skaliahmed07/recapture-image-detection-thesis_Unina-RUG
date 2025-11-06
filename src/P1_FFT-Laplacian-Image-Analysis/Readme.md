 Image Analysis: Recapture Detection using Fourier and Laplacian Methods

This project explores image recapture detection using basic computer vision techniques.  
It compares professional and consumer-grade recaptured images to understand how visual artifacts differ.

---

 📁 Contents

- Google Colab Notebook  
  The Colab file contains code to:
  - Load two sample images:
    - DSLR photo from NTU-Rose Lab Dataset
    - Android photo from Custom Smartphone Dataset
  - Perform Fourier Transform Analysis  
    (to study frequency components and moiré patterns)
  - Perform Laplacian Analysis  
    (to detect edge blurring and sharpness loss)
  - Display the processed images and results

---

 🧠 Key Findings

- NTU-Rose Lab Images (Professional Recaptures)  
  - Minimal artifacts  
  - Fourier and Laplacian methods show poor detection  
  - Needs deep learning for reliable results  

- Smartphone Recaptures (Screen Photos)  
  - Clear visible artifacts (moire, blur)  
  - Fourier and Laplacian methods work very well

---

 📊 Summary

| Dataset | Recapture Type | Detection Quality | Notes |
|----------|----------------|------------------|--------|
| NTU-Rose Lab | Professional | Poor | Requires Stage-2 Deep Analysis |
| Smartphone | Consumer | Excellent | Stage-1 Analysis Sufficient |

---

 🚀 Next Steps

Future improvements will include:
- Deep learning models (CNN, ResNet)
- Advanced frequency and noise pattern analysis
- Automated classification of recaptured vs. original images

---

Stage-1 Analysis:  
✅ Consumer Recaptures  ✖️ Professional Recaptures  

Next Step: Advanced AI-based analysis for professional datasets.
```
