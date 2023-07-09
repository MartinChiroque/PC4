
import requests

url = 'https://images.unsplash.com/photo-1591160690555-5debfba289f0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=464&q=80'

def main():

    try:
        # Conexion a url
        response = requests.get(URL)
    except requests.RequestException:
        raise Exception('A ocurrido un error en la conexión a la url')

    # descarga imagen
    with open('pastor.jpg', 'wb') as f:
        f.write(response.content)
    pass

if __name__ == '__main__':
    main()