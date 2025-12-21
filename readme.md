# Build and install dependencies

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Description

Simui is a simple application to visualize the profiles of the camera frames with ImGui and ImPlot for desktop and web and mobile platforms. The python code is based on the ImGui Bundle. The goal is to show how to use ImPlot and ImGui in a python project, and it portability in web view with pyodide.

## Visualise now

Just open the index.html file in your browser or click here -> [simui](https://neudinger.github.io/simui).

Wait a bit for the Pyodide to load and then it will start the simulation.

Look at the source code of the index.html file to see how to use the python code in the web version.

## Install uv python package manager and environment

Source: https://astral.sh/uv/

> An extremely fast Python package and project manager, written in Rust.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Run the simulation

#### Install dependencies and create a virtual environment

```bash
export UV_LINK_MODE=copy
# This will automatically install the dependencies and copy them to the project in to the venv
uv sync
source .venv/bin/activate
```

#### Run the simulation with python interpreter

```bash
python simui.py
```

### Package the simulation to a single executable file

It will compile the python code into a single executable file.

This will create a single executable file that can be run on any computer don't need python installed.

#### Install dependencies and create a virtual environment

```bash
export UV_LINK_MODE=copy

# This will automatically install the dependencies and copy them to the project in to the venv

uv sync
source .venv/bin/activate
```

```bash
export PATH=$PATH:$PWD/.venv/bin/

imgui_bundle_asset_path=`python -c "import imgui_bundle, os; print(os.path.join(os.path.dirname(imgui_bundle.__file__), 'assets'))"`
PYTHONOPTIMIZE=3

pyinstaller \
  --onefile \
  --noconsole \
  --windowed \
  --add-data "${imgui_bundle_asset_path}:imgui_bundle/assets" \
  --name "simui" \
  simui.py
```

#### Run the simulation with the single executable file

```bash
./dist/simui
```

#### Make a standalone executable statically linked to the system libraries

Now we have a single executable file that can be run on any computer.

But it is not statically linked to the system libraries.

```bash
ldd ./dist/simui
        linux-vdso.so.1 (0x00007907122e2000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007907122b6000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x0000790712298000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x0000790712293000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x0000790712000000)
    /lib64/ld-linux-x86-64.so.2 (0x00007907122e4000)
```


We can use the staticx tool to make a standalone executable that is statically linked to the system libraries.

- [python-staticx](https://pypi.org/project/staticx/)

```bash
sudo apt install patchelf
```

```bash
staticx ./dist/simui ./dist/simui_static
```

Now we have a single executable file that is statically linked to the system libraries.

```bash
ldd ./dist/simui_static
        not a dynamic executable
```

```bash
./simui_static
```

### Docker

```bash
xhost +local:docker

docker build . -t simui:latest
```

X11 forwarding

```bash
docker run -it --rm \
    --net=host \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $HOME/.Xauthority:/root/.Xauthority \
    simui:latest
```

Wayland forwarding

```bash
docker run -it --rm \
    -e XDG_RUNTIME_DIR=/tmp \
    -e WAYLAND_DISPLAY=$WAYLAND_DISPLAY \
    -e DISPLAY=$DISPLAY \
    -v $XDG_RUNTIME_DIR/$WAYLAND_DISPLAY:/tmp/$WAYLAND_DISPLAY \
    -e QT_QPA_PLATFORM=wayland \
    -e GDK_BACKEND=wayland \
    simui:latest
```

Adapt with `--device /dev/...`

## Pyiodide for web

source: https://pyodide.com/

It is a Python distribution for the web, built with WebAssembly.

Just open the index.html file in your browser.

Dont need a server to run it your web browser will make the simulation and computation and use the GPU if available.

Imgui_bundle, ImPlot, ImGui_Md, Hello_imgui, Immvision, Immapp, numpy, and ImGui are all available in the web version.

## Source dependencies used

- [numpy](https://numpy.org/)
- [imgui_bundle](https://github.com/pthom/imgui_bundle)
- [immapp](https://github.com/pthom/imgui_bundle)
- [implot](https://github.com/epezent/implot)
- [imgui_md](https://github.com/pthom/imgui_md)
- [hello_imgui](https://github.com/pthom/hello_imgui)
- [immvision](https://github.com/pthom/immvision)
- [python-staticx](https://github.com/indygreg/python-staticx)
- [pyinstaller](https://pyinstaller.org/)

## Perspectives

### ImGui

Use [Fiatlight](https://pthom.github.io/fiatlight_doc/flgt/intro.html) for faster UI developement.

### Packages

[PyInstaller](https://pyinstaller.org/en/stable/) or [PyOxidizer](https://github.com/indygreg/PyOxidizer) can be used to compile the python code into a single executable file.

Shaders (GLSL) can be used to use gpu acceleration, also interoperability with vulkan, metal, dx12, OpenCV, and CUDA is Possible.

## Possible Performance Improvements

[cythonizer](https://github.com/TechLearnersInc/cythonizer) and [pyoxidizer](https://github.com/indygreg/PyOxidizer) can be used to compile the python code into a single executable file.

Write the code in cython and compile it to c code.

### ImGui

- [imgui_bundle_playground](https://traineq.org/imgui_bundle_online/projects/imgui_bundle_playground/)
- [imgui_bundle quickstart](https://pthom.github.io/imgui_bundle/quickstart.html#_widgets)
- [imgui_python_intro](https://github.com/pthom/imgui_bundle/blob/main/docs/docs_md/imgui_python_intro.md)
- [youtube imgui_bundle tutorial](https://www.youtube.com/channel/UCopFrJZ1jWMf2Fw7AG52JYQ)