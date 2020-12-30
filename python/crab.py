from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'More50_RunB_JetHT3'
#config.General.requestName = 'JetHT_RunD'
#29 is run B, 30 is run C
config.General.workArea = 'crabworkarea'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'

config.JobType.psetName = 'JMEanalysis.py'
#config.JobType.outputFiles = ['UL2017RunBSingleMuon_task3.root']
disableAutomaticOutputCollection = False
#config.JobType.maxJobRuntimeMin = 300
#config.JobType.maxMemoryMB = 2000
config.JobType.inputFiles = [
'Summer16_07Aug2017_V11_MC.db','Summer16_07Aug2017All_V11_DATA.db','Summer16_25nsV1b_MC.db','Summer16_25nsV1b_DATA.db',
'Fall17_17Nov2017_V32_102X_MC.db','Fall17_17Nov2017_V32_102X_DATA.db','Fall17_V3b_MC.db','Fall17_V3b_DATA.db',
'Autumn18_V19_MC.db','Autumn18_RunABCD_V19_DATA.db','Autumn18_V7b_MC.db','Autumn18_V7b_DATA.db', 'Summer19UL17_RunF_V5_DATA.db', 'Summer19UL17_JRV2_DATA.db', 'Summer19UL17_JRV2_MC.db', 'Summer19UL17_RunB_V5_DATA.db', 'Summer19UL17_RunC_V5_DATA.db', 'Summer19UL17_RunD_V5_DATA.db', 'Summer19UL17_RunE_V5_DATA.db', 'Summer19UL17_RunF_V5_DATA.db', 'Summer19UL17_V5_MC.db',
'Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt',
'Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt',
'Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt',
'Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt',
'RochesterCorrections',
#'UnprefirableEventList_SingleElectron_Run2017BtoF.root'
'UnprefirableEventList_JetHT_Run2017BtoF.root' 
]
#Make sure all the needed files are included. For example, running on UL, you should add files such as Summer19UL17_JRV2_DATA.db Summer19UL17_RunF_V5_DATA.db
config.Data.inputDataset = '/JetHT/Run2017B-09Aug2019_UL2017-v1/MINIAOD'    
#config.Data.allowNonValidInputDataset = True
#/JetHT/Run2017B-09Aug2019_UL2017-v1/MINIAOD
#'/SingleElectron/Run2017B-09Aug2019_UL2017-v1/MINIAOD'
#'/SingleMuon/Run2017F-09Aug2019_UL2017-v1/MINIAOD' 
#'/JetHT/Run2017F-09Aug2019_UL2017pilot-v1/MINIAOD' 
#'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM'

config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic' #'LumiBased' # 'LumiBased' #'FileBased'
#config.Data.unitsPerJob = 20 #minutes for automatic splitting, 


config.Data.publication = True
config.Data.outputDatasetTag = 'UnprefireableEventsNtuples_JetHT_RunC_morethan50' #'UnprefirableEventsNtuples_JetHT_RunB'
#'RunIISummer16MiniAODv3_PUMoriond17_94X_mcRun2_asymptotic_v3_ext2_v1'


config.Site.storageSite ='T2_AT_Vienna' #T2_BE_IIHE' UF T2
config.Site.blacklist = ['T2_IN_TIFR','T2_US_UCSD','T2_US_Wisconsin','T2_FR_GRIF_LLR','T2_UK_London_Brunel','T2_FR_GRIF_IRFU','T2_US_Caltech','T3_US_Colorado','T1_UK_RAL','T2_US_Vanderbilt']
#config.Site.whitelist =['T1_US_FNAL']

#config.section_("Debug")
#config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#config.User.voGroup = 'becms'
config.section_("Debug")
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']
#so that site blacklist are note allowed to overflow (submit to a blacklisted site)
