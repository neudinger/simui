cmake_minimum_required(VERSION 3.16)
project(MyWebSim)


set(IMMVISION_FETCH_OPENCV ON CACHE BOOL "" FORCE)
set(IMGUI_BUNDLE_BUILD_PYTHON ON CACHE BOOL "" FORCE)

include(FetchContent)
FetchContent_Declare(
  imgui_bundle
  GIT_REPOSITORY https://github.com/pthom/imgui_bundle.git
  GIT_TAG        v1.92.5
)
FetchContent_MakeAvailable(imgui_bundle)

# apt install libx11-dev libxcursor-dev libxrandr-dev libxinerama-dev libxi-dev libgl1-mesa-dev
# apt install libglfw3-dev libopencv-dev python3-dev python3-opencv python3-nanobind python3-pybind11
# emcmake cmake -B build -DCMAKE_BUILD_TYPE=MinSizeRel
# cmake -B build -DCMAKE_BUILD_TYPE=MinSizeRel
imgui_bundle_add_app(MyWebSim simui.cc)
