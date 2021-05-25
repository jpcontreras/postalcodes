import requests
import json

class ProcessorService:
    API_URL = "http://processor_web_1:3000/processor_files/"

    # ===== Parameters:
    # *+file+: String(binary)
    def create(self, file):
        files = {'file': file}
        response = requests.post(f"{self.API_URL}create", files=files, verify=False).text
        data_string = json.loads(response)

