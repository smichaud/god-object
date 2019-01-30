import sys
import os
import time
import datetime
import requests
import cv2

HOST_IP = "http://172.16.20.100:5000"
API_PATH = "/api/photo"
URL = HOST_IP + API_PATH
VIDEO_DEVICE = 0

# Basically only need to upload images to the "server"
# Could get the server for setting update... get before next post or simply return params in the post response
def main(argv):
    time_in_seconds_between_frames = 10
    max_images_count = 50
    images_count = 0

    start_time = time.time()
    last_post_time = start_time
    cam = cv2.VideoCapture(VIDEO_DEVICE)
    while images_count < max_images_count:
        current_time = time.time()
        if current_time - last_post_time > time_in_seconds_between_frames:
            images_count = images_count + 1
            last_post_time = time.time()

            s, img = cam.read()
            formatted_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
            filename = formatted_datetime + ".jpg"
            filepath = "../data_device/" + filename
            cv2.imwrite(filepath, img)

            file = open(filepath, "rb")
            files = {"file": file}
            response = requests.post(URL, files=files)
            response_data = response.json()

            os.remove(filepath)


if __name__ == "__main__":
    main(sys.argv[1:])
