#!/usr/bin/env python3
"""
Experiment Results Summary (Exp 09-13)
Generates a PDF report and a TXT summary using FPDF (classic).
This script normalizes Unicode punctuation to ASCII to avoid latin-1 encoding errors.
"""

import os
import json
from datetime import datetime
from fpdf import FPDF

# ---------------------------
# Helpers: ASCII normalization
# ---------------------------
def normalize_ascii(s: str) -> str:
    """Replace common Unicode punctuation with ASCII-safe equivalents."""
    if s is None:
        return ""
    return (
        str(s)
        .replace("–", "-")
        .replace("—", "-")
        .replace("―", "-")
        .replace("•", "-")
        .replace("·", "-")
        .replace("“", '"')
        .replace("”", '"')
        .replace("„", '"')
        .replace("‹", "<")
        .replace("›", ">")
        .replace("‘", "'")
        .replace("’", "'")
        .replace("…", "...")
        .replace("™", "(TM)")
        .replace("©", "(C)")
        .replace("®", "(R)")
        .replace("\u2014", "-")
    )

def safe_str(x):
    return normalize_ascii(str(x))

# ---------------------------
# FPDF safe wrappers
# ---------------------------
def safe_cell(pdf, w, h, txt="", border=0, ln=0, align=""):
    pdf.cell(w, h, safe_str(txt), border=border, ln=ln, align=align)

def safe_multi_cell(pdf, w, h, txt="", border=0, align="L"):
    pdf.multi_cell(w, h, safe_str(txt), border=border, align=align)

# ---------------------------
# Prepare results directory
# ---------------------------
OUT_DIR = "./results"
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------
# Experiment data (09-13)
# ---------------------------
experiments = [
    {
        "exp": "09",
        "name": "RGB_EfficientNetB0-Laplacian",
        "status": "FAILED (val_acc=0.50)",
        "accuracy": 0.8271604938271605,
        "original": {"precision": 0.8648648648648649, "recall": 0.7804878048780488, "f1": 0.8205128205128205, "support": 41.0},
        "recaptured": {"precision": 0.7954545454545454, "recall": 0.875, "f1": 0.8333333333333334, "support": 40.0},
        "macro_avg": {"precision": 0.8301597051597052, "recall": 0.8277439024390244, "f1": 0.8269230769230769, "support": 81.0},
        "weighted_avg": {"precision": 0.8305881639214973, "recall": 0.8271604938271605, "f1": 0.8268439379550491, "support": 81.0},
        "json": {"val_accuracy": 0.82, "original_correct": 32, "recaptured_correct": 35, "total": 81},
    },
    {
        "exp": "10",
        "name": "RGB-EfficientNetB0 (Roselab + Android-captured)",
        "status": "GOOD",
        "accuracy": 0.9223,
        "original": {"precision": 0.93, "recall": 0.91, "f1": 0.92, "support": 284.0},
        "recaptured": {"precision": 0.91, "recall": 0.93, "f1": 0.92, "support": 282.0},
        "macro_avg": {"precision": 0.92, "recall": 0.92, "f1": 0.92, "support": 566.0},
        "weighted_avg": {"precision": 0.92, "recall": 0.92, "f1": 0.92, "support": 566.0},
        "json": {"val_accuracy": 0.9223, "f1_recaptured": 0.9228, "original_correct": 259, "recaptured_correct": 263, "total_samples": 566},
    },
    {
        "exp": "11",
        "name": "RGB-EnetB0 (NTU-Android x8) + Testing iPhone",
        "status": "CONSISTENT",
        "accuracy": 0.9223,
        "original": {"precision": 0.93, "recall": 0.91, "f1": 0.92, "support": 284.0},
        "recaptured": {"precision": 0.91, "recall": 0.93, "f1": 0.92, "support": 282.0},
        "macro_avg": {"precision": 0.92, "recall": 0.92, "f1": 0.92, "support": 566.0},
        "weighted_avg": {"precision": 0.92, "recall": 0.92, "f1": 0.92, "support": 566.0},
        "json": {"val_accuracy": 0.9223, "f1_recaptured": 0.9228, "original_correct": 259, "recaptured_correct": 263, "total_samples": 566},
    },
    {
        "exp": "12",
        "name": "Robust_3_devices_EfficientNetB0",
        "status": "BEST",
        "accuracy": 0.9481,
        "original": {"precision": 0.93, "recall": 0.97, "f1": 0.95, "support": 68.0},
        "recaptured": {"precision": 0.97, "recall": 0.93, "f1": 0.95, "support": 67.0},
        "macro_avg": {"precision": 0.95, "recall": 0.95, "f1": 0.95, "support": 135.0},
        "weighted_avg": {"precision": 0.95, "recall": 0.95, "f1": 0.95, "support": 135.0},
        "json": {"accuracy": 0.9481, "f1_original": 0.9496, "f1_recaptured": 0.9466},
    },
    {
        "exp": "13",
        "name": "MobileNetV3_3_Mobile_devices",
        "status": "GOOD",
        "accuracy": 0.89,
        "original": {"precision": 0.9, "recall": 0.88, "f1": 0.89, "support": 68.0},
        "recaptured": {"precision": 0.88, "recall": 0.9, "f1": 0.89, "support": 67.0},
        "macro_avg": {"precision": 0.89, "recall": 0.89, "f1": 0.89, "support": 135.0},
        "weighted_avg": {"precision": 0.89, "recall": 0.89, "f1": 0.89, "support": 135.0},
        "json": None,
    },
]

