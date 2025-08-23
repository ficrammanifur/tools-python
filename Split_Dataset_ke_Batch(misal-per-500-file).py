import os
import shutil

input_folder = "dataset_monyet_webp"
output_base = "dataset_batches"
batch_size = 500

os.makedirs(output_base, exist_ok=True)

files = [f for f in os.listdir(input_folder) if f.endswith(".webp")]
for i in range(0, len(files), batch_size):
    batch_folder = os.path.join(output_base, f"batch_{i//batch_size+1}")
    os.makedirs(batch_folder, exist_ok=True)
    
    for f in files[i:i+batch_size]:
        shutil.copy(os.path.join(input_folder, f), batch_folder)

print("✅ Dataset berhasil dibagi jadi beberapa batch folder")
