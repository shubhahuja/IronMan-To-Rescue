import cx_Freeze

executables=[cx_Freeze.Executable("flight_simulator.py")]

cx_Freeze.setup(
    name="IronMan Racer",
    options={"build_exe":{"packages":["pygame"],
    "include_files": ["fireball.png","ironmanflysmall.png","rockbg.png"]}},
    executables= executables
    )



