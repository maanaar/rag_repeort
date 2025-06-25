import requests

# Replace with the actual URL if running on a server or different port
API_URL ="http://11.11.11.222:8060/question"


# Example question
# query = """MAGNETIC RESONANCE IMAGING REPORT
#
# Patient Information:
# Name: John Smith
# DOB: 01/15/1975
# MRN: 123456789
# Date of Exam: March 15, 2024
# Referring Physician: Dr. Sarah Johnson, Neurology
#
# Clinical Indication:
# Headaches, dizziness, and memory problems for the past 3 months. Rule out intracranial pathology.
#
# Technique:
# MRI of the brain was performed without and with intravenous gadolinium contrast using a 3 Tesla scanner. Multiplanar T1-weighted, T2-weighted, FLAIR, and diffusion-weighted imaging sequences were obtained.
#
# Findings:
#
# Brain Parenchyma:
# The cerebral hemispheres demonstrate normal signal intensity and morphology. No evidence of acute infarction on diffusion-weighted imaging. No hemorrhage or mass lesion identified. The brainstem and cerebellum appear normal. Normal gray-white matter differentiation is preserved.
#
# Ventricular System:
# The lateral, third, and fourth ventricles are normal in size and configuration. No evidence of hydrocephalus or midline shift.
#
# Extra-axial Spaces:
# The subarachnoid spaces are within normal limits. No evidence of subdural or epidural hematoma. No abnormal extra-axial fluid collections.
#
# Vascular Structures:
# The major intracranial arteries demonstrate normal flow voids. No evidence of aneurysm or vascular malformation. The dural venous sinuses appear patent.
#
# Skull and Scalp:
# The calvarium demonstrates normal signal intensity. Paranasal sinuses show mild mucosal thickening in the maxillary sinuses bilaterally, likely representing chronic sinusitis. The orbits and temporal bones are unremarkable.
#
# Post-Contrast Images:
# No abnormal enhancement identified. The blood-brain barrier appears intact. Normal enhancement of the pituitary gland and choroid plexus.
#
# IMPRESSION:
#
# 1. Normal brain MRI examination
# 2. No evidence of acute intracranial pathology
# 3. Mild chronic maxillary sinusitis
#
# Recommendations:
# Clinical correlation is recommended. If symptoms persist or worsen, consider follow-up imaging in 6 months. ENT consultation may be considered for chronic sinusitis if clinically indicated.
#
# Radiologist: Dr. Michael Chen, MD
# Date Reported: March 15, 2024
# Electronically signed on: March 15, 2024 at 14:30
#
# Summarize the key findings of this MRI report"""
query = 'what are syptoms of a brain tumor'
# Make a POST request
response = requests.post(API_URL, data={"query": query})

# Print the result
if response.status_code == 200:
    result = response.json()
    print("✅ Answer:", result.get("answer"))
else:
    print("❌ Failed to get answer. Status code:", response.status_code)
    print("Details:", response.text)
