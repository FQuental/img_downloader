import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL do site que você deseja baixar
site_url = 

# Pasta onde as imagens serão salvas
download_folder = "imagens"

# Certifique-se de que a pasta de download exista ou crie-a
if not os.path.exists(download_folder):
    os.mkdir(download_folder)

# Faça uma solicitação HTTP para o site
response = requests.get(site_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    img_tags = soup.find_all("img")

    for img_tag in img_tags:
        img_url = img_tag.get("src")
        if img_url:
            img_url = urljoin(site_url, img_url)
            img_name = os.path.basename(img_url)
            img_path = os.path.join(download_folder, img_name)

            # Faça o download da imagem
            img_data = requests.get(img_url).content
            with open(img_path, "wb") as img_file:
                img_file.write(img_data)
            print(f"Baixando: {img_url}")

    print("Download de imagens concluído.")
else:
    print(f"Não foi possível acessar o site. Status code: {response.status_code}")
