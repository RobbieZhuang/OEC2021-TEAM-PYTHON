from constants import *
from exposure import ExposureChance

def initialize_exposures():
    exposures = {}

    for c in CLASSES:
        exposures[c] = ExposureChance(c, CLASS_EXPOSURE_FACTOR)
        transition = c + ' Transition'
        exposures[transition] = ExposureChance(transition, TRANSITION_EXPOSURE_FACTOR, False)

    for ec in ECS:
        exposures[ec] = ExposureChance(ec, EC_EXPOSURE_FACTOR)
        transition = ec + ' Transition'
        exposures[transition] = ExposureChance(transition, TRANSITION_EXPOSURE_FACTOR, False)

    return exposures
    
def run_simluation(exposures, students):
    def have_class():
        for e in exposures:
            

    def ecs():
        pass

    def period_transition():
        pass

    def lunch():
        pass

    have_class()
    period_transition()
    have_class()
    period_transition()
    lunch()
    have_class()
    period_transition()
    have_class()
    period_transition()
    ecs()

    show_exposures()

def show_exposures():
    pass



    
