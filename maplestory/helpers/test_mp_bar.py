import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from maplestory_telemetry import get_mp_percentage
import time

import time
while True:
    time.sleep(1)
    print(get_mp_percentage())
