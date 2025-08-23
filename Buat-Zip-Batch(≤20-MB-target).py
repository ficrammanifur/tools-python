import os
import zipfile

batch_folder = "dataset_batches"

for folder in os.listdir(batch_folder):
    folder_path = os.path.join(batch_folder, folder)
    zip_path = folder_path + ".zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), file)

print("✅ Semua batch sudah dijadikan file .zip")
