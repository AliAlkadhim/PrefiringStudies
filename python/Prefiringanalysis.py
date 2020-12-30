import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )  
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(23374) )  

from PhysicsTools.PatAlgos.tools.helpers import getPatAlgosToolsTask
patAlgosToolsTask = getPatAlgosToolsTask(process)


process.source = cms.Source("PoolSource",
                                fileNames = cms.untracked.vstring(
'/store/mc/RunIISummer19UL17MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/002C691B-A0CE-A24F-8805-03B4C52C9004.root'
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/FB3AF382-9B0B-0149-992B-FE2821BDD760.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/072C9A2E-CB16-454A-B606-23CC06A9D99E.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/8275D908-9210-E740-82D6-B8A900C3F159.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/D98076B6-6554-3D49-900C-FF8B2745FE28.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/286E776F-8336-5146-BDF0-7A105C62F6AF.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/874FCEB9-F89C-F343-80DB-517399B933C5.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/EC1FE245-3CB6-D54F-A3E0-9FEE00F13D24.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/6289DC1C-8893-E94B-AB5B-71D7D118D404.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/991FC419-3364-5440-ABCF-C4B7E43A4DA2.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/2A9B513D-4CF7-7148-8BC0-5B93BE3DF4DD.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/EBED85A4-4FD4-8A48-9101-FCB0FF838998.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/E08E2CE9-6C1A-1742-8CC5-0FF7C53E21DD.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/5CE83870-328E-544F-934B-EF6AC9B30A8D.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/BFBB6E02-96D3-544A-AC8F-C3A757507D34.root',
#'/store/data/Run2017B/SingleMuon/MINIAOD/09Aug2019_UL2017-v1/130000/38934817-8B86-114B-B531-4E0C57D1205F.root'
#'/store/data/Run2017F/JetHT/MINIAOD/09Aug2019_UL2017-v1/130000/3CD3E778-D5BF-394E-9D46-98D77A3CB58D.root' 
#Here's a MINIAOD file on lxplus in case you want to use a local sample
#'file:/afs/cern.ch/work/l/lathomas/public/qcdht1000to1500_1.root'
        )
                            )

#process.TFileService = cms.Service("TFileService", fileName = cms.string("outputQCDHT1000to1500_puppiv16_200kevts.root") )
#process.TFileService = cms.Service("TFileService", fileName = cms.string("outputQCDHT1000to1500_puppiv16_23374evts.root") )
#process.TFileService = cms.Service("TFileService", fileName = cms.string("UL2017RunBSingleMuon_task2.root") )

process.TFileService = cms.Service("TFileService", fileName = cms.string('DYJetsUL17MC_test.root') ) 

#process.output = cms.OutputModule("PoolOutputModule",
#    fileName = cms.untracked.string('UL2017RunBSingleMuon_task3.root')
#,dataset = cms.untracked.PSet(dataTier = cms.untracked.string('MINIAOD')#
#)
process.options = cms.untracked.PSet(
 wantSummary = cms.untracked.bool( True ),
 SkipEvent = cms.untracked.vstring('ProductNotFound')
)

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag="102X_dataRun2_v8"

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")


process.load('Configuration.StandardSequences.Reconstruction_cff')


ISMC=True

runEra="DataUL2017B"
#runEra="MCUL2017"
UseSQLiteFiles=True


if "MC" in runEra:
    ISMC=True


EleVetoWP=''
EleTightWP=''
PhotonTightWP=''
#Rochester corrections folder: 
RochesterCorrectionFile="RochesterCorrections/"


if "Data2018" in runEra:
    if "2018D" in runEra: 
        process.GlobalTag.globaltag="102X_dataRun2_Prompt_v16" #2018D
    else:
        process.GlobalTag.globaltag="102X_dataRun2_v13" #2018ABC
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V2-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'
    RochesterCorrectionFile+="RoccoR2018.txt"

if "Data2017" in runEra:
    process.GlobalTag.globaltag="102X_dataRun2_v13" #2017      
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V1-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'
    RochesterCorrectionFile+="RoccoR2017.txt"

