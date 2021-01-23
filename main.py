from constants import *
from exposure import ExposureChance

def initialize_exposures():
    exposures = {}

    for c in CLASSES:
        exposures[c] = ExposureChance(c, CLASS_EXPOSURE_FACTOR)
        transition = c + ' Transition'
        exposures[transition] = ExposureChance(transition, TRANSITION_EXPOSURE_FACTOR)

    for ec in ECS:
        exposures[c] = ExposureChance(ec, EC_EXPOSURE_FACTOR)
