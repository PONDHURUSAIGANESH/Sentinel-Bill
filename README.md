## A simple bank note authentication application
 ## **Bank Note Authentication**

**A machine learning application that accurately identifies authentic banknotes using image-based features and a Random Forest Classifier.**

## Overview

This application effectively detects forged banknotes by analyzing key image features:

- Variance
- Skewness
- Kurtosis
- Entropy

It employs a Random Forest Classifier to classify banknotes as either authentic or forged.

## Dataset

- Source: UCI Machine Learning Repository
- Features:
    - Variance of Wavelet Transformed image
    - Skewness of Wavelet Transformed image
    - Kurtosis of Wavelet Transformed image
    - Entropy of image
- Target variable: Class (0 for authentic, 1 for forged)

## Image Preprocessing

- Images captured using an industrial camera with 400x400 pixels and 660 dpi resolution.
- Grayscale conversion for feature extraction.
- Wavelet Transform applied for feature extraction.

## Model

- Random Forest Classifier chosen for its robustness and accuracy.
- Trained and validated using appropriate dataset splits.

## Usage

**Prerequisites:**

- Python 3.x
- Required libraries: pandas, NumPy, scikit-learn

**To run:**

1. Clone this repository.
2. Navigate to the project directory.
3. Execute the `New.py` file (or equivalent).

## Contributing

Feel free to contribute to this project by:

- Reporting issues or suggesting improvements.
- Submitting pull requests for code enhancements.


**Additional Information:**

- Model performance metrics (accuracy, precision, recall, etc.).
- Visuals (e.g., confusion matrix, feature importance plots).
- Deployment instructions (if applicable).
- Future work or potential extensions.
