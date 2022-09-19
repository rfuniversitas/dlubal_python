import sys
import os
import pytest
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

from RFEM.initModel import Model, SetAddonStatus
from RFEM.enums import AddOn, AluminumMemberRotationalRestraintType, AluminumMemberRotationalRestraintContinuousBeamEffect, AluminumMemberRotationalRestraintPositionofSheeting, AddOn
from RFEM.TypesForAluminumDesign.aluminumMemberRotationalRestraints import AluminumMemberRotationalRestraint

if Model.clientModel is None:
    Model()

def test_aluminumMemberRotationalRestraints():

    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.aluminum_design_active)

    AluminumMemberRotationalRestraint(1, [False], AluminumMemberRotationalRestraintType.TYPE_CONTINUOUS, "", "",["Grade S275", "Arval (-) 35/207 - 0.63 (b: 1) | DIN 18807 | Arval",
            AluminumMemberRotationalRestraintPositionofSheeting.SHEETING_POSITION_NEGATIVE, AluminumMemberRotationalRestraintContinuousBeamEffect.CONTINUOUS_BEAM_EFFECT_END_PANEL, True],
            parameters = [205000000000.0, 0.00063, 7.5e-08, 0.207, 0.106, 5200.0, 3.0])

    AluminumMemberRotationalRestraint(2, [True, 'test_restraint'], AluminumMemberRotationalRestraintType.TYPE_DISCRETE, "", "",
            ["Grade S275", "IPE A 80 | EN 10365:2017 | ArcelorMittal (2018)", AluminumMemberRotationalRestraintPositionofSheeting.SHEETING_POSITION_POSITIVE, AluminumMemberRotationalRestraintContinuousBeamEffect.CONTINUOUS_BEAM_EFFECT_END_PANEL, True],
            parameters=[205000000000.0, 6.44e-07, 1, 3])

    Model.clientModel.service.finish_modification()

    steelMemberRestraint1 = Model.clientModel.service.get_aluminum_member_rotational_restraint(1)
    steelMemberRestraint2 = Model.clientModel.service.get_aluminum_member_rotational_restraint(2)

    assert steelMemberRestraint1.no == 1
    assert steelMemberRestraint1.material_name == "Grade S275"

    assert steelMemberRestraint2.type == "TYPE_DISCRETE"
    assert steelMemberRestraint2.continuous_beam_effect == "CONTINUOUS_BEAM_EFFECT_END_PANEL"