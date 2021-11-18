"""
to prepare the aladin outputs as the forcing of WRF
"""

__version__ = f'Version 2.0  \nTime-stamp: <2021-05-15>'
__author__ = "ChaoTANG@univ-reunion.fr"

import os
import sys
import hydra
import numpy as np
import scipy
import matplotlib.pyplot as plt
import pandas as pd
import xarray as xr
from omegaconf import DictConfig
import GEO_PLOT


@hydra.main(config_path="configs", config_name="scale_interaction")
def forcing(cfg: DictConfig) -> None:

    print(f'project is staring ...')

    if cfg.job.loading_model_setup_from_ccub:
        os.system("./src/get_model_setup.sh")


if __name__ == "__main__":
    sys.exit(forcing())
