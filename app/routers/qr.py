from fastapi import APIRouter, Response
import qrcode
import io

router = APIRouter(prefix="/generar-qr", tags=["QR"])

@router.post("/creacion")
async def creat_qr(texto: str):
    img = qrcode.make(texto)

    buffer = io.BytesIO()

    img.save(buffer, format="PNG")

    image_bytes = buffer.getvalue()
    return Response(content=image_bytes, media_type = "image/png")
