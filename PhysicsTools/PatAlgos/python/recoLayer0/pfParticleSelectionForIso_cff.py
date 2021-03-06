import FWCore.ParameterSet.Config as cms

from CommonTools.ParticleFlow.PFBRECO_cff import particleFlowPtrs
from CommonTools.ParticleFlow.PFBRECO_cff import pfPileUpIsoPFBRECO, pfNoPileUpIsoPFBRECO, pfNoPileUpIsoPFBRECOSequence
from CommonTools.ParticleFlow.PFBRECO_cff import pfPileUpPFBRECO, pfNoPileUpPFBRECO, pfNoPileUpPFBRECOSequence
from CommonTools.ParticleFlow.PFBRECO_cff import pfAllNeutralHadronsPFBRECO, pfAllChargedHadronsPFBRECO, pfAllPhotonsPFBRECO, pfAllChargedParticlesPFBRECO, pfPileUpAllChargedParticlesPFBRECO, pfAllNeutralHadronsAndPhotonsPFBRECO, pfSortByTypePFBRECOSequence
from CommonTools.ParticleFlow.PFBRECO_cff import pfParticleSelectionPFBRECOSequence

pfParticleSelectionForIsoSequence = cms.Sequence(
    particleFlowPtrs +
    pfParticleSelectionPFBRECOSequence
    )