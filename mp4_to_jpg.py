import cv2
import os
import tkinter as tk
from tkinter import filedialog
import re

def select_video_file():
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(
        title="Pilih file video MP4",
        filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
    )
    return file_path

def get_last_frame_number(output_folder):
    """Mendapatkan nomor frame terakhir dari file di folder hasil_images."""
    if not os.path.exists(output_folder):
        return 0
    
    files = [f for f in os.listdir(output_folder) if re.match(r'frame_\d{4}\.jpg', f)]
    if not files:
        return 0
    
    last_file = max(files, key=lambda x: int(re.search(r'\d{4}', x).group()))
    last_number = int(re.search(r'\d{4}', last_file).group())
    return last_number

def convert_mp4_to_jpg():
    input_video = select_video_file()
    if not input_video:
        print("Tidak ada file video yang dipilih!")
        return
    
    output_folder = "hasil_images"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    output_count = get_last_frame_number(output_folder) + 1
    
    video = cv2.VideoCapture(input_video)
    
    fps = video.get(cv2.CAP_PROP_FPS)
    
    frame_interval = int(round(fps / 1))
    
    frame_count = 0
    
    while True:
        success, frame = video.read()
        if not success:
            break
            
        if frame_count % frame_interval == 0:
            output_path = os.path.join(output_folder, f"frame_{output_count:04d}.jpg")
            cv2.imwrite(output_path, frame)
            output_count += 1
            
        frame_count += 1
    
    video.release()
    print(f"Konversi selesai! {output_count - get_last_frame_number(output_folder) - 1} frame telah disimpan di {output_folder}, mulai dari frame_{get_last_frame_number(output_folder) + 1:04d}.jpg")

if __name__ == "__main__":
    convert_mp4_to_jpg()
