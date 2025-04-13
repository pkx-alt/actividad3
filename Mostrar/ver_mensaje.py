from stegano import lsb
from PIL import Image, ImageSequence

# ========== CONFIGURACIÓN ========== 
gif_con_mensaje = "gif_con_mensaje.gif"  # Ruta del GIF que enviaste
frame_objetivo = 0  # Frame donde se encuentra el mensaje oculto
# ===================================

# Extraer el primer frame
with Image.open(gif_con_mensaje) as im:
    # Extraemos los frames del GIF
    frames = [frame.convert("RGB") for frame in ImageSequence.Iterator(im)]  # Aseguramos el formato RGB
    # Guardamos el primer frame
    frame = frames[frame_objetivo]
    ruta_frame = f"frame_{frame_objetivo}.png"
    frame.save(ruta_frame)

# Extraer el mensaje
print("Extrayendo mensaje oculto...")
mensaje_extraido = lsb.reveal(ruta_frame)
print("Mensaje extraído:", mensaje_extraido)
