"""
Utility helpers
---------------
- Seed control
- Simple logging shim
"""
import random
import numpy as np

def set_seed(seed: int = 42):
    random.seed(seed)
    np.random.seed(seed)

class Logger:
    @staticmethod
    def info(msg: str):
        print(f"[INFO] {msg}")
    @staticmethod
    def warn(msg: str):
        print(f"[WARN] {msg}")
    @staticmethod
    def error(msg: str):
        print(f"[ERROR] {msg}")