if "DataUL2017" in runEra:
    process.GlobalTag.globaltag="102X_dataRun2_v13" #2017      
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V1-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'
    RochesterCorrectionFile+="RoccoR2017UL.txt"

if "Data2016" in runEra:
    process.GlobalTag.globaltag="102X_dataRun2_v13" #2016
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V1-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'
    RochesterCorrectionFile+="RoccoR2016.txt"

if "MC2018" in runEra:
    process.GlobalTag.globaltag="102X_upgrade2018_realistic_v21" #2018     
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V2-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'
    RochesterCorrectionFile+="RoccoR2018.txt"

if "MC2017" in runEra:
    process.GlobalTag.globaltag="102X_mc2017_realistic_v8" #2017
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V1-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'
    RochesterCorrectionFile+="RoccoR2017.txt"

if "MC2016" in runEra:
    process.GlobalTag.globaltag="102X_mcRun2_asymptotic_v8" #2016
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V1-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'
    RochesterCorrectionFile+="RoccoR2016.txt"

if "MCUL2017" in runEra:
    process.GlobalTag.globaltag="102X_mc2017_realistic_v8" #2017
    EleVetoWP='cutBasedElectronID-Fall17-94X-V1-veto'
    EleTightWP='mvaEleID-Fall17-iso-V1-wp90'
    PhotonTightWP='mvaPhoID-RunIIFall17-v1p1-wp80'
    RochesterCorrectionFile+="RoccoR2017UL.txt"

print "Roch corr file: " 
print RochesterCorrectionFile

process.prefiringanalyzer = cms.EDAnalyzer('prefiringanalyzer',
                                     METFiltersPAT = cms.InputTag("TriggerResults::PAT"),
                                     METFiltersRECO = cms.InputTag("TriggerResults::RECO"),
                                     ECALBadCalibFilterUpdate=cms.InputTag("ecalBadCalibReducedMINIAOD2019Filter"),
                                     ECALLaserCorrFilterUpdate=cms.InputTag("ecalLaserCorrFilter"),
                                     ECALDeadCellBoundaryEnergyFilterUpdate=cms.InputTag("ecalDeadCellBoundaryEnergyFilterUpdate"),
                                     BadChargedCandidateFilterUpdate=cms.InputTag("BadChargedCandidateFilterUpdate"),
                                     Vertices=cms.InputTag("offlineSlimmedPrimaryVertices"),
                                     Jets=cms.InputTag("updatedPatJetsUpdatedJEC"),
#                                     JetsPuppi=cms.InputTag("updatedPatJetsUpdatedJECPuppi"),
                                     JetsPuppi=cms.InputTag("slimmedJetsPuppi"),
                                     JetsPuppiAK8=cms.InputTag("slimmedJetsAK8"),
                                     pileupJetIdDiscriminantUpdate = cms.InputTag('pileupJetIdUpdate:fullDiscriminant'),
                                     pileupJetIdDiscriminantUpdate2017 = cms.InputTag('pileupJetIdUpdate2017:fullDiscriminant'),
                                     pileupJetIdDiscriminantUpdate2018 = cms.InputTag('pileupJetIdUpdate2018:fullDiscriminant'),
                                     pileupJetIdVariablesUpdate = cms.InputTag('pileupJetIdUpdate'),
                                     QuarkGluonLikelihood = cms.InputTag('QGTagger:qgLikelihood'),
                                     PFCandidates=cms.InputTag("packedPFCandidates"),
                                     PuppiWeights=cms.InputTag("puppi"),
                                     PULabel = cms.InputTag("slimmedAddPileupInfo"),
                                     Triggers = cms.InputTag("TriggerResults::HLT"),
                                     l1GtSrc = cms.InputTag("gtStage2Digis"),
                                     GenParticles=cms.InputTag("prunedGenParticles"),
                                     GenInfo=cms.InputTag("generator"),
                                     LHELabel = cms.InputTag("externalLHEProducer"),
                                     LHELabelALT = cms.InputTag("source"),
                                     GenJetMatchCHS= cms.InputTag("patJetGenJetMatchUpdate"),
                                     GenJetWithNuMatchCHS= cms.InputTag("patJetGenWithNuJetMatchUpdate"),
                                     GenJetMatchPuppi= cms.InputTag("patJetGenJetMatchUpdatePuppi"),
                                     GenJetWithNuMatchPuppi= cms.InputTag("patJetGenWithNuJetMatchUpdatePuppi"),
                                     PFMet=cms.InputTag("slimmedMETs"),
                                     PuppiMet=cms.InputTag("slimmedMETsPuppi"),
                                     Electrons=cms.InputTag("slimmedElectrons"),
                                     Muons=cms.InputTag("slimmedMuons"),
                                     Photons=cms.InputTag("slimmedPhotons"),
                                     JetPtCut=cms.double(20),
                                     AK8JetPtCut=cms.double(200),
                                     ElectronPtCut=cms.double(20),
                                     ElectronVetoWorkingPoint=cms.string(EleVetoWP),
                                     ElectronTightWorkingPoint=cms.string(EleTightWP),
                                     MuonPtCut=cms.double(20),
                                     RochCorrFile=cms.string(RochesterCorrectionFile),
                                     PhotonPtCut=cms.double(20),
                                     PhotonTightWorkingPoint=cms.string(PhotonTightWP),
                                     PFCandPtCut=cms.double(1000),
                                     SaveTree=cms.bool(False),
                                     IsMC=cms.bool(ISMC),
                                     SavePUIDVariables=cms.bool(False),
                                     SaveAK8Jets=cms.bool(False),
                                     DropUnmatchedJets=cms.bool(False),
                                     DropBadJets=cms.bool(False),
                                     ApplyPhotonID=cms.bool(False),
#                                     Skim=cms.string("ZToEEorMuMu"),
                                     Skim=cms.string("Dilepton"),
#                                     Skim=cms.string("HighHT"),
                                     Debug=cms.bool(False)
                              )





