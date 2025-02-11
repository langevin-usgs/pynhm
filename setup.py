import os
import platform
import setuptools  # noqa
import warnings

from numpy.distutils.misc_util import Configuration
from numpy.distutils.core import setup

pynhm_fortran = str(os.getenv("PYNHM_FORTRAN"))
if pynhm_fortran.lower() == "true":
    pynhm_fortran = True
    if platform.system() == "Windows":
        pynhm_fortran = False
        warnings.warn(
            "Fortran source compilation not enabled on Windows", Warning
        )

else:
    pynhm_fortran = False


config = Configuration("pynhm")

if pynhm_fortran:
    source_dir_names = {
        "hydrology": ["PRMSGroundwater", "PRMSCanopy", "PRMSChannel"]
    }
    for dir, names in source_dir_names.items():
        for name in names:
            config.add_extension(
                f"{name}_f",
                sources=[
                    f"pynhm/{dir}/{name}.pyf",
                    f"pynhm/{dir}/{name}.f90",
                ],
            )


setup(**config.todict(), packages=setuptools.find_packages())
