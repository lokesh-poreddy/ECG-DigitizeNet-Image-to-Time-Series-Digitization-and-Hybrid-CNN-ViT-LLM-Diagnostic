# doctor_lokitrix.py
# Lightweight clinical text generator.

LEADS = ['I','II','III','aVR','aVL','aVF','V1','V2','V3','V4','V5','V6']

class DoctorLokitrixLLM:
    def __init__(self):
        self.abnormality_map = {
            0: "Normal Sinus Rhythm",
            1: "Atrial Fibrillation",
            2: "Left Bundle Branch Block",
            3: "Right Bundle Branch Block",
            4: "Myocardial Infarction Pattern",
            5: "ST-Segment Elevation",
            6: "ST-Segment Depression"
        }

    def generate(self, prediction_class, confidence, signals):
        return "Doctor Lokitrix report text placeholder."
