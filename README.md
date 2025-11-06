# Image Recapture Detection

--> Introduction

This project is about finding if an image is original or a recaptured one. A recaptured image means a photo taken of a digital screen like a laptop, tablet, or smartphone. The aim is to detect small clues that show if the picture was taken from a screen and not directly from a digital file.

--> What is Recapture Detection

Recapture detection helps us understand if a photo was taken from another screen. When someone takes a photo of a monitor, small visual marks appear because of screen pixels, reflections, or lighting. These clues can be used by computers to know if an image is real or recaptured.

--> Why It Is Important

1. It helps stop stealing of important digital information.
2. It can be used to find fake ID photos or fake screenshots.
3. It helps in digital security and forensic work.

--> Papers Studied

Before building the model, six main research papers were studied. Each one used different ideas like chromaticity maps, adversarial learning, and attention networks. These papers helped understand what works best for this problem.

Some main ideas from the papers:

- Looking at color changes that happen when screens are photographed.
- Using special networks to separate clean images from recaptured ones.
- Using physical light reflections to find screen images.
- Mixing local and global image details for better prediction.

--> Technical Words Explained

- Moiré Pattern: Strange wavy lines that appear when taking a photo of a screen.
- Color Artifacts: Weird colors around edges in photos of screens.
- Fourier Transform: A way to look at images using their frequency details.
- Laplacian Filter: Finds sharp edges in an image.
- Transfer Learning: Using a pre-trained model to save time and improve results.

--> Method Used

--># Step 1: Image Feature Extraction

Two main image processing techniques were used:

Fourier Transform

- Changes the image into frequency space.
- Helps find patterns like moiré lines.

Laplacian Filter

- Finds edges and small details.
- Helps detect blur and unnatural sharpness from screens.

--># Step 2: Custom CNN Model

A small CNN model was created for classification. It has four convolution layers, followed by pooling, batch normalization, dropout, and finally a dense layer with sigmoid output. It predicts if an image is original or recaptured.

--># Step 3: Using Transfer Learning

Two advanced models, MobileNetV2 and EfficientNet, were also tested.

MobileNetV2

- Small and fast model.
- Works well even with less data.

EfficientNet

- Gives high accuracy with fewer parameters.
- Keeps fine details that help detect screen artifacts.

--> Experiments

Eight experiments were done using different image types and model combinations:

1. Normal image analysis and cleaning
2. CNN on Fourier images
3. MobileNetV2 on Fourier images
4. MobileNetV2 on Laplacian images
5. MobileNetV2 on both Fourier and Laplacian images
6. MobileNetV2 on RGB (normal) images
7. EfficientNet on RGB images
8. EfficientNet Two Models on Laplacian images and RGB

--> Results

The best result came from the model that used both Fourier and Laplacian processed images with MobileNetV2. It reached around 94% accuracy. This shows that mixing traditional image filters with modern deep learning gives very good results.

--> How to Use

All the code is written in Google Colab.

1. Open any notebook from the `src` folder.
2. Install the libraries given in `requirements.txt`.
3. Run all the cells to train and test the model.

--> Credits

Faculty of Science and Engineering
Information Systems — Bernoulli Institute

Master's Thesis
UZER AHMED

Affiliation:
PRISMA Research Lab, University of Groningen, The Netherlands
Department of Electrical Engineering and Information Technology [Note: Adjust if different], Federico II University of Naples, Italy

Thesis Supervisors:

1. Prof. George Azzopardi (Primary Supervisor)
   University of Groningen, The Netherlands

2. Dr. Guru Swaroop Bennabhatkula (Co-Supervisor)
   University of Groningen, The Netherlands

This project is focused only on images taken from digital screens like laptops, smartphones, and tablets — not from paper or printed copies.
