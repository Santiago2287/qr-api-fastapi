from fastapi import APIRouter, Response, HTTPException, status
import qrcode
import io
from PIL import Image, UnidentifiedImageError
from app.models.qr import Qr
import requests

router = APIRouter(prefix="/generar-qr", tags=["QR"])

@router.post("/creacion")
async def creat_qr(data: Qr):
    qr_config = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=data.box_size,
        border=4,
        )
    qr_config.add_data(data.text)
    qr_config.make(fit=True)

    img_qr = qr_config.make_image(
        fill_color=data.fill_color,
        back_color=data.back_color
        ).convert("RGB")

    # 2. Logo: solo si viene URL
    if data.logo_url: 
        try:
            respuesta = requests.get(str(data.logo_url), headers=headers, timeout=5)
            logo = Image.open(io.BytesIO(respuesta.content)).convert("RGBA")

            # ~20% del ancho del QR (no 50%)
            max_dim = img_qr.size[0] // 5
            logo.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)

            pos = (
                (img_qr.size[0] - logo.size[0]) // 2,
                (img_qr.size[1] - logo.size[1]) // 2,
                )

            # 3er argumento = máscara → respeta la transparencia
            img_qr.paste(logo, pos, logo)
        except requests.RequestException:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se pudo descargar el logo. Verifica que la URL esté activa.")
        except UnidentifiedImageError:
            raise HTTPException(status_code= status. HTTP_400_BAD_REQUEST, detail="La URL no contiene una imagen válida. Usa formatos PNG o JPG.")

    buffer = io.BytesIO()
    img_qr.save(buffer, format="PNG")
    buffer.seek(0)
    return Response(content=buffer.getvalue(), media_type="image/png")
