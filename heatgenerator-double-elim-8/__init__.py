'''Standardized heat structures'''

import logging
from eventmanager import Evt
from HeatGenerator import HeatGenerator, HeatPlan, HeatPlanSlot, SeedMethod
from RHUI import UIField, UIFieldType, UIFieldSelectOption

logger = logging.getLogger(__name__)

def bracket_2e_8(rhapi):
    return [
        HeatPlan(
            rhapi.__("Race") + " 1",
            [
                HeatPlanSlot(SeedMethod.INPUT, 1),
                HeatPlanSlot(SeedMethod.INPUT, 3),
                HeatPlanSlot(SeedMethod.INPUT, 5),
                HeatPlanSlot(SeedMethod.INPUT, 7)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 2",
            [
                HeatPlanSlot(SeedMethod.INPUT, 2),
                HeatPlanSlot(SeedMethod.INPUT, 4),
                HeatPlanSlot(SeedMethod.INPUT, 6),
                HeatPlanSlot(SeedMethod.INPUT, 8)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 3 Lower",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 0),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 0),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 1),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 1)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 4 Upper",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 0),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 0),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 1),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 1)
            ]
        ),
        HeatPlan(
            rhapi.__("Race") + " 5 Lower",
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 2),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 2),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 3, 3),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 4, 3)
            ]
        ),
        HeatPlan(
            rhapi.__("Finals"),
            [
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 3),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 3),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 1, 4),
                HeatPlanSlot(SeedMethod.HEAT_INDEX, 2, 4)
            ]
        )
      
    ]

def bracket_2e_std(rhapi, generate_args):
    if 'standard' not in generate_args:
        return False
    if generate_args['standard'] == 'custom8':
        return bracket_2e_8(rhapi)
    else:
        return False

def register_handlers(args):
    for generator in [
        HeatGenerator(
            "Custom bracket, double elimination",
            bracket_2e_std,
            None,
            [
                UIField('standard', "Spec", UIFieldType.SELECT, options=[UIFieldSelectOption('custom8', "Non regulation 8 pilots"),], value='custom8'),
                UIField('seed_offset', "Seed from rank", UIFieldType.BASIC_INT, value=1),
            ],
        ),
    ]:
        args['register_fn'](generator)

def initialize(rhapi):
    rhapi.events.on(Evt.HEAT_GENERATOR_INITIALIZE, register_handlers)

