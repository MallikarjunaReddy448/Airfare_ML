import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import Logger
import os

from utils import save_object
