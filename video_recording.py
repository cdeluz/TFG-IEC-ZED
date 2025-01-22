
import sys
import pyzed.sl as sl
from signal import signal, SIGINT
import argparse
import os

cam = sl.Camera()


# Handler to deal with CTRL+C properly
def handler(signal_received, frame):
    cam.disable_recording()
    cam.close()
    sys.exit(0)


signal(SIGINT, handler)


def main():
    init = sl.InitParameters()
    init.depth_mode = sl.DEPTH_MODE.NONE  # Set configuration parameters for the ZED
    init.camera_fps = 30
    status = cam.open(init)
    if status != sl.ERROR_CODE.SUCCESS:
        print("Camera Open", status, "Exit program.")
        exit(1)

    i = 0
    while os.path.exists("zed%s.svo" % i):
        i += 1

    svo_file = f'zed{i}.svo'

    recording_param = sl.RecordingParameters(svo_file,
                                             sl.SVO_COMPRESSION_MODE.H264,
                                             30)  # Enable recording with the filename specified in argument
    err = cam.enable_recording(recording_param)
    if err != sl.ERROR_CODE.SUCCESS:
        print("Recording ZED : ", err)
        exit(1)

    runtime = sl.RuntimeParameters()
    print("SVO is Recording, use Ctrl-C to stop.")  # Start recording SVO, stop with Ctrl-C command
    frames_recorded = 0

    while True:
        if cam.grab(runtime) == sl.ERROR_CODE.SUCCESS:  # Check that a new image is successfully acquired
            frames_recorded += 1
            print("Frame count: " + str(frames_recorded), end="\r")


if __name__ == "__main__":
    main()