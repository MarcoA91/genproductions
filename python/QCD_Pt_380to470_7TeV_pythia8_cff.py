import FWCore.ParameterSet.Config as cms

configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('$Revision$'),
	name = cms.untracked.string('$Source$'),
	annotation = cms.untracked.string('Spring10: Pythia8 generation of QCD events, 7TeV, pthat = 380 .. 470 GeV')
)

generator = cms.EDFilter("Pythia8GeneratorFilter",
	crossSection = cms.untracked.double(2.434e+02),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaPylistVerbosity = cms.untracked.int32(1),
	filterEfficiency = cms.untracked.double(1.0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	comEnergy = cms.double(7000.0),
	PythiaParameters = cms.PSet(
		processParameters = cms.vstring(
			'Main:timesAllowErrors    = 10000',
			'ParticleDecays:limitTau0 = on',
			'ParticleDecays:tauMax = 10',
			'HardQCD:all = on',
			'PhaseSpace:pTHatMin = 380',
			'PhaseSpace:pTHatMax = 470',
			'Tune:pp 2',
			'Tune:ee 3'),
		parameterSets = cms.vstring('processParameters')
	)
)