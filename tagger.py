
import argparse
import requests


def tag(text, server_url):
    response = requests.post(server_url, data={
        "text": text
    })

    return response.json()["text"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Menghubungi server tagger untuk melakukan tagging pada teks input.")
    parser.add_argument("text", help="Teks yang ingin di-tag")
    parser.add_argument('--server', help='URL server tagger')

    args = parser.parse_args()

    server_url = args.server
    if server_url == None:
        server_url = "http://localhost:7000"

    try:
        print(tag(args.text, server_url))
    except Exception as e:
        print("Gagal menghubungi server.")
