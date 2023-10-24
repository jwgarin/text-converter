import requests

def image_to_text(filename, api_key):
    """Use API Ninjas to convert image file to texts"""
    with open(filename, 'rb') as f:
        image_descriptor = f.read()
        files = {'image': image_descriptor}
        r = requests.post('https://api.api-ninjas.com/v1/imagetotext', files=files, headers={'x-api-key': api_key})
        return ' '.join([o['text'] for o in r.json()])