


import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
        comEnergy = cms.double(13000.0),
        crossSection = cms.untracked.double(1.095e-3),
        filterEfficiency = cms.untracked.double(1),
        maxEventsToPrint = cms.untracked.int32(0),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        pythiaPylistVerbosity = cms.untracked.int32(1),
        PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'HiggsSM:gg2H = on',
            '25:m0 = 760.00',
            '25:mWidth = 42.560',
            '25:onMode = off',
            '25:OnIfMatch = 23 22',
            '25:doForceWidth = on',
            'Higgs:clipWings = on',
            'Higgs:clipWings = 10',
            '23:onMode = off',
            '23:OnIfMatch = 1 1',
            '23:OnIfMatch = 2 2',
            '23:OnIfMatch = 3 3',
            '23:OnIfMatch = 4 4',
            '23:OnIfMatch = 5 5',
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
)

ProductionFilterSequence = cms.Sequence(generator)
