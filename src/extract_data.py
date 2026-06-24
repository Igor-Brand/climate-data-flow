import json
import logging
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(Path("config/.env"))
print(load_dotenv)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

api_key = os.getenv("OPENWEATHER_API_KEY")
print(api_key)
url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q=Brasilia,BR&units=metric&appid={api_key}"
)


def extract_weather_data(url: str) -> dict:
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        logging.error(
            f"Erro na requisição! Status: {response.status_code}"
        )
        return {}

    data = response.json()

    if not data:
        logging.warning("Nenhum dado retornado")
        return {}

    output_path = Path("data/weather_data.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    logging.info(f"Arquivo salvo em {output_path}")

    return data


if __name__ == "__main__":
    weather_data = extract_weather_data(url)
    print(weather_data)