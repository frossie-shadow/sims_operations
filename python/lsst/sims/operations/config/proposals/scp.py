import lsst.pex.config as pexConfig

from ..base import field as baseField
from ..base import filters as baseFilters
from ..base import proposalconf as baseProposal
from ..base import sequencesconf as baseSequences
from ..base import target as baseTarget
from .. import factories
from .. import utils

@pexConfig.registerConfig("SouthCelestialPole", factories.standardPropReg,
                          baseProposal.StandardProposalConfig)
class SouthCelestialPole(baseProposal.StandardProposalConfig):
    """
    This class gathers the information for the South Celestial Pole proposal.
    """

    def setDefaults(self):
        """
        Setup all the proposal information.
        """
        
        self.name = "SouthCelestialPole-18-0824"
        self.WLType = False
        self.ScienceType = ["WFD"]

        #-----------------
        # Event Sequencing
        #-----------------

        es = baseSequences.StandardEventSequencingConfig()
        es.NVisits = 3

        # Filter Information

        uFilter = baseFilters.FilterConfig()
        uFilter.name = 'u'
        uFilter.numVisits = 30
        uFilter.minBright = 21.00
        uFilter.maxBright = 30.0
        uFilter.maxSeeing = 3.0

        gFilter = baseFilters.FilterConfig()
        gFilter.name = 'g'
        gFilter.numVisits = 30
        gFilter.minBright = 21.0
        gFilter.maxBright = 30.0
        gFilter.maxSeeing = 3.0

        rFilter = baseFilters.FilterConfig()
        rFilter.name = 'r'
        rFilter.numVisits = 30
        rFilter.minBright = 20.00
        rFilter.maxBright = 30.0
        rFilter.maxSeeing = 2.0

        iFilter = baseFilters.FilterConfig()
        iFilter.name = 'i'
        iFilter.numVisits = 30
        iFilter.minBright = 19.5
        iFilter.maxBright = 30.0
        iFilter.maxSeeing = 2.0

        zFilter = baseFilters.FilterConfig()
        zFilter.name = 'z'
        zFilter.numVisits = 30
        zFilter.minBright = 17.5
        zFilter.maxBright = 21.4
        zFilter.maxSeeing = 2.0

        yFilter = baseFilters.FilterConfig()
        yFilter.name = 'y'
        yFilter.numVisits = 30
        yFilter.minBright = 16.5
        yFilter.maxBright = 21.4
        yFilter.maxSeeing = 3.0

        es.filters = baseFilters.FiltersConfig(filters={'u': uFilter,
                                                        'g': gFilter,
                                                        'r': rFilter,
                                                        'i': iFilter,
                                                        'z': zFilter,
                                                        'y': yFilter})

        self.eventSequence = es

        #----------------
        # Field Selection
        #----------------

        fs = baseField.FieldSelectionConfig()
        fs.userRegions = self.__make_user_regions__()
        fs.taperL = 0.0
        fs.taperB = 0.0
        fs.peakL = 0.0

        self.fieldSelect = fs

        #-----------------
        # Target Selection
        #-----------------

        ts = baseTarget.TargetSelectionConfig()
        ts.MaxAirmass = 2.5
        ts.MaxSeeing = 2.0

        self.targetSelect = ts

        #---------------
        # Target Ranking
        #---------------

        tr = baseTarget.TargetRankingConfig()
        tr.RelativeProposalPriority = 1.0

        self.targetRanking = tr

    def __make_user_regions__(self):
        __regions__ = ((0.0, -90.0, 0.03),
                       (180.0, -87.57, 0.03),
                       (324.0, -87.57, 0.03),
                       (36.0, -87.57, 0.03),
                       (252.0, -87.57, 0.03),
                       (108.0, -87.57, 0.03),
                       (216.0, -85.27, 0.03),
                       (144.0, -85.27, 0.03),
                       (0.0, -85.27, 0.03),
                       (288.0, -85.27, 0.03),
                       (72.0, -85.27, 0.03),
                       (324.0, -84.74, 0.03),
                       (36.0, -84.74, 0.03),
                       (180.0, -84.74, 0.03),
                       (252.0, -84.74, 0.03),
                       (108.0, -84.74, 0.03),
                       (203.15, -82.8, 0.03),
                       (156.85, -82.8, 0.03),
                       (275.14, -82.8, 0.03),
                       (84.86, -82.8, 0.03),
                       (347.14, -82.8, 0.03),
                       (12.86, -82.8, 0.03),
                       (228.85, -82.8, 0.03),
                       (131.15, -82.8, 0.03),
                       (300.86, -82.8, 0.03),
                       (59.14, -82.8, 0.03),
                       (180.0, -81.97, 0.03),
                       (324.0, -81.97, 0.03),
                       (36.0, -81.97, 0.03),
                       (252.0, -81.97, 0.03),
                       (108.0, -81.97, 0.03),
                       (216.0, -80.52, 0.03),
                       (144.0, -80.52, 0.03),
                       (0.0, -80.52, 0.03),
                       (288.0, -80.52, 0.03),
                       (72.0, -80.52, 0.03),
                       (268.86, -80.2, 0.03),
                       (91.14, -80.2, 0.03),
                       (196.86, -80.2, 0.03),
                       (163.14, -80.2, 0.03),
                       (340.86, -80.2, 0.03),
                       (19.14, -80.2, 0.03),
                       (235.14, -80.2, 0.03),
                       (124.86, -80.2, 0.03),
                       (307.14, -80.2, 0.03),
                       (52.86, -80.2, 0.03),
                       (180.0, -79.22, 0.03),
                       (252.0, -79.22, 0.03),
                       (108.0, -79.22, 0.03),
                       (324.0, -79.22, 0.03),
                       (36.0, -79.22, 0.03),
                       (295.81, -78.07, 0.03),
                       (64.19, -78.07, 0.03),
                       (280.19, -78.07, 0.03),
                       (79.81, -78.07, 0.03),
                       (223.81, -78.07, 0.03),
                       (136.19, -78.07, 0.03),
                       (352.18, -78.07, 0.03),
                       (7.81, -78.07, 0.03),
                       (208.19, -78.07, 0.03),
                       (151.81, -78.07, 0.03),
                       (265.21, -77.54, 0.03),
                       (94.79, -77.54, 0.03),
                       (310.79, -77.54, 0.03),
                       (49.21, -77.54, 0.03),
                       (238.79, -77.54, 0.03),
                       (121.21, -77.54, 0.03),
                       (193.21, -77.54, 0.03),
                       (166.79, -77.54, 0.03),
                       (337.21, -77.54, 0.03),
                       (22.79, -77.54, 0.03),
                       (180.0, -76.46, 0.03),
                       (324.0, -76.46, 0.03),
                       (36.0, -76.46, 0.03),
                       (252.0, -76.46, 0.03),
                       (108.0, -76.46, 0.03),
                       (216.0, -75.74, 0.03),
                       (144.0, -75.74, 0.03),
                       (0.0, -75.74, 0.03),
                       (288.0, -75.74, 0.03),
                       (72.0, -75.74, 0.03),
                       (203.04, -75.52, 0.03),
                       (156.96, -75.52, 0.03),
                       (347.04, -75.52, 0.03),
                       (12.96, -75.52, 0.03),
                       (228.96, -75.52, 0.03),
                       (131.04, -75.52, 0.03),
                       (275.04, -75.52, 0.03),
                       (84.96, -75.52, 0.03),
                       (300.96, -75.52, 0.03),
                       (59.04, -75.52, 0.03),
                       (190.84, -74.83, 0.03),
                       (169.16, -74.83, 0.03),
                       (313.16, -74.83, 0.03),
                       (46.84, -74.83, 0.03),
                       (241.16, -74.83, 0.03),
                       (118.84, -74.83, 0.03),
                       (262.84, -74.83, 0.03),
                       (97.16, -74.83, 0.03),
                       (334.84, -74.83, 0.03),
                       (25.16, -74.83, 0.03),
                       (180.0, -73.69, 0.03),
                       (252.0, -73.69, 0.03),
                       (108.0, -73.69, 0.03),
                       (324.0, -73.69, 0.03),
                       (36.0, -73.69, 0.03),
                       (210.39, -73.29, 0.03),
                       (149.61, -73.29, 0.03),
                       (293.61, -73.29, 0.03),
                       (66.39, -73.29, 0.03),
                       (221.61, -73.29, 0.03),
                       (138.39, -73.29, 0.03),
                       (354.39, -73.29, 0.03),
                       (5.61, -73.29, 0.03),
                       (282.39, -73.29, 0.03),
                       (77.61, -73.29, 0.03),
                       (199.43, -72.9, 0.03),
                       (160.57, -72.9, 0.03),
                       (232.57, -72.9, 0.03),
                       (127.43, -72.9, 0.03),
                       (271.43, -72.9, 0.03),
                       (88.57, -72.9, 0.03),
                       (343.43, -72.9, 0.03),
                       (16.57, -72.9, 0.03),
                       (304.57, -72.9, 0.03),
                       (55.43, -72.9, 0.03),
                       (242.81, -72.1, 0.03),
                       (117.19, -72.1, 0.03),
                       (314.81, -72.1, 0.03),
                       (45.19, -72.1, 0.03),
                       (333.19, -72.1, 0.03),
                       (26.81, -72.1, 0.03),
                       (189.19, -72.1, 0.03),
                       (170.81, -72.1, 0.03),
                       (261.19, -72.1, 0.03),
                       (98.81, -72.1, 0.03),
                       (288.0, -70.93, 0.03),
                       (72.0, -70.93, 0.03),
                       (216.0, -70.93, 0.03),
                       (144.0, -70.93, 0.03),
                       (0.0, -70.93, 0.03),
                       (180.0, -70.92, 0.03),
                       (252.0, -70.92, 0.03),
                       (108.0, -70.92, 0.03),
                       (324.0, -70.92, 0.03),
                       (36.0, -70.92, 0.03),
                       (297.78, -70.76, 0.03),
                       (62.22, -70.76, 0.03),
                       (278.22, -70.76, 0.03),
                       (81.78, -70.76, 0.03),
                       (225.78, -70.76, 0.03),
                       (134.22, -70.76, 0.03),
                       (350.22, -70.76, 0.03),
                       (9.78, -70.76, 0.03),
                       (206.22, -70.76, 0.03),
                       (153.78, -70.76, 0.03),
                       (196.78, -70.23, 0.03),
                       (163.22, -70.23, 0.03),
                       (235.22, -70.23, 0.03),
                       (124.78, -70.23, 0.03),
                       (340.78, -70.23, 0.03),
                       (19.22, -70.23, 0.03),
                       (307.22, -70.23, 0.03),
                       (52.78, -70.23, 0.03),
                       (268.78, -70.23, 0.03),
                       (91.22, -70.23, 0.03),
                       (244.02, -69.35, 0.03),
                       (115.98, -69.35, 0.03),
                       (331.98, -69.35, 0.03),
                       (28.02, -69.35, 0.03),
                       (259.98, -69.35, 0.03),
                       (100.02, -69.35, 0.03),
                       (316.02, -69.35, 0.03),
                       (43.98, -69.35, 0.03),
                       (187.98, -69.35, 0.03),
                       (172.02, -69.35, 0.03),
                       (283.64, -68.47, 0.03),
                       (76.36, -68.47, 0.03),
                       (220.36, -68.47, 0.03),
                       (139.64, -68.47, 0.03),
                       (211.64, -68.47, 0.03),
                       (148.36, -68.47, 0.03),
                       (292.36, -68.47, 0.03),
                       (67.64, -68.47, 0.03),
                       (355.64, -68.47, 0.03),
                       (4.36, -68.47, 0.03),
                       (203.03, -68.15, 0.03),
                       (156.97, -68.15, 0.03),
                       (275.03, -68.15, 0.03),
                       (84.97, -68.15, 0.03),
                       (228.97, -68.15, 0.03),
                       (131.03, -68.15, 0.03),
                       (347.03, -68.15, 0.03),
                       (12.97, -68.15, 0.03),
                       (300.97, -68.15, 0.03),
                       (59.03, -68.15, 0.03),
                       (180.0, -68.12, 0.03),
                       (252.0, -68.12, 0.03),
                       (108.0, -68.12, 0.03),
                       (324.0, -68.12, 0.03),
                       (36.0, -68.12, 0.03),
                       (194.77, -67.52, 0.03),
                       (165.23, -67.52, 0.03),
                       (237.23, -67.52, 0.03),
                       (122.77, -67.52, 0.03),
                       (266.77, -67.52, 0.03),
                       (93.23, -67.52, 0.03),
                       (309.23, -67.52, 0.03),
                       (50.77, -67.52, 0.03),
                       (338.77, -67.52, 0.03),
                       (21.23, -67.52, 0.03),
                       (331.05, -66.57, 0.03),
                       (28.95, -66.57, 0.03),
                       (316.95, -66.57, 0.03),
                       (43.05, -66.57, 0.03),
                       (244.95, -66.57, 0.03),
                       (115.05, -66.57, 0.03),
                       (172.95, -66.57, 0.03),
                       (187.05, -66.57, 0.03),
                       (259.05, -66.57, 0.03),
                       (100.95, -66.57, 0.03),
                       (0.0, -66.07, 0.03),
                       (216.0, -66.07, 0.03),
                       (144.0, -66.07, 0.03),
                       (288.0, -66.07, 0.03),
                       (72.0, -66.07, 0.03),
                       (151.83, -65.93, 0.03),
                       (64.17, -65.93, 0.03),
                       (295.83, -65.93, 0.03),
                       (223.83, -65.93, 0.03),
                       (136.17, -65.93, 0.03),
                       (352.17, -65.93, 0.03),
                       (7.83, -65.93, 0.03),
                       (280.17, -65.93, 0.03),
                       (79.83, -65.93, 0.03),
                       (272.52, -65.5, 0.03),
                       (87.48, -65.5, 0.03),
                       (231.48, -65.5, 0.03),
                       (128.52, -65.5, 0.03),
                       (159.48, -65.5, 0.03),
                       (303.48, -65.5, 0.03),
                       (56.52, -65.5, 0.03),
                       (344.52, -65.5, 0.03),
                       (15.48, -65.5, 0.03),
                       (252.0, -65.32, 0.03),
                       (108.0, -65.32, 0.03),
                       (324.0, -65.32, 0.03),
                       (36.0, -65.32, 0.03),
                       (166.8, -64.78, 0.03),
                       (238.8, -64.78, 0.03),
                       (121.2, -64.78, 0.03),
                       (310.8, -64.78, 0.03),
                       (49.2, -64.78, 0.03),
                       (265.2, -64.78, 0.03),
                       (94.8, -64.78, 0.03),
                       (337.2, -64.78, 0.03),
                       (22.8, -64.78, 0.03),
                       (245.67, -63.78, 0.03),
                       (114.33, -63.78, 0.03),
                       (258.33, -63.78, 0.03),
                       (101.67, -63.78, 0.03),
                       (317.67, -63.78, 0.03),
                       (42.33, -63.78, 0.03),
                       (330.33, -63.78, 0.03),
                       (29.67, -63.78, 0.03),
                       (147.56, -63.58, 0.03),
                       (356.44, -63.58, 0.03),
                       (3.56, -63.58, 0.03),
                       (291.56, -63.58, 0.03),
                       (68.44, -63.58, 0.03),
                       (140.44, -63.58, 0.03),
                       (284.44, -63.58, 0.03),
                       (75.56, -63.58, 0.03),
                       (298.61, -63.32, 0.03),
                       (61.39, -63.32, 0.03),
                       (133.39, -63.32, 0.03),
                       (277.39, -63.32, 0.03),
                       (82.61, -63.32, 0.03),
                       (154.61, -63.32, 0.03),
                       (349.39, -63.32, 0.03),
                       (10.61, -63.32, 0.03),
                       (161.48, -62.8, 0.03),
                       (270.52, -62.8, 0.03),
                       (89.48, -62.8, 0.03),
                       (126.52, -62.8, 0.03),
                       (342.52, -62.8, 0.03),
                       (17.48, -62.8, 0.03),
                       (305.48, -62.8, 0.03),
                       (54.52, -62.8, 0.03),
                       (252.0, -62.51, 0.03),
                       (108.0, -62.51, 0.03),
                       (324.0, -62.51, 0.03),
                       (36.0, -62.51, 0.03),)

        rlist = []
        for ur in __regions__:
            rlist.append(baseField.UserRegionConfig(ra=ur[0], dec=ur[1],
                                                    diameter=ur[2]))
        return utils.makeIntDict(rlist)
