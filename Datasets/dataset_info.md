# 📸 NTU-Roselab Dataset

## 🧾 Overview

The **NTU-Roselab Dataset** is used in this project to train and test models for **image recapture detection**.
It includes both **original natural images** and **recaptured images** that were taken from digital screens such as monitors.

The dataset contains around **1200 original images** and **1700 recaptured images**, with a total size of **about 17 GB**.
Most images are in **JPG** format, with a few in **BMP** format.
Image resolutions range between **2272×1704** and **4256×2832** pixels.

---

## 📷 Original Images

The **1200 natural (original)** images were taken using **five camera brands** — *Canon, Casio, Lumix, Nikon,* and *Sony.*
These are organized into different folders based on camera type and environment (indoor/outdoor).

### 📁 Categories

zCanon10D1, zCanon10D2, zCanon400D1, zCanon400D2,
zCanonIxusIndoor, zCanonIxusOutdoor, zCasioIndoor, zCasioOutdoor,
zLumixD1Indoor, zLumixD1Outdoor, zNikonD70D1, zNikonD70D2,
zNikonS210, zNikonS210D2, zSonyAlpha, zSonyIndoor, zSonyOutdoor

---

## 🔁 Recaptured Images

The **2700 recaptured** images were created by photographing screens that displayed other images.
The sources include:

* 100 images captured directly by available cameras
* 100 images downloaded from Flickr
* 100 *tampered* images where around **10% of the content was modified**

Each group of 300 images was captured using a combination of different **cameras** and **LCD screens**.

### 🖼️ Camera–Screen Combinations

* Canon Powershot A620 + Philips 19” 190B6CG LCD
* Canon Powershot A620 + NEC 17” AccuSync LCD
* Canon Powershot A620 + Acer 17” AL712 LCD
* Olympus Mju 300 + Philips 19” 190B6CG LCD
* Olympus Mju 300 + NEC 17” AccuSync LCD
* Olympus Mju 300 + Acer 17” AL712 LCD
* Olympus E500 + Philips 19” 190B6CG LCD
* Olympus E500 + NEC 17” AccuSync LCD
* Olympus E500 + Acer 17” AL712 LCD

---

## 🗂️ Folder Structure

Each recaptured group (CanonAcer, MjuAcer, OlymAcer, etc.) contains three main subfolders:

📁 **Download** – Images taken from the Flickr dataset
📁 **OurPhoto** – Original photos recaptured from cameras
📁 **Tampered** – Images where a small area was digitally changed before recapture

Example folder structure:

```
CanonAcer/
 ├── Download/
 ├── OurPhoto/
 └── Tampered/

MjuNEC/
 ├── Download/
 ├── OurPhoto/
 └── Tampered/
```

---

## ⚖️ Dataset Balancing

Out of **2900 total images**,

* **1200** are **original**,
* **1700** are **recaptured**.

To make the dataset **balanced**, about **500 recaptured images** were removed, keeping equal numbers for fair training.

---

## 🧩 Notes

✔️ Dataset focuses only on **screen recaptures** from laptops, monitors, or smartphones,
and You can make a request for the dataset
---

💾 **Total Size:** ~17 GB
🖼️ **Formats:** JPG, BMP
📸 **Used For:** Image Recapture Detection (Monitor-based)
🏷️ **Source:** NTU-Roselab Dataset

---

*More datasets may be added in the future, and this README will be updated accordingly.*
