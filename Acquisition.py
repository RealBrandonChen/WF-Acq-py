import time
import random
import numpy as np
from pycromanager import Core

class MicroscopeAcquisition:
    def __init__(self):
        """
        Initialize the acquisition system by connecting to the Micro-Manager Core.
        """
        print("Connecting to Micro-Manager Core...")
        try:
            self.core = Core()
        except Exception as e:
            print(f"Error connecting to Micro-Manager: {e}")
            print("Please ensure Micro-Manager is running and the server is enabled (Tools > Options > Run server on port 4827).")
            raise

        self.xy_stage = self.core.get_xy_stage_device()
        self.camera = self.core.get_camera_device()
        
        if not self.xy_stage:
            print("Warning: No default XY Stage found.")
        else:
            print(f"Using XY Stage: {self.xy_stage}")
            
        if not self.camera:
            print("Warning: No default Camera found.")
        else:
            print(f"Using Camera: {self.camera}")

        self.start_x = 0.0
        self.start_y = 0.0
        # Get initial position
        if self.xy_stage:
            self.start_x = self.core.get_x_position(self.xy_stage)
            self.start_y = self.core.get_y_position(self.xy_stage)
            print(f"Initial Position recorded: X={self.start_x}, Y={self.start_y}")

    def move_to_random_loc(self, range_um=100):
        """
        Move the stage to a random position within +/- range_um of the current position.
        Note: The user requirement implies moving to a new position. 
        We'll use a random delta from the START position to keep it bound, 
        or from current. Let's do random offset from START to avoid drifting too far.
        """
        if not self.xy_stage:
            print("No stage to move.")
            return

        # Generate random offsets
        dx = random.uniform(-range_um, range_um)
        dy = random.uniform(-range_um, range_um)
        
        target_x = self.start_x + dx
        target_y = self.start_y + dy
        
        print(f"Moving to: X={target_x:.2f}, Y={target_y:.2f}")
        try:
            self.core.set_xy_position(self.xy_stage, target_x, target_y)
            self.core.wait_for_device(self.xy_stage)
        except Exception as e:
            print(f"Error moving stage: {e}")

    def acquire_image(self):
        """
        Snap an image from the camera.
        """
        if not self.camera:
            print("No camera to acquire image.")
            return

        print("Acquiring image...")
        try:
            self.core.snap_image()
            tagged_image = self.core.get_tagged_image()
            # pixels = np.reshape(tagged_image.pix, newshape=[tagged_image.tags['Height'], tagged_image.tags['Width']])
            print("Image acquired.")
            # In a real scenario, we might save 'pixels' here using tifffile or similar.
        except Exception as e:
            print(f"Error acquiring image: {e}")

    def return_to_start(self):
        """
        Return the stage to the recorded initial position.
        """
        if not self.xy_stage:
            return

        print(f"Returning to start: X={self.start_x}, Y={self.start_y}")
        try:
            self.core.set_xy_position(self.xy_stage, self.start_x, self.start_y)
            self.core.wait_for_device(self.xy_stage)
        except Exception as e:
            print(f"Error returning to start: {e}")

    def run_acquisition_cycle(self, num_rounds=5, moves_per_round=10):
        """
        Run the main acquisition loop.
        """
        print(f"Starting acquisition: {num_rounds} rounds, {moves_per_round} moves/round.")
        
        for r in range(num_rounds):
            print(f"--- Round {r+1}/{num_rounds} ---")
            
            for m in range(moves_per_round):
                print(f"Move {m+1}/{moves_per_round}")
                self.move_to_random_loc()
                self.acquire_image()
                # Optional small delay
                time.sleep(0.1)
            
            self.return_to_start()
            print("Round complete, returned to start.")
            time.sleep(1) # Pause between rounds

if __name__ == "__main__":
    try:
        acq = MicroscopeAcquisition()
        # You can adjust parameters here as needed
        acq.run_acquisition_cycle(num_rounds=5, moves_per_round=10)
        print("Acquisition process finished successfully.")
    except Exception as e:
        print(f"An error occurred during execution: {e}")
