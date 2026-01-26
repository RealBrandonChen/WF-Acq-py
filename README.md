# Microscope Random Acquisition Control

This project contains a Python script `Acquisition.py` that utilizes `pycro-manager` to control a microscope system (specifically targeting ASI M2000 stage and Dhyana camera) for a random movement acquisition cycle.

## Prerequisites

1.  **Micro-Manager**: Ensure Micro-Manager (2.0-gamma or later recommended) is installed and running.
2.  **Hardware Configuration**:
    *   ASI M2000 Stage (or compatible XY stage).
    *   Dhyana Camera (or compatible camera).
    *   Enable the "Pycro-manager" server in Micro-Manager (Tools > Options > Run server on port 4827).
3.  **Python Environment**: Install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Functionality

The script performs the following:
1.  Connects to the running Micro-Manager instance.
2.  Identifies the default Camera and XYStage devices.
3.  Records the initial stage position.
4.  Runs a specified number of acquisition rounds (default: 5).
5.  In each round:
    *   Moves the stage to 10 random positions within a defined range (default: +/- 100 microns).
    *   Captures an image at each position.
6.  Returns the stage to the initial position after each round of 10 images.

## Usage

ensure Micro-Manager is running and the server is active, then run:

```bash
python Acquisition.py
```

## Logs
The script outputs progress to the console, including current stage coordinates and image capture status.
