EN|[CN](README.zh.md)
# GraphShow Tool
-----------------------------------------------
## Function
- Generally, the Graph.config file configuration may vary with services. There are many engines and the service logic is complex. It is difficult to understand the logical structure of the system by reading the config file. This tool displays the config file in graphics by using the visualization technology, which helps you to understand the logical structure of the service system.

## Supported Systems

Operator Systems: Ubuntu16.04 and CentOS7.4

CPU Architecture: x86_64 and aarch64 

## Installation Environment

- Ubuntu16.04/CentOS7.4
- python3
- pip3
- Graphviz library and dependency library
```
pip3 install graphviz
sudo apt-get(yum) install graphviz
sudo apt-get(yum) install xdg-utils
```

## Usage Instructions
- The converted Graph.config file needs to be placed in the demo folder, then run the following command in the root directory of the project:
``` python
python3 ./draw.py ./demo/graph_video_struct.config
```
- Result Files
Generate the EngineFlow.gv.svg file in the project root directory and the EngineFlow.gv file in the intermediate representation of the DOT.

- Result Display：
  ![result](./img/demo.png)

  In the above figure, the "HOST" box indicates that the blue boxes are the host side engines, and the "DEVICE" box indicates that the green boxes are the device side engines.

## Notice

- Visible images are saved as vector images in .svg format by default. Visible images can be opened with Internet Explorer browser. If the image is too large, you can right-click the image displayed on the browser, save the image as a .png or .jpeg image, and then view the image using the image viewer.

