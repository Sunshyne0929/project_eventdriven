from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

def ocr_view(request):
    return render(request, 'ocr_template.html')

def ocr_process(request):
    if request.method == 'POST' and request.FILES['image']:
        # Handle file upload
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)

        # Perform OCR
        img = Image.open(f'media/{filename}')
        ocr_result = pytesseract.image_to_string(img)

        return render(request, 'ocr_result.html', {'ocr_result': ocr_result})

    return redirect('ocr_view')  # Redirect if no file is uploaded
