import os
from fpdf import FPDF
from datetime import datetime

# Create directory
os.makedirs('./results', exist_ok=True)

# Create PDF with UTF-8 support
pdf = FPDF()
pdf.add_page()

# Enable UTF-8 (if your FPDF version supports it)
try:
    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.add_font('DejaVu', 'B', 'DejaVuSans-Bold.ttf', uni=True)
    USE_UTF8 = True
    DEFAULT_FONT = 'DejaVu'
except:
    # Fallback to standard fonts without Unicode
    USE_UTF8 = False
    DEFAULT_FONT = 'Arial'

# Title
pdf.set_font(DEFAULT_FONT, 'B', 16)
pdf.cell(0, 10, 'Experiment Report: Exp 2-8 (COMPLETE RESULTS)', 0, 1, 'C')
pdf.set_font(DEFAULT_FONT, 'I', 10)
pdf.cell(0, 5, f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}', 0, 1, 'C')
pdf.ln(10)

# Note about test set consistency
pdf.set_font(DEFAULT_FONT, 'B', 10)
pdf.cell(0, 8, ' ALL experiments use SAME test set (481 images)', 0, 1, 'C')
pdf.ln(5)

# Main Results Table
pdf.set_font(DEFAULT_FONT, 'B', 12)
pdf.cell(0, 10, 'Complete Experiment Results (Same Test Set):', 0, 1)
pdf.ln(5)

# Column widths
col_widths = [15, 75, 20, 20, 20, 20]  # [Exp, Model, Test Acc, P(Orig), R(Orig), Status]

# Table headers
pdf.set_font(DEFAULT_FONT, 'B', 8)
headers = ["Exp", "Model", "Test Acc", "P(Orig)", "R(Orig)", "Status"]
for i, header in enumerate(headers):
    pdf.cell(col_widths[i], 10, header, 1, 0, 'C')
pdf.ln()

# Table data
pdf.set_font(DEFAULT_FONT, '', 8)
data = [
    ["2", "Fourier_Balanced_CNN", "0.499", "0.000", "0.000", "FAILED"],
    ["3", "Fourier_MobileNetV2", "0.499", "0.000", "0.000", "FAILED"],
    ["4", "Laplacian_MobileNetV2", "0.846", "0.835", "0.863", "GOOD"],
    ["5", "Hybrid_MobileNetV2", "0.807", "0.968", "0.635", "IMBALANCED"],
    ["6", "RGB_MobileNetV2", "0.857", "0.814", "0.925", "GOOD"],
    ["7", "RGB_EfficientNetB0", "0.877", "0.870", "0.888", "BETTER"],
    ["8", "RGB_Laplacian_EfficientNetB0", "0.900", "0.910", "0.880", "BEST"]
]

for row in data:
    for i, item in enumerate(row):
        pdf.cell(col_widths[i], 10, str(item), 1, 0, 'C')
    pdf.ln()

# Footnotes
pdf.ln(5)
pdf.set_font(DEFAULT_FONT, 'I', 8)
pdf.cell(0, 5, "Note: Exp 5 (Hybrid) uses Fourier+Laplacian preprocessing", 0, 1)
pdf.cell(0, 5, "P(Orig) = Precision for Originals, R(Orig) = Recall for Originals", 0, 1)
pdf.cell(0, 5, "Test set: 481 images (241 originals, 240 recaptures)", 0, 1)
pdf.cell(0, 5, "FAILED = Model always predicts one class (class collapse)", 0, 1)

pdf.ln(15)

# Detailed Class Performance Table
pdf.set_font(DEFAULT_FONT, 'B', 12)
pdf.cell(0, 10, 'Detailed Class Performance:', 0, 1)
pdf.ln(5)

col_widths2 = [15, 55, 15, 15, 15, 15, 15]
pdf.set_font(DEFAULT_FONT, 'B', 7)
headers2 = ["Exp", "Model", "Acc", "P(O)", "R(O)", "P(R)", "R(R)"]
for i, header in enumerate(headers2):
    pdf.cell(col_widths2[i], 8, header, 1, 0, 'C')
pdf.ln()

pdf.set_font(DEFAULT_FONT, '', 7)
data2 = [
    ["2", "Fourier_Balanced_CNN", "0.499", "0.000", "0.000", "0.499", "1.000"],
    ["3", "Fourier_MobileNetV2", "0.499", "0.000", "0.000", "0.499", "1.000"],
    ["4", "Laplacian_MobileNetV2", "0.846", "0.835", "0.863", "0.858", "0.829"],
    ["5", "Hybrid_MobileNetV2", "0.807", "0.968", "0.635", "0.728", "0.979"],
    ["6", "RGB_MobileNetV2", "0.857", "0.814", "0.925", "0.913", "0.788"],
    ["7", "RGB_EfficientNetB0", "0.877", "0.870", "0.888", "0.885", "0.867"],
    ["8", "RGB_Laplacian_EfficientNetB0", "0.900", "0.910", "0.880", "0.880", "0.920"]
]

