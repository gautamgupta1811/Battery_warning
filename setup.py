from cx_Freeze import setup, Executable


exe = Executable(
   script="main code.py",
   base=None,
   targetName="Battery_check.exe"
   )


setup(
    name="Test",
    version="0.1",
    author="Prachi",
    options={"build_exe": {"packages": ["wmi", "os", "getpass"],
            "include_files": ["battery_popup.py", "Battery_check.py"]}},
    description="Helps in checking battery charge percentage to increase battery life",

    executables=[exe])