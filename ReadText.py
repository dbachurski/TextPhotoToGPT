from google.cloud import vision
import io

class ReadText:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def read(self, file_name):
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image({'content': content})

        response = self.client.document_text_detection(image=image)

        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(response.text_annotations[0].description)


read=ReadText()
