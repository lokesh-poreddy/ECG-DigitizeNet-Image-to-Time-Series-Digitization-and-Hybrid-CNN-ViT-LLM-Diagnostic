# ECG-DigitizeNet
Image-to-Time-Series Digitization and Hybrid CNN–ViT–LLM Diagnostic System.
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
