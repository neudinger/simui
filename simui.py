# %%
import os
import time
import numpy as np
from dataclasses import dataclass
from typing import Optional
from imgui_bundle import imgui, implot, imgui_md, hello_imgui, immvision, immapp
from typing import Any

if os.getenv("XDG_SESSION_TYPE") == "wayland" and not os.getenv("PYOPENGL_PLATFORM"):
    os.environ["PYOPENGL_PLATFORM"] = "x11"


@dataclass
class AppState:
    is_running: bool = True
    current_frame: Optional[np.ndarray[Any, np.dtype[np.float64]]] = None


app_state = AppState()


def readCurrentFrame(
    meshgrid_size_x: int = 200, meshgrid_size_y: int = 100
) -> np.ndarray[Any, np.dtype[np.float64]]:
    index = int(time.time() * 10) % 100
    x, y = np.meshgrid(list(range(meshgrid_size_x)), list(range(meshgrid_size_y)))
    out = (
        np.exp(-(x**2 + (y - 50) ** 2) / 400)
        + np.exp(-((x - 199) ** 2 + (y - 50) ** 2) / 400)
        + np.exp(
            -((x - 2 * index) ** 2 + (y - 50 + np.sin(index / 10.0) * 40) ** 2) / 1000
        )
    )
    return out.astype(np.float32)


def update_simulation() -> None:
    """Updates the data if the simulation is running."""
    if app_state.is_running or app_state.current_frame is None:
        app_state.current_frame = readCurrentFrame()


def gui_left_panel() -> None:
    """Left Panel: Controls and Info"""
    imgui_md.render_unindented("## Controls")

    # Start/Stop Button
    button_label = "Stop Simulation" if app_state.is_running else "Resume Simulation"
    if imgui.button(button_label, size=imgui.ImVec2(-1, 0)):
        app_state.is_running = not app_state.is_running

    # Exit Button
    if imgui.button("Exit Application", size=imgui.ImVec2(-1, 0)):
        hello_imgui.get_runner_params().app_shall_exit = True

    imgui.separator()

    imgui_md.render_unindented(
        """
        ### Layout Info
        This layout uses **Docking**.
        
        - **Left**: Fixed controls
        - **Right**: Resizable visualization
        
        Try dragging the separator between this panel and the image!
        """
    )


def gui_right_panel() -> None:
    """Right Panel: Image and Plots"""
    frame = app_state.current_frame
    if frame is None:
        return

    x_profile = np.mean(frame, axis=0)
    y_profile = np.mean(frame, axis=1)
    x_coords = np.arange(len(x_profile), dtype=np.float32)
    y_coords = np.arange(len(y_profile), dtype=np.float32)

    image_params: immvision.ImageParams = immvision.ImageParams(
        image_display_size=(600, 300),
        show_grid=True,
        show_options_button=False,
        show_zoom_buttons=False,
        show_options_panel=False,
        colormap_settings=immvision.ColormapSettingsData(
            colormap="Parula", colormap_scale_min=0.0, colormap_scale_max=1.0
        ),
    )
    immvision.image("Live View", frame, image_params)
    imgui.same_line()

    if implot.begin_plot(
        "##YProfile", size=imgui.ImVec2(-1, 0)
    ):  # -1 width, 0 height (auto)
        implot.setup_axes("Y Coordinate", "Intensity")
        implot.plot_line(label_id="Y-Axis Mean", xs=y_coords, ys=y_profile)
        implot.plot_line(label_id="X-Axis Mean", xs=x_coords, ys=x_profile)
        implot.end_plot()

    imgui.dummy(imgui.ImVec2(0, 10))  # Spacer with dummy widget

    imgui.separator()
    imgui.text("Real-time Profiles")

    if implot.begin_plot(
        title_id="Average X-Axis Profile", size=hello_imgui.em_to_vec2(40, 20)
    ):
        implot.setup_axes("X Coordinate", "Mean Intensity")
        implot.plot_line(label_id="Profile", xs=x_coords, ys=x_profile)
        implot.end_plot()

    imgui.same_line()

    if implot.begin_plot(
        title_id="Average Y-Axis Profile", size=hello_imgui.em_to_vec2(40, 20)
    ):
        implot.setup_axes("Y Coordinate", "Mean Intensity")
        implot.plot_line(label_id="Profile", xs=y_coords, ys=y_profile)
        implot.end_plot()


def main() -> None:
    runner_params = hello_imgui.RunnerParams()

    # runner_params.app_window_params.borderless = True
    # runner_params.app_window_params.resizable = False

    runner_params.app_window_params.window_title = "Simui camera_profile_viewer"
    runner_params.app_window_params.window_geometry.size = (1700, 1500)

    runner_params.imgui_window_params.default_imgui_window_type = (
        hello_imgui.DefaultImGuiWindowType.provide_full_screen_dock_space
    )
    runner_params.imgui_window_params.enable_viewports = True

    split = hello_imgui.DockingSplit()
    split.initial_dock = "MainDockSpace"
    split.new_dock = "LeftDock"
    split.direction = imgui.Dir.left
    split.ratio = 0.25

    runner_params.docking_params.docking_splits = [split]

    left_window = hello_imgui.DockableWindow()
    left_window.label = "Control Panel"
    left_window.dock_space_name = "LeftDock"
    left_window.gui_function = gui_left_panel
    left_window.can_be_closed = False  # Keep controls always open

    right_window = hello_imgui.DockableWindow()
    right_window.label = "Visualization"
    right_window.dock_space_name = "MainDockSpace"
    right_window.gui_function = gui_right_panel
    right_window.can_be_closed = False

    runner_params.docking_params.dockable_windows = [left_window, right_window]

    runner_params.callbacks.before_imgui_render = update_simulation

    addons = immapp.AddOnsParams()
    addons.with_implot = True
    addons.with_markdown = True

    immapp.run(runner_params, add_ons_params=addons)


if __name__ == "__main__":
    main()
