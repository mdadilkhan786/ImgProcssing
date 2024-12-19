import base64
import requests
from urllib.request import urlretrieve
from PIL import Image

api_url = "https://python-api.techsimplus.com/api/amazon-service/"

with open('image.jpg', 'rb') as image_file:
    base64_bytes = base64.b64encode(image_file.read())
    base64_string = base64_bytes.decode()

# Send the POST request with the image data and service type
response = requests.post(api_url, json={"image": base64_string, "service_type": "FaceDetection"})

if response.status_code == 200:
    response_data = response.json()
    image_url = response_data['data']['image']
    
    # Download and save the processed image
    urlretrieve(image_url, 'processed_image.jpg')

    # Open and show the processed image
    processed_image = Image.open('processed_image.jpg')
    processed_image.show()
else:
    print("Error: Failed to retrieve image from the API.")
