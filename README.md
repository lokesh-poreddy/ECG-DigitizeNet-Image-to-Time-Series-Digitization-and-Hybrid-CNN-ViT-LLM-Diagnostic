# ECG-DigitizeNet
Image-to-Time-Series Digitization and Hybrid CNN–ViT–LLM Diagnostic System.
ECG-DigitizeNet is an end-to-end AI pipeline designed to transform raw 12-lead 
ECG images into clinically usable digital signals and automated diagnostic 
interpretations. The system consists of three major components:

1. **ECG Signal Extractor** – A robust image-processing engine that digitizes 
   ECG paper images into clean 12-lead time-series data using adaptive 
   normalization, morphological grid removal, skeletonization, and 
   centroid-based waveform tracing.

2. **Hybrid CNN–ViT Classifier** – A lightweight yet powerful deep-learning 
   architecture combining Convolutional Neural Networks with a 
   Vision Transformer–style encoder for multi-class cardiac rhythm 
   classification.

3. **Doctor Lokitrix LLM** – A domain-tuned lightweight medical text generator 
   that produces structured clinical reports, including condition explanation, 
   lead-wise observations, and final cardiology interpretation.

ECG-DigitizeNet is optimized for Kaggle, research workflows, and medical AI 
prototyping, and includes a pretrained model, modular source code, and a ready-to-run 
inference pipeline.


## Features:
- Convert ECG images to 12-lead time-series.
- Hybrid CNN + Transformer classifier.
- Doctor Lokitrix LLM clinical interpretation.
## Structure:
```
ECG-DigitizeNet/
│
├── src/
│   ├── signal_extractor.py
│   ├── model_cnn_vit.py
│   ├── doctor_lokitrix.py
│   ├── pipeline_inference.py
│
├── notebooks/
│   └── ECG_DigitizeNet_Kaggle.ipynb
│
├── models/
│   └── hybrid_model_best.pt
│
├── examples/
│   └── sample_report.txt
│
├── data/
│   └── README.md
│
├── README.md
└── LICENSE

```
## Author:
- Lokesh Reddy Poreddy
GitHub: https://github.com/lokesh-poreddy