#Rerunning the ecalbadcalibration filter
from RecoMET.METFilters.ecalBadCalibFilter_cfi import ecalBadCalibFilter

baddetEcallistnew2019 = cms.vuint32(
    [872439604,872422825,872420274,872423218,872423215,872416066,872435036,872439336,
     872420273,872436907,872420147,872439731,872436657,872420397,872439732,872439339,
     872439603,872422436,872439861,872437051,872437052,872420649,872421950,872437185,
     872422564,872421566,872421695,872421955,872421567,872437184,872421951,872421694,
     872437056,872437057,872437313,872438182,872438951,872439990,872439864,872439609,
     872437181,872437182,872437053,872436794,872436667,872436536,872421541,872421413,
     872421414,872421031,872423083,872421439,872423224,872421438,872420397,872421566,
     872422589,872423096,872422717,872423214,872421415,872422311,872421926,872439469,
     872438567,872436659,872439731,872438311,872438078,872438438,872439601,872437951,
     872437950,872439729,872436792,872438183,872439468,872436663,872439728,872439727,
     872437694,872437823,872438845,872438973,872439354,872438566,872439733,872436530,
     872436655,872439600,872439730]
    )

process.ecalBadCalibReducedMINIAOD2019Filter = ecalBadCalibFilter.clone(
    EcalRecHitSource = cms.InputTag("reducedEgamma:reducedEERecHits"),
    ecalMinEt        = cms.double(50.),
    baddetEcal    = baddetEcallistnew2019,
    taggingMode = cms.bool(True),
    debug = cms.bool(False)
    )

