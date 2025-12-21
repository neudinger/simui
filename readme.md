
# Build and install dependencies

## Visualise now

Just open the index.html file in your browser or click here -> [simui](https://neudinger.github.io/simui).

Wait a bit for the piodide to load and then it will start the simulation.

Look at the source code of the index.html file to see how to use the python code in the web version.

## Install uv python package manager and environment

Source: https://astral.sh/uv/

> An extremely fast Python package and project manager, written in Rust.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

export PYTHONPATH="/media/neudinger/media/zerauth/pyimgui/imgui"

```bash
export UV_LINK_MODE=copy
# This will automatically install the dependencies and copy them to the project in to the venv
uv sync
source .venv/bin/activate
python simui.py
```

## Pyiodide for web

source: https://pyodide.com/

It is a Python distribution for the web, built with WebAssembly.

Just open the index.html file in your browser.

Dont need a server to run it your web browser will make the simulation and computation and use the GPU if available.

Imgui_bundle, ImPlot, ImGui_Md, Hello_imgui, Immvision, Immapp, numpy, and ImGui are all available in the web version.

Imgui is 

## Source dependencies used

- [numpy](https://numpy.org/)
- [imgui_bundle](https://github.com/pthom/imgui_bundle)
- [immapp](https://github.com/pthom/imgui_bundle)
- [implot](https://github.com/epezent/implot)
- [imgui_md](https://github.com/pthom/imgui_md)
- [hello_imgui](https://github.com/pthom/hello_imgui)
- [immvision](https://github.com/pthom/immvision)

## Install dependencies

- imgui_bundle
- implot
- imgui_md
- hello_imgui
- immvision
- immapp


## Perspectives

### ImGui

Use [Fiatlight](https://github.com/fiatjaf/fiatlight) for faster UI generation.

### Packages

[PyInstaller](https://pyinstaller.org/en/stable/) and/or [Nuitka](https://nuitka.net/) or [PyOxidizer](https://github.com/indygreg/PyOxidizer) can be used to compile the python code into a single executable file.

Shaders (GLSL) can be used to use gpu acceleration, also interoperability with vulkan, metal, dx12, OpenCV, and CUDA is Possible.

### ImGui

- https://pthom.github.io/imgui_bundle/quickstart.html#_widgets
- https://github.com/pthom/imgui_bundle
- https://github.com/epezent/implot
- https://www.youtube.com/channel/UCopFrJZ1jWMf2Fw7AG52JYQ