for row in data2:
    for i, item in enumerate(row):
        pdf.cell(col_widths2[i], 8, str(item), 1, 0, 'C')
    pdf.ln()

pdf.ln(5)
pdf.set_font(DEFAULT_FONT, 'I', 7)
pdf.cell(0, 5, "P(O)=Precision Originals, R(O)=Recall Originals, P(R)=Precision Recaptured, R(R)=Recall Recaptured", 0, 1)

pdf.ln(10)

# Performance Progression (using ASCII characters only)
pdf.set_font('Courier', '', 8)
progression = [
    "Exp 2: Fourier_Balanced_CNN           -> 49.9% (COMPLETE FAILURE: Always predicts recaptured)",
    "Exp 3: Fourier_MobileNetV2            -> 49.9% (COMPLETE FAILURE: Same pattern as Exp 2)",
    "Exp 4: Laplacian_MobileNetV2          -> 84.6% (FIRST WORKING: Balanced P/R both classes)",
    "Exp 5: Hybrid_MobileNetV2             -> 80.7% (IMBALANCED: High P/low R originals)",
    "Exp 6: RGB_MobileNetV2                -> 85.7% (IMPROVED: Better than feature engineering)",
    "Exp 7: RGB_EfficientNetB0             -> 87.7% (BETTER ARCH: More balanced)",
    "Exp 8: RGB_Laplacian_EfficientNetB0   -> 90.0% (BEST: Perfect F1 balance)"
]

for line in progression:
    pdf.cell(0, 5, line, 0, 1)

# Add a second page with technical analysis
pdf.add_page()

# Critical Technical Findings (using ASCII only)
pdf.set_font(DEFAULT_FONT, 'B', 12)
pdf.cell(0, 10, 'Critical Technical Findings:', 0, 1)
pdf.ln(5)

pdf.set_font(DEFAULT_FONT, '', 10)
findings = [
    "1. FOURIER PREPROCESSING DESTROYS MODEL LEARNING:",
    "   - Experiments 2 & 3: Precision_originals = 0.0, Recall_originals = 0.0",
    "   - Fourier transform eliminates recapture artifacts needed for classification",
    "   - Models collapse to single-class prediction (always 'recaptured')",
    "",
    "2. LAPLACIAN (EDGE DETECTION) PRESERVES IMPORTANT FEATURES:",
    "   - Experiment 4: 84.6% accuracy with balanced performance",
    "   - Edge features capture recapture boundary artifacts",
    "   - But: RGB images work even better (85.7% vs 84.6%)",
    "",
    "3. HYBRID FOURIER+LAPLACIAN CAUSES IMBALANCE:",
    "   - Experiment 5: 80.7% accuracy but severe class imbalance",
    "   - Originals: P=0.968 (high), R=0.635 (low) -> many false negatives",
    "   - Recaptured: P=0.728 (low), R=0.979 (high) -> many false positives",
    "",
    "4. RGB-ONLY OUTPERFORMS FEATURE ENGINEERING:",
    "   - Exp 6 (RGB MobileNetV2): 85.7% > Exp 4 (Laplacian): 84.6%",
    "   - Modern CNNs learn optimal features directly from raw images",
    "   - Feature engineering may remove important information",
    "",
    "5. EFFICIENTNETB0 ARCHITECTURE SUPERIORITY:",
    "   - Exp 7 (EfficientNetB0): 87.7% > Exp 6 (MobileNetV2): 85.7%",
    "   - Compound scaling and better design yield +2% improvement",
    "   - More consistent CV performance (lower variance)",
    "",
    "6. OPTIMAL COMBINATION: RGB + LAPLACIAN + EFFICIENTNETB0:",
    "   - Experiment 8: 90.0% accuracy (best overall)",
    "   - Perfect F1 score balance (0.90 for both classes)",
    "   - Combines raw image information with edge-enhanced features"
]

for finding in findings:
    if finding and finding[0].isdigit():
        pdf.set_font(DEFAULT_FONT, 'B', 10)
        pdf.cell(0, 6, finding, 0, 1)
        pdf.ln(1)
    elif finding:
        pdf.set_font(DEFAULT_FONT, '', 9)
        pdf.cell(10)
        pdf.cell(0, 5, finding, 0, 1)
    else:
        pdf.ln(2)

pdf.ln(10)

# Cross-Validation Insights
pdf.set_font(DEFAULT_FONT, 'B', 12)
pdf.cell(0, 10, 'Cross-Validation Insights:', 0, 1)
pdf.ln(5)

