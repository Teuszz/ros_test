import pyrealsense2 as rs
import numpy as np

class DepthCamera:
    def __init__(self):
        # Configure depth and color streams
        self.pipeline = rs.pipeline()
        config = rs.config()

        # Get device product line for setting a supporting resolution
        pipeline_wrapper = rs.pipeline_wrapper(self.pipeline)
        pipeline_profile = config.resolve(pipeline_wrapper)
        device = pipeline_profile.get_device()
        device_product_line = str(device.get_info(rs.camera_info.product_line))

# M.Sielski###
# Anpassen der "img-size" und Belegung des RGB-Moduls der Kamera unterbinden
        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        #config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
#############

#M.Sielski###
# Ausgabe, dass Kamera bereit und Initialisierung erfolgreich.
        # Start streaming
        print("[INFO] Starting streaming...") 
        self.pipeline.start(config)
        print("[INFO] Camera ready.") 
#############

#M.Sielski###
# Zugriff auf Tiefeninformationen. YOLOv5 verwendet RGB-Modul.
    def get_frame(self):
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        #color_frame = frames.get_color_frame()

        depth_image = np.asanyarray(depth_frame.get_data())
        #color_image = np.asanyarray(color_frame.get_data())
        
        if not depth_frame: #or not color_frame:
            return False, None #, None
        return True, depth_image # color_image
#############

    def release(self):
        self.pipeline.stop()