#Rerunning the laser correction filter
process.load('RecoMET.METFilters.ecalLaserCorrFilter_cfi')
process.ecalLaserCorrFilter = cms.EDFilter(
    "EcalLaserCorrFilter",
    EBRecHitSource = cms.InputTag("reducedEgamma:reducedEBRecHits"),
    EERecHitSource = cms.InputTag("reducedEgamma:reducedEERecHits"),
    EBLaserMIN     = cms.double(0.3),
    EELaserMIN     = cms.double(0.3),
    EBLaserMAX     = cms.double(5.0), #this was updated wrt default
    EELaserMAX     = cms.double(100.0), #this was updated wrt default
    EBEnegyMIN     = cms.double(10.0),
    EEEnegyMIN     = cms.double(10.0),
    taggingMode    = cms.bool(True), #updated wrt default
    Debug          = cms.bool(False)
    )

#Rerunning EcalDeadCellBoundaryEnergyFilter
from RecoMET.METFilters.EcalDeadCellBoundaryEnergyFilter_cfi import EcalDeadCellBoundaryEnergyFilter
process.ecalDeadCellBoundaryEnergyFilterUpdate=EcalDeadCellBoundaryEnergyFilter.clone(
    recHitsEB = cms.InputTag("reducedEgamma:reducedEBRecHits"),
    recHitsEE = cms.InputTag("reducedEgamma:reducedEERecHits"),
    cutBoundEnergyDeadCellsEE=cms.untracked.double(10),
    taggingMode    = cms.bool(True)
    )

#Rerunning BadChargedCandidateFilter
from RecoMET.METFilters.BadChargedCandidateFilter_cfi import BadChargedCandidateFilter 
process.BadChargedCandidateFilterUpdate=BadChargedCandidateFilter.clone(
    muons = cms.InputTag("slimmedMuons"),
    PFCandidates = cms.InputTag("packedPFCandidates"),
    taggingMode    = cms.bool(True)
)



import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())


JSONfile =''

if "DataUL2017" in runEra:
    JSONfile = 'Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt'
if "Data2018" in runEra:
    JSONfile = 'Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt'
if "Data2017" in runEra:
    JSONfile = 'Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt'
if "Data2016" in runEra:
    JSONfile = 'Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt'
myLumis = LumiList.LumiList(filename = JSONfile).getCMSSWString().split(',')
if not ISMC:
    process.source.lumisToProcess.extend(myLumis)
print "json" 
print JSONfile 

#Updating JECs
JECsVersion=""
if "MC2018" in runEra:
    JECsVersion='Autumn18_V19_MC'
if "MC2017" in runEra:
    JECsVersion='Fall17_17Nov2017_V32_102X_MC'
if "MC2016" in runEra:
    JECsVersion='Summer16_07Aug2017_V11_MC'
if "MCUL2017" in runEra:
    JECsVersion='Summer19UL17_V5_MC'

if "Data2018" in runEra:
    JECsVersion='Autumn18_RunABCD_V19_DATA'
if "Data2017" in runEra:
    JECsVersion='Fall17_17Nov2017_V32_102X_DATA'
if "Data2016" in runEra:
    JECsVersion='Summer16_07Aug2017All_V11_DATA'

if "DataUL2017B" in runEra:
    JECsVersion='Summer19UL17_RunB_V5_DATA'
if "DataUL2017C" in runEra:
    JECsVersion='Summer19UL17_RunC_V5_DATA'
if "DataUL2017D" in runEra:
    JECsVersion='Summer19UL17_RunD_V5_DATA'
if "DataUL2017E" in runEra:
    JECsVersion='Summer19UL17_RunE_V5_DATA'
if "DataUL2017F" in runEra:
    JECsVersion='Summer19UL17_RunF_V5_DATA'



SQLiteFile='sqlite:'+JECsVersion+'.db'

TagForAK4CHSJet='JetCorrectorParametersCollection_'+JECsVersion+'_AK4PFchs'
TagForAK4PuppiJet='JetCorrectorParametersCollection_'+JECsVersion+'_AK4PFPuppi'

from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup


process.jec = cms.ESSource('PoolDBESSource',
                           CondDBSetup,
                           connect = cms.string(SQLiteFile),
                           toGet = cms.VPSet(
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string(TagForAK4CHSJet),
            label  = cms.untracked.string('AK4PFchs')
            ),
        cms.PSet(
            record = cms.string('JetCorrectionsRecord'),
            tag    = cms.string(TagForAK4PuppiJet),
            label  = cms.untracked.string('AK4PFPuppi')
            ) 
        )
                           )

