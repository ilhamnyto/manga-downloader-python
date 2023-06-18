import os 
import json
import aiohttp
import requests
from io import BytesIO

from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader
from reportlab.lib.utils import ImageReader
from django.http import HttpResponse, JsonResponse


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

async def search(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        keyword = data.get('keyword')
       
        url = 'https://ww5.mangakakalot.tv/search/' + keyword.replace(" ", "%20")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')

                tags = soup.select(".story_name a")
                resp = [{"title": tag.text, "url": tag.get('href')} for tag in tags if keyword in tag.text.lower()]

        return JsonResponse({"data": resp})

async def get_chapter(request, id):
    if request.method == 'GET':
        url = 'https://ww5.mangakakalot.tv/' + id

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')

                chaps = soup.select(".row span a")
                
                resp = [{"title": chap.get('title'), "url": chap.get('href')} for chap in chaps]
                
        return JsonResponse({"data": resp})

async def get_image(request, id):
    if request.method == 'GET':
        
        url = 'https://ww5.mangakakalot.tv/' + id
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')

                images = soup.select(".img-loading")
                urls = [img.get('data-src') for img in images]
                
                pdf_writer = PdfWriter()
                buffer = BytesIO()

                for url in urls:
                    response = requests.get(url)
                    # Create a BytesIO object to hold the image data
                    image_stream = BytesIO(response.content)

                    # Load the image to get its dimensions
                    image = ImageReader(image_stream)
                    image_width = image.getSize()[0]
                    image_height = image.getSize()[1]

                    # Create a new PDF canvas with the same size as the image
                    output_pdf_stream = BytesIO()
                    canvas_obj = canvas.Canvas(output_pdf_stream, pagesize=(image_width, image_height))

                    # Draw the image on the canvas
                    canvas_obj.drawImage(image, 0, 0, width=image_width, height=image_height)

                    # Save the canvas as a PDF
                    canvas_obj.save()
                    # Add the canvas pages to the PDF writer
                    pdf_stream = BytesIO(output_pdf_stream.getvalue())
                    temp_pdf = PdfReader(pdf_stream)                    
                    page = temp_pdf.pages[0]
                    pdf_writer.add_page(page)
                    
                pdf_writer.write(buffer)
                buffer.seek(0)
                response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="example.pdf"'

                return response


