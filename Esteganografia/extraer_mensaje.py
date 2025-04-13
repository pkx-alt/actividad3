
from PIL import Image, ImageSequence
from stegano import lsb
import os

carpeta_frames = "frames_extraidos2"
gif_original = "gif_con_mensaje - copia.gif"
frame_objetivo = 0

ruta_frame_oculto = f"{carpeta_frames}/frame_{frame_objetivo}_oculto.png"

# Crear carpeta para los frames
os.makedirs(carpeta_frames, exist_ok=True)

# === 1. EXTRAER FRAMES ===
print("Extrayendo frames del GIF...")
with Image.open(gif_original) as im:
    for i, frame in enumerate(ImageSequence.Iterator(im)):
        frame = frame.convert("RGB")  # Asegura formato editable
        frame.save(f"{carpeta_frames}/frame_{i}.png")
print(f"Frames extraídos en carpeta: {carpeta_frames}")


# === 4. EXTRAER EL MENSAJE OCULTO ===
print("Extrayendo mensaje oculto del frame oculto...")
mensaje_recuperado = lsb.reveal(ruta_frame_oculto)
print("Mensaje recuperado:", mensaje_recuperado)