# Add an ESPrefer to override JEC that might be available from the global tag
if UseSQLiteFiles:
    process.es_prefer_jec = cms.ESPrefer('PoolDBESSource', 'jec')
else:
    process.es_prefer_jec = cms.ESPrefer('PoolDBESSource', 'GlobalTag')


JERVersion=''

if "MC2018" in runEra:
    JERVersion='Autumn18_V7b_MC'
if "MC2017" in runEra:
    JERVersion='Fall17_V3b_MC'
if "MC2016" in runEra:
    JERVersion='Summer16_25nsV1b_MC'

if "Data2018" in runEra:
    JERVersion='Autumn18_V7b_DATA'
if "Data2017" in runEra:
    JERVersion='Fall17_V3b_DATA'
if "Data2016" in runEra:
    JERVersion='Summer16_25nsV1b_DATA'

if "MCUL2017" in runEra:
    JERVersion='Summer19UL17_JRV2_MC'
if "DataUL2017" in runEra:
    JERVersion='Summer19UL17_JRV2_DATA'


SQLiteFileJER='sqlite:'+JERVersion+'.db'


print SQLiteFileJER
process.jer = cms.ESSource("PoolDBESSource",
                           CondDBSetup,
                           toGet = cms.VPSet(
        cms.PSet(
            record = cms.string('JetResolutionRcd'),
            tag    = cms.string('JR_'+JERVersion+'_PtResolution_AK4PFchs'),
            label  = cms.untracked.string('AK4PFchs_pt')
            ),
        cms.PSet(
            record = cms.string('JetResolutionScaleFactorRcd'),
            tag    = cms.string('JR_'+JERVersion+'_SF_AK4PFchs'),
            label  = cms.untracked.string('AK4PFchs')
            ),
#        cms.PSet(                                                                                                                                                                                            
#            record = cms.string('JetResolutionRcd'),                                                                                                                                                         
#            tag    = cms.string('JR_'+JERVersion+'_PtResolution_AK4PFPuppi'),
#            label  = cms.untracked.string('AK4PFPuppi_pt')                                                                                                                                                   
#            ),                                                                                                                                                                                               
#        cms.PSet(                                                                                                                                                                                            
#            record = cms.string('JetResolutionScaleFactorRcd'),                                                                                                                                              
#            tag    = cms.string('JR_'+JERVersion+'_SF_AK4PFPuppi'),                                                                                                                                    
#            label  = cms.untracked.string('AK4PFPuppi')                                                                                                                                                      
#            ),                                                                                                                                                                                               
        ),
                           connect = cms.string(SQLiteFileJER)
                           )

if UseSQLiteFiles: 
    process.es_prefer_jer = cms.ESPrefer('PoolDBESSource', 'jer')
else:
    process.es_prefer_jer = cms.ESPrefer('PoolDBESSource', 'GlobalTag')


from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection

updateJetCollection(
    process,
    jetSource = cms.InputTag('slimmedJets'),
    labelName = 'UpdatedJEC',
    jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None')  
)

