import cv2
import os
from natsort import natsorted, ns
image_folder = 'inference_frames'
video_name = 'video.avi'
images = [img for img in natsorted(os.listdir(image_folder), key=lambda y: y.lower())
 if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()