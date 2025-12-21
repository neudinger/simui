def make_exe():
    # 1. Get the default Python distribution (standard Python library)
    policy = dist.make_python_packaging_policy()
    policy.resources_location_fallback = "filesystem-relative:lib"
    dist = default_python_distribution()

    # 2. Configure the interpreter startup
    # This tells the app to import 'main.py' and run the 'run()' function inside it
    python_config = dist.make_python_interpreter_config()
    python_config.run_command = "import simui; simui.run()"

    # 3. Define the executable wrapper
    exe = dist.to_python_executable(
        name="simui",
        config=python_config,
        packaging_policy=policy,
    )

    # 4. Add your Python source code
    # Scans the current directory (".") for the "main" module (main.py)
    exe.add_python_resources(exe.read_package_root(
        path=".",
        packages=["simui"]
    ))

    # exe.add_python_resources(exe.pip_install(["."]))
    
    return exe

# 5. Register the build target so PyOxidizer knows what to build
register_target("exe", make_exe)

# 6. Finalize targets (Standard boilerplate)
resolve_targets()