# Assignment 2: Case Studies with Programming Problems

**Unit:** Software Technology 1 (4483/8995)  
**Student ID:** U3243935  
**Due:** Week 8 Friday 11:59 PM  
**Total Marks:** 30

---

## Repository Structure

| Folder | Case Study | Week | Topic | Files |
|--------|-----------|------|-------|-------|
| `case_study_1/` | Case Study 1 | Week 4 | Python Tkinter & Pillow | 6 scripts |
| `case_study_2/` | Case Study 2 | Week 5 | NumPy & OpenCV | 20 scripts |
| `case_study_3/` | Case Study 3 | Week 6 | Keras, Matplotlib & Google Colab | 7 scripts |
| `case_study_4/` | Case Study 4 | Week 7 | MobileNetV2 Image Classifier (Colab) | 1 notebook |
| `case_study_5/` | Case Study 5 | Week 8 | MobileNet + EfficientNet + ViT (Colab) | 1 notebook |

---

## Case Study 1 — Pillow Image Manipulation (Week 4)

Run each script from inside `case_study_1/`. Requires an `Assets/Insects/` folder with insect images.

```bash
pip install Pillow
python intro.py
python manipulate.py
python explore_colors.py
python enhance.py
python image_filter.py
python image_operations.py
```

---

## Case Study 2 — NumPy & OpenCV (Week 5)

Run each script from inside `case_study_2/`. Requires an `Assets/Insects/` folder with insect images.

```bash
pip install numpy opencv-python
python task1_1.py   # through task1_10.py  (NumPy tasks)
python task2_1.py   # through task2_10.py  (OpenCV tasks)
```

---

## Case Study 3 — Keras & Matplotlib (Week 6)

Run each script from inside `case_study_3/`. Requires an `Assets/Insects/` folder with insect images.

```bash
pip install tensorflow matplotlib
python task1_1.py   # through task1_7.py
```

---

## Case Study 4 — MobileNetV2 Stream Macroinvertebrate Classifier (Week 7)

Open `ST1_Week7_MobileNetV2_Classifier.ipynb` in **Google Colab** (GPU runtime required).

Steps before running:
1. Mount Google Drive
2. Download the [Stream Macroinvertebrates dataset from Kaggle](https://www.kaggle.com/datasets/kennethtm/stream-macroinvertebrates/data)
3. Create `Assets/insects_dataset/train_data/` and `Assets/insects_dataset/test_data/` with 3 species

---

## Case Study 5 — MobileNet + EfficientNet + ViT Classifier (Week 8)

Open `ST1_Week8_MultiModel_Classifier.ipynb` in **Google Colab** (GPU runtime required).

Compares three transfer learning models:
- MobileNetV2
- EfficientNetB0 (with optional fine-tuning)
- Vision Transformer (ViT) via keras-cv

Uses the same dataset structure as Week 7.

---

## Dependencies Summary

| Package | Used In |
|---------|---------|
| `Pillow` | CS1 |
| `numpy` | CS2, CS3 |
| `opencv-python` | CS2 |
| `tensorflow` | CS3, CS4, CS5 |
| `matplotlib` | CS3, CS4, CS5 |
| `scikit-learn` | CS4, CS5 |
| `keras-cv` | CS5 (ViT) |
