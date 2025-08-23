import os
from PIL import Image

input_folder = "dataset_monyet"   # folder asal gambar
output_folder = "dataset_monyet_webp"  # folder hasil kompres

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGB")

        # Simpan ke .webp (quality bisa 50–95, makin kecil makin ringan)
        out_path = os.path.join(output_folder, filename.rsplit(".", 1)[0] + ".webp")
        img.save(out_path, "webp", quality=70)

print("✅ Semua gambar berhasil dikompresi & dikonversi ke .webp")
