import os
import subprocess
from docx import Document

def convert_single_doc_to_docx_inplace(input_path):
    if input_path.lower().endswith(".doc") and not input_path.lower().endswith(".docx"):
        input_dir = os.path.dirname(input_path)
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = os.path.join(input_dir, base_name + ".docx")
        try:
            subprocess.run(
                ["libreoffice", "--headless", "--convert-to", "docx", input_path, "--outdir", input_dir],
                check=True
            )
            print(f"✅ Converted: {input_path} -> {output_path}")
            return output_path
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to convert {input_path}: {e}")
            return None
    return input_path  # already .docx

def load_docx_text(path):
    try:
        doc = Document(path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"❌ Failed to read {path}: {e}")
        return ""

def process_all_docs(base_folder):
    for radiology_type in os.listdir(base_folder):
        radiology_path = os.path.join(base_folder, radiology_type)
        if os.path.isdir(radiology_path):
            print(f"\n📂 Processing folder: {radiology_type}")
            for filename in os.listdir(radiology_path):
                file_path = os.path.join(radiology_path, filename)
                if filename.lower().endswith((".doc", ".docx")):
                    # Convert .doc to .docx if needed
                    if filename.lower().endswith(".doc") and not filename.lower().endswith(".docx"):
                        file_path = convert_single_doc_to_docx_inplace(file_path)
                    # Read .docx content
                    if file_path and file_path.endswith(".docx"):
                        text = load_docx_text(file_path)
                        print(f"\n📄 File: {filename}")
                        print(f"{text[:500]}...\n")  # print first 500 chars

# Example usage
process_all_docs("/home/diwan/Downloads/smart_report")