pdf.set_font(DEFAULT_FONT, '', 10)
cv_insights = [
    "1. Fourier Models (Exp 2-3):",
    "   - Inconsistent class prediction across folds",
    "   - Complete failure on test set",
    "",
    "2. Laplacian MobileNetV2 (Exp 4):",
    "   - High variance: 55.7% to 81.5% across folds",
    "   - Fold 3 shows severe recall imbalance",
    "",
    "3. Hybrid Model (Exp 5):",
    "   - Highest variance: 65.6% to 84.6% across folds",
    "   - Most unstable model architecture",
    "",
    "4. RGB Models (Exp 6-8):",
    "   - Lower variance and more consistent performance",
    "   - EfficientNetB0 shows best CV consistency"
]

for insight in cv_insights:
    if insight and insight[0].isdigit():
        pdf.set_font(DEFAULT_FONT, 'B', 10)
        pdf.cell(0, 6, insight, 0, 1)
        pdf.ln(1)
    elif insight:
        pdf.set_font(DEFAULT_FONT, '', 9)
        pdf.cell(10)
        pdf.cell(0, 5, insight[3:], 0, 1)

pdf.ln(10)

# Save PDF
pdf.output('./results/complete_experiment_report.pdf')
print("PDF saved to: ./results/complete_experiment_report.pdf")

# Create comprehensive text summary
with open('./results/experiment_summary_detailed.txt', 'w') as f:
    f.write("""
COMPLETE EXPERIMENT SUMMARY (Exp 2-8)
=====================================

EXPERIMENT RESULTS (Same Test Set - 481 images):
------------------------------------------------
Exp  Model                               Test Acc  Originals (P/R)   Recaptured (P/R)   Status
2    Fourier_Balanced_CNN                0.499     0.000 / 0.000     0.499 / 1.000     FAILED
3    Fourier_MobileNetV2                 0.499     0.000 / 0.000     0.499 / 1.000     FAILED  
4    Laplacian_MobileNetV2               0.846     0.835 / 0.863     0.858 / 0.829     GOOD
5    Hybrid_MobileNetV2                  0.807     0.968 / 0.635     0.728 / 0.979     IMBALANCED
6    RGB_MobileNetV2                     0.857     0.814 / 0.925     0.913 / 0.788     GOOD
7    RGB_EfficientNetB0                  0.877     0.870 / 0.888     0.885 / 0.867     BETTER
8    RGB_Laplacian_EfficientNetB0        0.900     0.910 / 0.880     0.880 / 0.920     BEST

KEY TECHNICAL FINDINGS:
----------------------
1. FOURIER PREPROCESSING COMPLETELY FAILS
   - Both Exp 2 & 3 achieve ~50% accuracy by always predicting "recaptured"
   - Fourier transform destroys recapture discrimination features

2. LAPLACIAN WORKS BUT RGB IS BETTER
   - Exp 4 (Laplacian): 84.6% accuracy
   - Exp 6 (RGB): 85.7% accuracy -> +1.1% improvement

3. ARCHITECTURE MATTERS: EfficientNetB0 > MobileNetV2
   - Exp 7 (EfficientNetB0): 87.7% > Exp 6 (MobileNetV2): 85.7% -> +2.0% improvement

4. BEST COMBINATION: RGB + Laplacian + EfficientNetB0
   - Exp 8: 90.0% accuracy with perfect F1 balance (0.90 for both classes)

5. HYBRID FOURIER+LAPLACIAN CAUSES PROBLEMS
   - Exp 5: Severe class imbalance despite 80.7% accuracy
   - High false negatives for originals, high false positives for recaptured

CV PERFORMANCE ANALYSIS:
-----------------------
- Fourier models: Complete failure (0% precision for originals)
- Laplacian: High variance (55.7% to 81.5% across folds)
- RGB models: More consistent performance
- EfficientNetB0: Best CV consistency across all experiments

RECOMMENDATIONS:
---------------
1. Use RGB_Laplacian_EfficientNetB0 (Exp 8) for maximum accuracy (90%)
2. For simpler deployment, use RGB_EfficientNetB0 (Exp 7) with 87.7% accuracy
3. Abandon Fourier preprocessing entirely
4. Focus on EfficientNet architecture family
5. Maintain consistent test set methodology

NEXT STEPS:
----------
- Deploy Exp 8 model for production use
- Analyze failure cases to understand remaining 10% error
- Consider ensemble of Exp 7 and Exp 8 for potential improvement
- Investigate why Fourier preprocessing fails (academic interest)

Full detailed report: complete_experiment_report.pdf
""")

print("Detailed summary saved to: ./results/experiment_summary_detailed.txt")