from django.shortcuts import render
from django.http import JsonResponse

import os
import base64
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from PIL import Image
from io import BytesIO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Get the absolute path of the canset.json file
canset_path = os.path.join(os.getcwd(), 'canset.json')


# Initialize Firebase Admin SDK
cred = credentials.Certificate(canset_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://canset-druksung-default-rtdb.firebaseio.com/'
})

def home(request):
    return render(request, 'api_endpoint/home.html')

def decode_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # Process the uploaded image here
        # You can access the uploaded image using request.FILES['image']
        print('Image received successfully')
        # Return a success response
        return JsonResponse({'message': 'Image received successfully'})

    # Return an error response if the image was not received
    return JsonResponse({'error': 'Image not received'}, status=400)

@require_GET
def convert_data_to_image(request):
    # Get data from Firebase database
    ref = db.reference('/image/gray')
    data = ref.get()

    encoded_image = data.encode()
    decoded_image_bytes = base64.b64decode(encoded_image)

    # Create a BytesIO object and write the decoded image bytes into it
    image_buffer = BytesIO()
    image_buffer.write(decoded_image_bytes)

    # Open the image from the buffer
    image = Image.open(image_buffer)

     # Create a response with the image content
    response = HttpResponse(content_type='image/jpeg')
    image.save(response, format='JPEG')

    return response

