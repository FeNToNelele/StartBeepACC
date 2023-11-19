import sys, winsound, dxcam
from numpy import mean

def main():
    print("Looking for green light. GLHF")
    camera = dxcam.create()
    camera.start(region=(825, 300, 840, 320), target_fps=145)
    screenshot = camera.get_latest_frame()
    pixel_avg = (mean(screenshot[:,:,0]), mean(screenshot[:,:,1]), mean(screenshot[:,:,2]))

    while(pixel_avg[0] >= 17 or pixel_avg[1] <= 195 or pixel_avg[1] >= 226 or pixel_avg[2] >= 17):
        screenshot = camera.get_latest_frame()
        pixel_avg = (mean(screenshot[:,:,0]), mean(screenshot[:,:,1]), mean(screenshot[:,:,2]))
    winsound.Beep(750, 1000)
    sys.exit()

main()