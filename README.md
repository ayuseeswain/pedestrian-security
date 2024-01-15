# Pedestrian Security - Cyber Threats and Risk Mitigation in Autonomous Driving

## Introduction
Welcome to the **Pedestrian Security** repository, a pivotal component of the **Cyber Threats and Risk Mitigation in Autonomous Driving** project. This repository focuses on enhancing the security of autonomous driving systems, particularly regarding pedestrian safety. We aim to develop and refine technologies to identify and mitigate potential cyber threats in autonomous driving environments, ensuring safer interactions for pedestrians.

## Project Overview
The "Pedestrian Security" project encompasses several key components:

### YOLO Model
Incorporates a state-of-the-art **You Only Look Once (YOLOv8)** model for real-time object detection, specially tailored to identify actual pedestrians and posters having people's image in an autonomous driving context.

### Sensor Fusion Code
This module integrates data from multiple sensors like RGB camera and LiDAR to create a comprehensive understanding of the vehicle's surroundings, essential for proper validation of objects detected by camera-based syetms like YOLO, in order to achieve accurate and reliable object classification.

### Spatial Analysis Post Fusion
Involves post-processing of sensor fusion data, including statistics-based spatial analysis to evaluate and interpret the data to classify 3D pedestrian and 2D posters, in order to counteract adversarial attacks used to confuse camera based systems in AVs. This will enhance the decision-making processes in autonomous driving systems.

### Dataset Generation
Utilizes both the **Carla Autonomous Driving Simulator** and the `simple_image_download` Python library to generate dataset of pedestrians and posters. The dataset provides a diverse range of scenarios and conditions, offering robust training and testing material for our models.

### Codebase
The code for sensor fusion and spatial analysis is contained within a single Jupyter Notebook (`.ipynb`) file, making it easier to understand the workflow and methodologies employed in this project.

### Installation

1. Download the Carla binaries and additional maps for Windows from [Carla Releases](https://github.com/carla-simulator/carla/releases).

2. Install Miniconda from [Miniconda Installation](https://docs.conda.io/en/latest/miniconda.html).

3. Open a "standard" Windows command prompt.

4. Create a Conda environment for Carla:
   ```shell
   conda create -n carla python=3.7

5. Activate the Conda environment.
   ```shell
   conda activate carla

6. Install the Python CARLA client library. This can be found as a .whl file in the pythonapi\carla\dist directory of the Carla distribution. Replace carla-0.9.14-cp37-cp37m-win_amd64.whl with the correct filename.
   ```shell
   pip3 install carla-0.9.14-cp37-cp37m-win_amd64.whl

7. Navigate to the pythonapi\examples directory.

8. Install the required dependencies for running Carla examples.
   ```shell
   pip install -r requirements.txt

9. Start Carla by running CarlaUE4.exe from the directory where the Carla distribution was unzipped.

10. Generate traffic by running the following Python script in the pythonapi\examples directory. You will now be able to see vehicles moving in the city.
    ```shell
    python generate_traffic.py

11. To install YOLOv8, ensure that PyTorch is available and CUDA is enabled.
    ```shell
    import torch
    print(torch.__version__)
    print(torch.cuda.is_available())

12. Pip install the ultralytics package including all requirements in a Python>=3.8 environment with PyTorch>=1.8.
    ```shell
    pip install ultralytics

13. To train the YOLOv8, run the following script on command prompt:
    ```shell
    yolo task=detect mode=train epochs=300 data=data_custom.yaml model=yolov8m.pt imgsz=640 batch=6

14. Once the training is over, go to \runs\detect\train\weights, copy the best.pt model to the source directory and run the following script on command prompt:
    ```shell
    yolo task=detect mode=predict model=best.pt show=True conf=0.5 source="<path\to\test\image\file\or\folder>" save_txt=True

15. For more information regarding the model and model training, visit the following links:
- [Ultralytics Documentation](https://docs.ultralytics.com)
- [Ultralytics Community](https://community.ultralytics.com)
- [Ultralytics Repository](https://github.com/ultralytics/ultralytics)