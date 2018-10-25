from cv2 import imencode, waitKey,  destroyAllWindows
from imutils.video import VideoStream
import time, sys

video_stream = VideoStream(resolution=(320, 240)).start()
time.sleep(1)

while(True):
    new_frame = video_stream.read()

    encoded_frame = bytearray(imencode('.jpeg', new_frame)[1])
    frame_size = str(len( encoded_frame ))


    sys.stdout.write('Content-Type: image/jpeg\r\n')
    sys.stdout.write('Content-Length: ' + frame_size + '\r\n\r\n')
    sys.stdout.write( encoded_frame )
    sys.stdout.write('\r\n')

    sys.stdout.write('--informs\r\n')

    if waitKey(1) & 0xFF == ord('q'):
        break

destroyAllWindows()
video_stream.stop()
