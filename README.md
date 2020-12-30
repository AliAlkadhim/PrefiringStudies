directions:
cmsrel ... cmsenv
git cms-addpkg RecoMET/METFilters
git clone PhysicsTools/PatUtils
git clone https://github.com/lathomas/JetMETStudies.git 
scram b -j4

git cms-merge-topic jainshilpi:ULV1_backport10616_forUsers
git clone https://github.com/cms-egamma/EgammaPostRecoTools.git
mv EgammaPostRecoTools/python/EgammaPostRecoTools.py RecoEgamma/EgammaTools/python/.
git clone https://github.com/jainshilpi/EgammaAnalysis-ElectronTools.git -b UL2018 EgammaAnalysis/ElectronTools/data/
git cms-addpkg EgammaAnalysis/ElectronTools
