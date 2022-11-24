#!/usr/bin/env python
# Created by "Thieu" at 14:06, 11/11/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

from mealpy.evolutionary_based import EP, ES, MA, GA, DE, FPA, CRO
from mealpy.swarm_based import ABC, ACOR, AGTO, ALO, AO, ARO, AVOA, BA, BeesA, BES, BFO, BSA, COA, CSA, CSO, DMOA, DO, EHO, FA, FFA, FOA, GOA, GWO
from mealpy.swarm_based import HBA, HGS, HHO, JA, MFO, MPA, MRFO, MSA, NMRA, PFA, PSO, SCSO, SFO, SHO, SLO, SRSR, SSA, SSO, SSpiderA, SSpiderO, WOA
from mealpy.physics_based import SA, WDO, MVO, TWO, EFO, NRO, HGSO, ASO, EO, ArchOA
from mealpy.human_based import BRO, BSO, CA, CHIO, FBIO, GSKA, ICA, LCO, QSA, SARO, SSDO, TLO, SPBO
from mealpy.bio_based import BBO, EOA, IWO, SBO, SMA, VCS, WHO, BMO, SOS, SOA, TSA
from mealpy.system_based import GCO, WCA, AEO
from mealpy.math_based import AOA, CGO, GBO, HC, PSS, SCA, INFO, RUN, CircleSA
from mealpy.music_based import HS

dict_optimizer_classes = {
    "EP": EP.OriginalEP,
    "ES": ES.OriginalES,
    "MA": MA.OriginalMA,
    "DE": DE.BaseDE,
    "GA": GA.BaseGA,
    "FPA": FPA.OriginalFPA,
    "CRO": CRO.OriginalCRO,

    "ABC": ABC.OriginalABC,
    "ACOR": ACOR.OriginalACOR,
    "AGTO": AGTO.OriginalAGTO,
    "ALO": ALO.OriginalALO,
    "AO": AO.OriginalAO,
    "ARO": ARO.OriginalARO,
    "AVOA": AVOA.OriginalAVOA,
    "BA": BA.OriginalBA,
    "BeesA": BeesA.OriginalBeesA,
    "BES": BES.OriginalBES,
    "BFO": BFO.ABFO,
    "BSA": BSA.OriginalBSA,
    "COA": COA.OriginalCOA,
    "CSA": CSA.OriginalCSA,
    "CSO": CSO.OriginalCSO,
    "DMOA": DMOA.DevDMOA,
    "DO": DO.OriginalDO,
    "EHO": EHO.OriginalEHO,
    "FA": FA.OriginalFA,
    "FFA": FFA.OriginalFFA,
    "FOA": FOA.BaseFOA,
    "GOA": GOA.OriginalGOA,
    "GWO": GWO.OriginalGWO,
    "GWO_WOA": GWO.GWO_WOA,
    "HBA": HBA.OriginalHBA,
    "HGS": HGS.OriginalHGS,
    "HHO": HHO.OriginalHHO,
    "JA": JA.BaseJA,
    "LEVY_JA": JA.LevyJA,
    "MFO": MFO.BaseMFO,
    "MPA": MPA.OriginalMPA,
    "MRFO": MRFO.OriginalMRFO,
    "MSA": MSA.OriginalMSA,
    "NMRA": NMRA.OriginalNMRA,
    "PFA": PFA.OriginalPFA,
    "PSO": PSO.OriginalPSO,
    "PPSO": PSO.PPSO,
    "CPSO": PSO.C_PSO,
    "CLPSO": PSO.CL_PSO,
    "SCSO": SCSO.OriginalSCSO,
    "SFO": SFO.OriginalSFO,
    "SHO": SHO.OriginalSHO,
    "SLO": SLO.OriginalSLO,
    "SRSR": SRSR.OriginalSRSR,
    "SSA": SSA.OriginalSSA,
    "SSO": SSO.OriginalSSO,
    "SSpiderA": SSpiderA.OriginalSSpiderA,
    "SSpiderO": SSpiderO.OriginalSSpiderO,
    "WOA": WOA.OriginalWOA,

    "SA": SA.OriginalSA,
    "WDO": WDO.OriginalWDO,
    "MVO": MVO.BaseMVO,
    "TWO": TWO.OriginalTWO,
    "OTWO": TWO.EnhancedTWO,
    "EFO": EFO.BaseEFO,
    "NRO": NRO.OriginalNRO,
    "HGSO": HGSO.OriginalHGSO,
    "ASO": ASO.OriginalASO,
    "EO": EO.OriginalEO,
    "ArchOA": ArchOA.OriginalArchOA,

    "BRO": BRO.BaseBRO,
    "BSO": BSO.OriginalBSO,
    "CA": CA.OriginalCA,
    "CHIO": CHIO.BaseCHIO,
    "FBIO": FBIO.OriginalFBIO,
    "GSKA": GSKA.OriginalGSKA,
    "ICA": ICA.OriginalICA,
    "LCO": LCO.BaseLCO,
    "QSA": QSA.BaseQSA,
    "ImprovedQSA": QSA.ImprovedQSA,
    "SARO": SARO.OriginalSARO,
    "SSDO": SSDO.OriginalSSDO,
    "TLO": TLO.BaseTLO,
    "SPBO": SPBO.DevSPBO,

    "BBO": BBO.BaseBBO,
    "EOA": EOA.OriginalEOA,
    "IWO": IWO.OriginalIWO,
    "SBO": SBO.BaseSBO,
    "SMA": SMA.BaseSMA,
    "VCS": VCS.BaseVCS,
    "WHO": WHO.OriginalWHO,
    "BMO": BMO.OriginalBMO,
    "SOS": SOS.OriginalSOS,
    "SOA": SOA.DevSOA,
    "TSA": TSA.OriginalTSA,

    "GCO": GCO.BaseGCO,
    "WCA": WCA.OriginalWCA,
    "AEO": AEO.OriginalAEO,
    "AAEO": AEO.AdaptiveAEO,

    "AOA": AOA.OriginalAOA,
    "CGO": CGO.OriginalCGO,
    "GBO": GBO.OriginalGBO,
    "HC": HC.SwarmHC,
    "PSS": PSS.OriginalPSS,
    "SCA": SCA.BaseSCA,
    "INFO": INFO.OriginalINFO,
    "RUN": RUN.OriginalRUN,
    "CircleSA": CircleSA.OriginalCircleSA,

    "HS": HS.BaseHS
}
