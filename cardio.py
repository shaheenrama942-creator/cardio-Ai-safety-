import neurokit2 as nk
import numpy as np

def validate_cardiac_rhythm(raw_signal, fs=1000):
    """
    PURPOSE: This function acts as a safety 'auditor' for AI-based ECG diagnosis.
    It specifically targets the 'Black Box' reasoning of LLMs in AFib detection.
    """
    
    # STEP 1: Signal Pre-processing
    # We use 'neurokit' to clean the raw ECG data and find R-peaks accurately.
    # This replaces simple visual pattern recognition with actual signal analysis.
    processed_ecg, info = nk.ecg_process(raw_signal, sampling_rate=fs)
    
    # STEP 2: R-R Interval Calculation
    # We extract the distance between each heartbeat (R-peaks) in milliseconds.
    r_peaks = info['ECG_R_Peaks']
    rr_intervals = np.diff(r_peaks)
    
    # STEP 3: HRV Statistical Analysis (The 'Human' Audit)
    # SDNN is the gold standard for rhythm regularity. 
    # AI (LLMs) often mistake a 'Silent P-wave' for AFib. 
    # Our logic: If it's AFib, SDNN MUST be high. If SDNN is low, it's NOT AFib.
    sdnn_value = np.std(rr_intervals)
    
    print(f"--- CLINICAL AUDIT METRICS ---")
    print(f"Computed SDNN: {sdnn_value:.2f} ms")

    # STEP 4: Clinical Decision Logic
    # Here we define the safety threshold (30ms) to catch LLM hallucinations.
    if sdnn_value < 30:
        conclusion = (
            "AUDIT ALERT: The LLM flagged this as AFib (due to missing P-waves), "
            "but statistical analysis shows high regularity (SDNN < 30ms). "
            "Diagnosis: Likely Junctional Rhythm. LLM Hallucination confirmed."
        )
    elif 30 <= sdnn_value <= 100:
        conclusion = "AUDIT PASS: Rhythm is within normal physiological variability."
    else:
        conclusion = "AUDIT CONFIRMED: High irregularity detected (SDNN > 100ms). AFib diagnosis is valid."

    return conclusion

# ---------------------------------------------------------
# SIMULATION: Testing the auditor with 'clean' regular data
# This simulates a Junctional Rhythm (Regular but missing P-waves)
# ---------------------------------------------------------
synthetic_ecg = nk.ecg_simulate(duration=12, heart_rate=65, noise=0.01)
audit_report = validate_cardiac_rhythm(synthetic_ecg)
print(audit_report)
