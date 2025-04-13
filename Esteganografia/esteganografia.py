from PIL import Image, ImageSequence
from stegano import lsb
import os

# ========== CONFIGURACIÓN ==========
gif_original = "gif_puesta.gif"
carpeta_frames = "frames_extraidos"
frame_objetivo = 0  # Frame donde se esconderá el mensaje
mensaje_secreto = "Fh4wx+DNMp+zifofG/GMzht9UKnE5lX+ZKM1vQ0xI6k2grDnDD79Nramf+ezyLod5VhQyeQtfoHccUersOrqJk9156vuK5thTZOO1NXRNEwzku0hrM7g6ZkpjoKhoY5XiekJ44X87B3clk66iRLXBIp9oVVOKC9vytnPJ93kVIY="

gif_salida = "gif_con_mensaje.gif"
# ===================================

# Crear carpeta para los frames
os.makedirs(carpeta_frames, exist_ok=True)

# === 1. EXTRAER FRAMES ===
print("Extrayendo frames del GIF...")
with Image.open(gif_original) as im:
    for i, frame in enumerate(ImageSequence.Iterator(im)):
        frame = frame.convert("RGB")  # Asegura formato editable
        frame.save(f"{carpeta_frames}/frame_{i}.png")
print(f"Frames extraídos en carpeta: {carpeta_frames}")

# === 2. OCULTAR MENSAJE EN UN FRAME ===
ruta_frame_objetivo = f"{carpeta_frames}/frame_{frame_objetivo}.png"
ruta_frame_oculto = f"{carpeta_frames}/frame_{frame_objetivo}_oculto.png"

print(f"Incrustando mensaje oculto en frame {frame_objetivo}...")
imagen_modificada = lsb.hide(ruta_frame_objetivo, message=mensaje_secreto)
imagen_modificada.save(ruta_frame_oculto)

# === 3. RECONSTRUIR EL GIF ===
print("Reconstruyendo el GIF animado...")

# Volvemos a abrir el GIF original para obtener la duración original de los frames
with Image.open(gif_original) as im:
    duraciones = [frame.info.get("duration", 100) for frame in ImageSequence.Iterator(im)]

frames = []
for i in range(len(duraciones)):
    path_oculto = f"{carpeta_frames}/frame_{i}_oculto.png"
    path_normal = f"{carpeta_frames}/frame_{i}.png"
    img = Image.open(path_oculto if os.path.exists(path_oculto) else path_normal)
    frames.append(img)

# Guardamos el GIF
frames[0].save(
    gif_salida,
    save_all=True,
    append_images=frames[1:],
    loop=0,
    duration=duraciones
)

print(f"GIF creado exitosamente (con duración original): {gif_salida}")


