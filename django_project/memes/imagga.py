import requests

class ImaggaService:
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def analyze_image(self, image_path, limit = 3):
        try:
            response = requests.post(
                'https://api.imagga.com/v2/tags',
                auth=(self.key, self.secret),
                files={'image': open(image_path, 'rb')})
            data = response.json()
            # Extrae las etiquetas y los ordena por nivel de confianza
            tags = sorted(
                data.get("result", {}).get("tags", []),
                key=lambda x: x["confidence"],
                reverse=True
            )[:limit]

            # Obtiene los nombres y el nivel de confianza de las qetiquetas
            top_tags = [(tag["tag"]["en"], tag['confidence']) for tag in tags]
            return top_tags

        except Exception as e:
            return f'Error en imagga: {str(e)}'
