#  Clinical AI Safety Audit: Cardiology LLMs
**Author:** [Rama Ala Eddein Akram Shaheen] | 3rd year Medical Student (GPA 3.9/4.2)

# Project Overview
This repository contains a clinical audit and a Python based validation layer designed to evaluate Med-PaLM 3  and GPT-4o interpretations of ECG rhythms. The primary focus is mitigating the Silent P-Wave Trap in automated diagnostics.

##  Technical Solution: The Validation Layer
Instead of relying on visual patterns alone I implemented a statistical auditor in `cardio.py` using `NeuroKit2`
- Metric used: SDNN (Standard Deviation of NN intervals) 
- Logic: High regularity (low SDNN) contradicts an AFib diagnosis (even if P-waves are absent) flagging potential AI hallucinations

##  Repository Contents
- `cardio.py`: Python script for signal processing and rhythm validation
- `Audit_Report.pdf`: (Make sure to upload your PDF file here) Detailed benchmarking and clinical findings


Aligned with Good Clinical Practice (GCP) for Digital Health applications
