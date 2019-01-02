import sys
import time
import requests

HOST_IP = "http://0.0.0.0:5000"
API_PATH = "/api/photo"
URL = HOST_IP + API_PATH

# Basically only need to upload images to the "server"
def main(argv):
    last_post_time = time.time()
    file = open("/home/smichaud/Desktop/tux.jpg", "rb")
    files = {"file": file}
    response = requests.post(URL, files=files)
    print(response.status_code, response.reason)


if __name__ == "__main__":
    main(sys.argv[1:])
