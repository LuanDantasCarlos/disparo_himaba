import requests


class WhatsappService:

    def __init__(self):
        ...

    def send_message(self, destinatario: str, message: str):
        url = "https://api.1msg.io/LOK814261759/sendTemplate"

        payload = {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbnN0YW5jZUlkIjoiTE9LODE0MjYxNzU5IiwidG9rZW4iOiJUS05xOHUwSVo0MElqc0dZd1JMOUU4ZE5EQ3J1dEZycSIsImlzcyI6IjFtc2cuaW8iLCJpYXQiOjE3NjA3MTExMjJ9.LVwfK2q-JbDouSoxPJ_pP5N0-oHKoBp77AnXxhuZ320",
            "template": "start_template_1_z5b2ko6p9",
            "language": {
                "policy": "deterministic",
                "code": "en_US"
            },
            "namespace": "d9791769_e051_4e43_af40_bd9c04b2789d",
            "phone": destinatario,
            "params": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": message
                        }
                    ]
                }
            ]
        }

        headers = {
            "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbnN0YW5jZUlkIjoiTE9LODE0MjYxNzU5IiwidG9rZW4iOiJUS05xOHUwSVo0MElqc0dZd1JMOUU4ZE5EQ3J1dEZycSIsImlzcyI6IjFtc2cuaW8iLCJpYXQiOjE3NjA3MTExMjJ9.LVwfK2q-JbDouSoxPJ_pP5N0-oHKoBp77AnXxhuZ320",
            "Content-Type": "application/json",
            "User-Agent": "python-requests"
        }

        response = requests.post(url, headers=headers, json=payload, timeout=15)

        return response.json()

# Teste
if __name__ == '__main__':
    whatsapp_service = WhatsappService()

    result = whatsapp_service.send_message(
        destinatario="5527999973911",
        message="Bom dia!"
    )

    print(result)