updateJetCollection(
    process,
    jetSource = cms.InputTag('slimmedJetsPuppi'),
    labelName = 'UpdatedJEC',
    postfix = 'Puppi',
    jetCorrections = ('AK4PFPuppi', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None') 
)
process.jecSequence = cms.Sequence(process.patJetCorrFactorsUpdatedJEC * process.updatedPatJetsUpdatedJEC * process.patJetCorrFactorsUpdatedJECPuppi * process.updatedPatJetsUpdatedJECPuppi)


#Recluster gen jets
## Filter out neutrinos from packed GenParticles 
#The filter on pdgid 2101, 2103, 2203 and 1103 should be harmless for standard samples. I added it because some private samples mistakenly added those unstable states as stable products. 
process.packedGenParticlesForJetsNoNuNEW = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedGenParticles"), cut = cms.string("abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16 && abs(pdgId) != 2101 &&abs(pdgId) != 2103 && abs(pdgId) != 2203  && abs(pdgId) != 1103 "))
process.packedGenParticlesForJetsWithNuNEW = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedGenParticles"), cut = cms.string("abs(pdgId) != 2101 &&abs(pdgId) != 2103 && abs(pdgId) != 2203  && abs(pdgId) != 1103 "))
## Define GenJets 
from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
process.ak4GenJetsNoNuNEW = ak4GenJets.clone(src = 'packedGenParticlesForJetsNoNuNEW')
process.ak4GenJetsWithNuNEW = ak4GenJets.clone(src = 'packedGenParticlesForJetsWithNuNEW')
#I didn't manage to create a new jet collection on top of MINIAOD with the matching to this updated gen jet collection   
#Work around: do the matching by hand                                                                                                                                                                                       
#Now redo the matching. The patJetGenJetMatch produces a matching between the gen jets and the reco jets. 
from PhysicsTools.PatAlgos.mcMatchLayer0.jetMatch_cfi import patJetGenJetMatch

process.patJetGenJetMatchUpdate = patJetGenJetMatch.clone(
src         = cms.InputTag("updatedPatJetsUpdatedJEC"),
matched     = cms.InputTag("ak4GenJetsNoNuNEW")
)
process.patJetGenJetMatchUpdatePuppi = patJetGenJetMatch.clone(
src         = cms.InputTag("slimmedJetsPuppi"),
matched     = cms.InputTag("ak4GenJetsNoNuNEW")
)
process.patJetGenWithNuJetMatchUpdate = patJetGenJetMatch.clone(
src         = cms.InputTag("updatedPatJetsUpdatedJEC"),
matched     = cms.InputTag("ak4GenJetsWithNuNEW")
)
process.patJetGenWithNuJetMatchUpdatePuppi = patJetGenJetMatch.clone(
src         = cms.InputTag("slimmedJetsPuppi"),
matched     = cms.InputTag("ak4GenJetsWithNuNEW")
)






#Update MET
from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD

#Recompute PFMET (with updated JECs)
runMetCorAndUncFromMiniAOD (
    process,
    isData = not ISMC
)



'''
#Rerunning PUPPI (standard approach, default tuning)
from PhysicsTools.PatAlgos.slimming.puppiForMET_cff import makePuppiesFromMiniAOD
makePuppiesFromMiniAOD( process, True );
#Set to false if you want to recompute PUPPI weights
process.puppiNoLep.useExistingWeights = True
process.puppi.useExistingWeights = True

#Recompute PUPPI MET (with updated JECs and possibly updated PUPPI weights)
runMetCorAndUncFromMiniAOD(process,
                           jetCollUnskimmed="updatedPatJetsUpdatedJECPuppi",
                           isData= not ISMC,
                           metType="Puppi",
                           postfix="Puppi",
                           jetFlavor="AK4PFPuppi",
                           reapplyJEC = False
                           )
'''

#Rerunning PUPPi with v14-Chihuahua tune
from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
process.ak4PuppiJets  = ak4PFJets.clone (src = 'puppi', doAreaFastjet = True, jetPtMin = 2.)

from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
addJetCollection(process,labelName = 'Puppi', jetSource = cms.InputTag('ak4PuppiJets'), algo = 'AK', rParam=0.4, genJetCollection=cms.InputTag('slimmedGenJets'), jetCorrections = ('AK4PFPuppi', ['L1FastJet', 'L2Relative', 'L3Absolute','L2L3Residual'], 'None'),pfCandidates = cms.InputTag('packedPFCandidates'),
                 pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
                 svSource = cms.InputTag('slimmedSecondaryVertices'),
                 muSource =cms.InputTag( 'slimmedMuons'),
                 elSource = cms.InputTag('slimmedElectrons'),
                 genParticles= cms.InputTag('prunedGenParticles'),
                 getJetMCFlavour=ISMC
)

process.patJetsPuppi.addGenPartonMatch = cms.bool(ISMC)
process.patJetsPuppi.addGenJetMatch = cms.bool(ISMC)

from CommonTools.PileupAlgos.customizePuppiTune_cff import UpdatePuppiTuneV15

patAlgosToolsTask.add(process.ak4PuppiJets)
UpdatePuppiTuneV15(process,ISMC)



#Recompute pile up ID
from RecoJets.JetProducers.PileupJetID_cfi import  _chsalgos_81x, _chsalgos_94x, _chsalgos_102x
process.load("RecoJets.JetProducers.PileupJetID_cfi")
process.pileupJetIdUpdate = process.pileupJetId.clone()
process.pileupJetIdUpdate.jets = cms.InputTag("updatedPatJetsUpdatedJEC")
process.pileupJetIdUpdate.inputIsCorrected = True
process.pileupJetIdUpdate.applyJec = False
process.pileupJetIdUpdate.vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
process.pileupJetIdUpdate.algos = cms.VPSet(_chsalgos_81x) 


process.pileupJetIdUpdate2017 = process.pileupJetId.clone()
process.pileupJetIdUpdate2017.jets = cms.InputTag("updatedPatJetsUpdatedJEC")
process.pileupJetIdUpdate2017.inputIsCorrected = True
process.pileupJetIdUpdate2017.applyJec = False
process.pileupJetIdUpdate2017.vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
process.pileupJetIdUpdate2017.algos = cms.VPSet(_chsalgos_94x)

process.pileupJetIdUpdate2018 = process.pileupJetId.clone()
process.pileupJetIdUpdate2018.jets = cms.InputTag("updatedPatJetsUpdatedJEC")
process.pileupJetIdUpdate2018.inputIsCorrected = True
process.pileupJetIdUpdate2018.applyJec = False
process.pileupJetIdUpdate2018.vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
process.pileupJetIdUpdate2018.algos = cms.VPSet(_chsalgos_102x)


#Compute QGL 
process.load('RecoJets.JetProducers.QGTagger_cfi')
process.QGTagger.srcJets          = cms.InputTag('updatedPatJetsUpdatedJEC')
process.QGTagger.jetsLabel        = cms.string('QGL_AK4PFchs')   


#

eraforEGMSmearing=''

if "UL2017" in runEra or "UL2018" in runEra:
    if "UL2017" in runEra:
        eraforEGMSmearing='2017-UL'
    if "UL2018" in runEra:
        eraforEGMSmearing='2018-UL'
    from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
    setupEgammaPostRecoSeq(process,
                           runVID=False, #saves CPU time by not needlessly re-running VID, if you want the Fall17V2 IDs, set this to True or remove (default is True)
                           era=eraforEGMSmearing)    
    process.ApplyEGMScaleSmearing=cms.Path(process.egammaPostRecoSeq)



process.applyjecs =  cms.Path( process.jecSequence )
if ISMC: 
    process.reclustergenjets = cms.Path(process.packedGenParticlesForJetsNoNuNEW * process.packedGenParticlesForJetsWithNuNEW *process.ak4GenJetsNoNuNEW * process.ak4GenJetsWithNuNEW * process.patJetGenJetMatchUpdate *process.patJetGenJetMatchUpdatePuppi  * process.patJetGenWithNuJetMatchUpdate  * process.patJetGenWithNuJetMatchUpdatePuppi)


#You may want to comment out some of the following lines to speed things up
#process.ApplyPatAlgos  = cms.Path(process.patAlgosToolsTask)

#process.rerunmetfilters = cms.Path( process.ecalBadCalibReducedMINIAOD2019Filter * process.ecalLaserCorrFilter * process.ecalDeadCellBoundaryEnergyFilterUpdate * process.BadChargedCandidateFilterUpdate ) 
#process.computepuid = cms.Path(process.pileupJetIdUpdate  * process.pileupJetIdUpdate2017 * process.pileupJetIdUpdate2018)
#process.computeqgl = cms.Path(process.QGTagger)

#This one obviously shouldn't be commented out
process.endpath = cms.EndPath( process.prefiringanalyzer)