# ---------------------------
# Create PDF
# ---------------------------
TITLE = "Experiment Results Summary (Exp 09-13)"
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Page 1
pdf.add_page()
pdf.set_font("Arial", "B", 16)
safe_cell(pdf, 0, 10, TITLE, ln=1, align="C")

pdf.set_font("Arial", "I", 9)
safe_cell(pdf, 0, 6, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=1, align="C")
pdf.ln(4)

# Intro / Key observations header
pdf.set_font("Arial", "B", 12)
safe_cell(pdf, 0, 8, "Summary Table:", ln=1)
pdf.ln(2)

# Summary table header
pdf.set_font("Arial", "B", 9)
col_widths = [12, 85, 22, 70]  # Exp, Model, Accuracy, Status
safe_cell(pdf, col_widths[0], 8, "Exp", border=1, align="C")
safe_cell(pdf, col_widths[1], 8, "Model", border=1, align="C")
safe_cell(pdf, col_widths[2], 8, "Accuracy", border=1, align="C")
safe_cell(pdf, col_widths[3], 8, "Status", border=1, ln=1, align="C")

# Summary table rows
pdf.set_font("Arial", size=9)
for e in experiments:
    safe_cell(pdf, col_widths[0], 8, e["exp"], border=1, align="C")
    safe_cell(pdf, col_widths[1], 8, e["name"], border=1, align="L")
    safe_cell(pdf, col_widths[2], 8, f"{e['accuracy']:.3f}", border=1, align="C")
    safe_cell(pdf, col_widths[3], 8, e["status"], border=1, ln=1, align="C")

pdf.ln(6)

# Key observations block
pdf.set_font("Arial", "B", 11)
safe_cell(pdf, 0, 7, "Key Observations:", ln=1)
pdf.set_font("Arial", size=10)
obs_lines = [
    "1. Experiment 09 failed with validation accuracy 50% (random guessing).",
    "2. Experiments 10 and 11 report identical metrics (0.922 accuracy, 566 samples).",
    "3. Experiment 12 is the best performing model (0.948 accuracy on 135 samples).",
    "4. Experiment 13 is an efficient alternative with 0.890 accuracy using MobileNetV3.",
    "5. Successful experiments (10-13) have balanced precision/recall scores.",
    "6. Dataset sizes vary: 81 (Exp 09), 566 (Exp 10-11), 135 (Exp 12-13).",
]
for line in obs_lines:
    safe_multi_cell(pdf, 0, 5, "- " + line)
pdf.ln(6)

