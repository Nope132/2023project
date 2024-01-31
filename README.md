# homework:SPH 流体模拟
这是在笔者大二阶段曾与另外一同学制作基础上进行的进一步开发，借鉴了清华大学姚班的计算机图像学课程并进一步复现，详见致谢

<figure align="center">
  <img src="./pipeline.png" alt="pipeline of our framework" width="96%">

</figure>

我们的SPH（Smoothed Particle Hydrodynamics）模拟框架详细工作流程如下所示：

1. **准备场景阶段：**
   用户在此阶段定义流体和刚体的属性，同时设置模拟参数。这一阶段是模拟的起始点。

2. **模拟阶段：**
   - **引力，黏性和压力力的应用：**
     顺序应用引力、黏性和压力力，这是模拟过程的核心。
   - **流体和刚体的动态更新：**
     针对流体和刚体进行动态更新，包括对粘度（标准和隐式）和压力管理（WCSPH、PCISPH和DFSPH）的各种求解器的应用。

3. **后处理阶段：**
   - **流体粒子的表面重建：**
     使用SplashSurf进行流体粒子的表面重建，以确保场景的准确呈现。
   - **在Blender中渲染场景：**
     利用Blender丰富的社区资源，将场景渲染出来。这一阶段完成后，用户可以享受Blender提供的丰富场景创建功能。

在整个过程中，我们面临了一些挑战，尤其是在正确实现IISPH和将PBF集成到我们的统一框架中时。这些挑战需要仔细的调试和解决，以确保模拟的准确性和稳定性。
## 功能
### SPH算法
自由表面流的弱可压缩SPH（WCSPH）

预测校正不可压缩SPH（PCISPH）

无发散光滑粒子流体动力学（DFSPH）

### 流体-刚体相互作用力

用于不可压缩SPH的通用刚性流体联轴器

### 粘度

标准粘度

物理一致性SPH流体隐式粘度求解器

### 刚性解算器

子弹物理引擎

### SPH曲面重建

飞溅冲浪

### Rendering

blender

## Heighlights
### 大规模的流体模拟

<figure align="center">
  <img src="./examples/large_scale_fluid.gif" alt="Large scale fluid simulation with over a million particles" width="96%">
  <figcaption>由1.23M颗粒组成的流体的大规模流体模拟。</figcaption>
</figure>


## 刚体流体耦合体

<figure align="center">
  <img src="./examples/coupling.gif" alt="Rigid-fluid coupling"width=96%">
  <figcaption>模拟密闭空间中的一个流体对象和九个刚性对象。</figcaption>
</figure>


## 高粘性流体

<figure align="center">
  <img src="./examples/high_viscosity_fluid.gif" alt="Fluid with extremely high viscosity" width="96%">
  <figcaption>模拟具有极高粘度的流体。</figcaption>
</figure>


## 屈服效应

<figure align="center">
  <img src="./examples/buckling_effect.gif" alt="Realistic simulation of buckling effect" width="96%">
  <figcaption>屈服效应模拟</figcaption>
</figure>


## 蜷曲效果

<figure align="center">
  <img src="./examples/coiling_effect.gif" alt="Realistic simulation of coiling effect" width="96%">
  <figcaption>蜷曲效果模拟</figcaption>
</figure>

## Linux的安装

### Python 环境

```bash
git clone https://github.com/jason-huang03/SPH_Project.git
cd SPH_Project
conda create --name SPH python=3.9
conda activate SPH
pip install -r requirements.txt
```

该代码已经在：

Ubuntu 22.04

Python 3.9.12

CUDA 12.2

NVIDIA A100 GPU

上进行了测试。



### 安装Vulkan SDK（自选）

您可能需要Vulkan SDK来运行代码。这里我们提供了一种在Linux上安装Vulkan SDK的方法，无需管理员许可。

