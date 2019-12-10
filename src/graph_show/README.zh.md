[EN](README.md)|CN
# GraphShow Tool
-----------------------------------------------
## 功能
- 一般情况下，我们的Graph.config的配置可能根据业务的不同，engine会很多，业务逻辑也会比较复杂。直接看这个config文件，很难一目了然的知道这个系统的逻辑结构。该工具用可视化技术，将config文件用图形的方式显示出来，便于直观，快捷的了解业务系统的逻辑结构。

## 支持的系统

操作系统：Ubuntu16.04 与 CentOS7.4

CPU架构：x86_64 与 aarch64 

## 环境安装

- Ubuntu16.04/CentOS7.4
- python3
- pip3
- 需要先安装Graphviz库及依赖库
```
pip3 install graphviz
sudo apt-get(yum) install graphviz
sudo apt-get(yum) install xdg-utils
```

## 使用说明
- 被转换的 Graph.config 文件放置在 demo 文件夹内，在工程根目录执行命令：
``` python
python3 ./draw.py ./demo/graph_video_struct.config
```
- 结果文件
在项目根目录下生成EngineFlow.gv.svg的文件及DOT中间表示的EngineFlow.gv文件
- 结果展示：
  ![result](./img/demo.png)

  图中 “HOST” 框表示蓝色框是 Host 侧的 Engine, "DEVICE" 框表示绿色框是 Device 侧的 Engine.

## 注意事项

- 可视化图像默认保存为.svg格式的矢量图。可以用IE浏览器打开。如果图像太大，可以在浏览器显示的图像上右键，另存为png或者jpeg等图像格式，再用图片查看器查看。

