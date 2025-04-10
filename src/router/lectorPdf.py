from fastapi import APIRouter, FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse, Response
from PyPDF2 import PdfReader
from io import BytesIO
import httpx
from bs4 import BeautifulSoup

lectorPdf = APIRouter()
app = FastAPI()

@lectorPdf.get("/lectorPdf")
def root():
    try:
        return {"message": "API Lector PDF Endpoint is Working"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@lectorPdf.post("/lectorPdf/upload")
async def upload_pdf(dataValue: str = Form(...), pdf: UploadFile = File(...)):
    try:
        content = await pdf.read()
        pdf_file = BytesIO(content)
        reader = PdfReader(pdf_file)

        print("🤓🤓🤓🤓", content)

        text = ""
        for page in reader.pages:
            text += page.extract_text()

        lines = text.split("\n")
        print("🦜🦜🦜🦜", lines)
        for line in lines:
            print("🧨🧨🧨", line)
            if dataValue in line.lower():
                print("💙💙💙💙", line.strip())
                return JSONResponse(content={"line": line.strip()}, status_code=200)

        return JSONResponse(content={"message": "La palabra "+ dataValue + " no fue encontrada en el PDF."}, status_code=404)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el PDF: {str(e)}")

@lectorPdf.get("/scrape")
async def scrape_website():
    url = "https://publicacionesprocesales.ramajudicial.gov.co/web/publicaciones-procesales/inicio?p_p_id=co_com_avanti_efectosProcesales_PublicacionesEfectosProcesalesPortlet_INSTANCE_qOzzZevqIWbb&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_co_com_avanti_efectosProcesales_PublicacionesEfectosProcesalesPortlet_INSTANCE_qOzzZevqIWbb_jspPage=%2FMETA-INF%2Fresources%2Fdetail.jsp&_co_com_avanti_efectosProcesales_PublicacionesEfectosProcesalesPortlet_INSTANCE_qOzzZevqIWbb_articleId=77183338"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            publicaciones = []

            for item in soup.find_all("div", class_="docs-publicacion"):
                tbody = item.find("tbody")
                titulo = tbody.text.strip() if tbody else "Sin título"

                print("🎹🎹🎹🎹", tbody)

                print("🧨🧨🧨", titulo)

                enlace_elemento = tbody.find("a") if tbody else None
                print("🤓🤓🤓🤓", enlace_elemento)
                enlace = enlace_elemento["href"] if enlace_elemento and enlace_elemento.has_attr("href") else None

                description = item.find("a").text.strip() if item.find("a") else "Sin descripción"
                if enlace and not enlace.startswith("http"):
                    enlace = f"https://publicacionesprocesales.ramajudicial.gov.co{enlace}"

                print("🤑🤑🤑🤑", enlace)

                publicaciones.append({
                    "titulo": titulo,
                    "description": description,
                    "enlace": enlace,
                })

                if enlace:
                    pdf_response = await client.get(enlace)
                    if pdf_response.status_code == 200:

                        content = pdf_response.read()
                        pdf_file = BytesIO(content)
                        reader = PdfReader(pdf_file)
                        print("🦜🦜🦜", reader)

                text = ""
                for page in reader.pages:
                    text += page.extract_text()

                print("⭐⭐⭐⭐", text)
            return JSONResponse(content={"publicaciones": publicaciones}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al hacer scraping: {str(e)}")