```bash
wget https://sdk.lunarg.com/sdk/download/latest/linux/vulkan-sdk.tar.gz -O vulkan-sdk.tar.gz


sudo mkdir -p /opt/vulkan-sdk
sudo tar -xvf vulkan-sdk.tar.gz -C /opt/vulkan-sdk # You can extract to your customized place. Change following lines accordingly.

VULKAN_SDK_VERSION=$(ls /opt/vulkan-sdk/ | grep -v "tar.gz")

echo "VULKAN_SDK_VERSION: $VULKAN_SDK_VERSION" # should be something like 1.3.268.0
```

然后可以在你的 `~/.bashrc` 文件.

```bash
# add following line in your ~/.bashrc
# suppose VULKAN_SDK_VERSION has a value

export VULKAN_SDK=/opt/vulkan-sdk/$VULKAN_SDK_VERSION/x86_64
export PATH="$PATH:$VULKAN_SDK/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$VULKAN_SDK/lib"

# possibly you will need this line
export VK_LAYER_PATH="$VULKAN_SDK/etc/vulkan/explicit_layer.d"

```

之后，您可以通过运行以下命令来检查是否已成功安装Vulkan SDK `source ~/.bashrc` 然后 `vulkaninfo` 在终端中



### 安装防溅板（自选）
您可以参考[official document](https://github.com/InteractiveComputerGraphics/splashsurf)飞溅冲浪的细节。这里我们提供了一种在Linux上安装splashsurf的方法，无需管理员许可。
```bash
# install rust toolchain
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# install splashsurf
cargo install splashsurf
```



### 安装搅拌器（自选)
您可以参考[official website](https://www.blender.org/)搅拌机的更多细节。在这里，我们提供了一种在没有管理员许可的情况下在LInux上安装搅拌器的方法。
```bash
# download blender 3.6 Linux package from https://www.blender.org/download/lts/3-6/

# uncompressed the .tar.gz file
tar -xf blender-3.6.7-linux-x64.tar.xz
```

Add the following line in your `~/.bashrc` file.

```bash
# update the $PATH variable
# add the following line in ~/.bashrc file
export PATH=$PATH:~/blender-3.6.7-linux-x64/
```

渲染脚本用搅拌器3.6.7测试，搅拌器4.0似乎不兼容。


## 使用方法

为了快速入门，请尝试以下命令，并确保在`json`场景配置
```bash
python run_simulation.py --scene ./data/scenes/dragon_bath_dfsph.json
```

要可视化结果，可以运行以下命令将图像制作成视频。这些原始图像来自 Taichi GGUI API.

```bash
python make_video.py --input_dir ./dragon_bath_dfsph_output \
--image_name raw_view.png --output_path --video.mp4 --fps 30
```

要使`.ply`粒子文件到`.OBJ`文件进行渲染，可以使用以下命令进行曲面重建：
```bash
python surface_reconstruction.py --input_dir ./dragon_bath_dfsph_output --num_workers 2
```

这将打开 `num_workers` 用[splashsurf](https://github.com/InteractiveComputerGraphics/splashsurf).进行曲面重建的过程

然后可以使用[blender](https://www.blender.org/)。我们建议您首先使用图形用户界面创建场景，设置材质、照明、摄影机、渲染参数并添加其他静态对象。然后可以将场景另存为·.blend·文件。通过此操作，可以通过运行以下命令渲染整个模拟过程
```bash
CUDA_VISIBLE_DEVICES=0 python render.py --scene_file ./scene.blend \
--input_dir ./dragon_bath_dfsph_output --num_workers=1 --device_type OPTIX
```
渲染脚本可以将渲染作业放在多个gpu上。可以根据可用的设备可以设置`CUDA_VISIBLE_DEVICES`和 `num_workers` 



## 鸣谢

此项目基于以下存储库构建：

+ [Taichi](https://github.com/taichi-dev/taichi)
+ [Bullet](https://github.com/bulletphysics/bullet3)
+ [SPH Taichi](https://github.com/erizmr/SPH_Taichi)
+ [SPlisHSPlasH](https://github.com/InteractiveComputerGraphics/SPlisHSPlasH)
+ [Splash Surf](https://github.com/InteractiveComputerGraphics/splashsurf)
+ [Blender](https://www.blender.org/)

我们感谢这些存储库的所有贡献者的出色工作和开源精神。
