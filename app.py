import base64
import os

from flask import Flask, render_template, request

app = Flask(__name__)

frame_count = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_frame', methods=['POST'])
def process_frame():
    frame_data = request.get_json()['frame']
    save_frame_as_image(frame_data)
    return 'Frame received'


def save_frame_as_image(frame_data):
    global frame_count
    # Create a directory to store the frames if it doesn't exist
    if not os.path.exists('frames'):
        os.makedirs('frames')

    # Decode the base64-encoded frame data and save it as an image
    frame_image_data = base64.b64decode(frame_data.split(',')[1])
    with open(f'frames/frame{frame_count}.jpg', 'wb') as file:
        file.write(frame_image_data)
    frame_count += 1


if __name__ == '__main__':
    app.run()