# Add full experimental sections (continuous report)
for e in experiments:
    pdf.set_font("Arial", "B", 12)
    safe_cell(pdf, 0, 8, f"Experiment {e['exp']} - {e['name']}", ln=1)
    pdf.ln(1)

    # Status and accuracy
    pdf.set_font("Arial", "", 10)
    safe_cell(pdf, 40, 6, "Status:", border=0)
    safe_cell(pdf, 0, 6, e["status"], ln=1)
    safe_cell(pdf, 40, 6, "Reported Accuracy:", border=0)
    safe_cell(pdf, 0, 6, f"{e['accuracy']:.4f}", ln=1)
    pdf.ln(2)

    # Metrics table: Precision / Recall / F1 / Support for both classes
    pdf.set_font("Arial", "B", 9)
    colw = [40, 35, 35, 35, 35]  # label, P, R, F1, Support
    safe_cell(pdf, colw[0], 7, "Class", border=1, align="C")
    safe_cell(pdf, colw[1], 7, "Precision", border=1, align="C")
    safe_cell(pdf, colw[2], 7, "Recall", border=1, align="C")
    safe_cell(pdf, colw[3], 7, "F1-score", border=1, align="C")
    safe_cell(pdf, colw[4], 7, "Support", border=1, ln=1, align="C")

    pdf.set_font("Arial", size=9)
    # Original
    orig = e["original"]
    safe_cell(pdf, colw[0], 7, "Original", border=1, align="C")
    safe_cell(pdf, colw[1], 7, f"{orig['precision']:.4f}", border=1, align="C")
    safe_cell(pdf, colw[2], 7, f"{orig['recall']:.4f}", border=1, align="C")
    safe_cell(pdf, colw[3], 7, f"{orig['f1']:.4f}", border=1, align="C")
    safe_cell(pdf, colw[4], 7, f"{int(orig['support'])}", border=1, ln=1, align="C")

    # Recaptured
    rec = e["recaptured"]
    safe_cell(pdf, colw[0], 7, "Recaptured", border=1, align="C")
    safe_cell(pdf, colw[1], 7, f"{rec['precision']:.4f}", border=1, align="C")
    safe_cell(pdf, colw[2], 7, f"{rec['recall']:.4f}", border=1, align="C")
    safe_cell(pdf, colw[3], 7, f"{rec['f1']:.4f}", border=1, align="C")
    safe_cell(pdf, colw[4], 7, f"{int(rec['support'])}", border=1, ln=1, align="C")

    pdf.ln(2)

    # Macro & weighted averages
    pdf.set_font("Arial", "B", 9)
    safe_cell(pdf, 40, 6, "Macro Avg (P/R/F1):", border=0)
    m = e.get("macro_avg", {})
    safe_cell(pdf, 0, 6, f"{m.get('precision', 0):.4f} / {m.get('recall', 0):.4f} / {m.get('f1', 0):.4f}", ln=1)
    pdf.set_font("Arial", "B", 9)
    safe_cell(pdf, 40, 6, "Weighted Avg (P/R/F1):", border=0)
    w = e.get("weighted_avg", {})
    safe_cell(pdf, 0, 6, f"{w.get('precision', 0):.4f} / {w.get('recall', 0):.4f} / {w.get('f1', 0):.4f}", ln=1)
    pdf.ln(3)

    # JSON block
    pdf.set_font("Courier", "", 9)
    safe_multi_cell(pdf, 0, 5, "JSON Data:")
    safe_multi_cell(pdf, 0, 5, json.dumps(e.get("json", {}), indent=2))
    pdf.ln(6)

# Final summary / recommendations
pdf.add_page()
pdf.set_font("Arial", "B", 12)
safe_cell(pdf, 0, 8, "Final Summary and Recommendations", ln=1)
pdf.ln(2)

pdf.set_font("Arial", "", 10)
final_lines = [
    "Summary:",
    " - Experiments 10 and 11 show identical, stable performance across datasets (0.922 accuracy).",
    " - Experiment 12 achieves the best performance (0.948 accuracy) and is recommended for production.",
    " - Experiment 09 shows failure on validation (50% val accuracy). Investigate dataset or preprocessing differences.",
    " - Experiment 13 (MobileNetV3) is a good lightweight alternative (0.890 accuracy).",
    "",
    "Recommendations:",
    " 1. Prioritize model from Experiment 12 for deployment (Robust_3_devices_EfficientNetB0).",
    " 2. Use Experiment 13 when compute or memory is constrained on device.",
    " 3. Re-evaluate Laplacian preprocessing used in Experiment 09 that led to validation collapse.",
    " 4. Maintain an identical test set across experiments when possible to reduce comparison variance.",
    " 5. Collect more diverse recapture samples to reduce remaining error margins.",
]

for line in final_lines:
    safe_multi_cell(pdf, 0, 6, line)

# Save PDF file
pdf_path = os.path.join(OUT_DIR, "experiment_09_13_report.pdf")
pdf.output(pdf_path)
print(f"PDF saved to: {pdf_path}")

# ---------------------------
# Write TXT summary
# ---------------------------
txt_path = os.path.join(OUT_DIR, "experiment_09_13_summary.txt")
with open(txt_path, "w", encoding="utf-8") as f:
    f.write("Experiment Results Summary (Exp 09-13)\n")
    f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
    f.write("Summary Table:\n")
    f.write("Exp\tModel\tAccuracy\tStatus\n")
    for e in experiments:
        f.write(f"{e['exp']}\t{e['name']}\t{e['accuracy']:.3f}\t{e['status']}\n")
    f.write("\nDetailed per-experiment JSON blocks:\n")
    for e in experiments:
        f.write(f"\nExperiment {e['exp']} - {e['name']}\n")
        f.write(json.dumps(e.get("json", {}), indent=2))
        f.write("\n")

print(f"TXT summary saved to: {txt_path}")
