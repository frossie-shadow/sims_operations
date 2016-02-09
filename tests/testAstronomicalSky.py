import unittest

import lsst.sims.operations.Database as DB
import lsst.sims.operations.AstronomicalSky as AS
import lsst.sims.operations.utilities as utilities

class TestAstronomicalSky(unittest.TestCase):

    def setUp(self):
        """
        Setup necessary objects for creating an AstronomicalSky instance.
        """
        self.db = DB.Database(False, dbConnect=False)

        # Setup observatory profile
        configDict, pairs = utilities.readConfFile("example_conf/system/SiteCP.conf")
        simStartDay = 0.0
        obsProfile = (configDict["longitude"] * utilities.DEG2RAD,
                      configDict["latitude"] * utilities.DEG2RAD,
                      configDict["height"],
                      configDict["seeingEpoch"] + simStartDay,
                      configDict["pressure"],
                      configDict["temperature"],
                      configDict["relativeHumidity"])

        self.sky = AS.AstronomicalSky(self.db, obsProfile, 0., 1, {},
                                      configFile="example_conf/system/AstronomicalSky.conf")

    def tearDown(self):
        self.db.closeConnection()

    def testLsstVSkyBrightness(self):
        date = 2922.8256
        dp = self.sky.computeDateProfile(date)
        mp = self.sky.computeMoonProfile(date)

        (sb, moon_dist, moon_alt) = self.sky.getLsstVSkyBrightness(96.055377, -62.021153, dp, mp)
        self.assertEquals(sb, 19.519380023758721)
        self.assertAlmostEqual(moon_dist, 1.621921, delta=1e-6)
        self.assertAlmostEqual(moon_alt, -0.493971, delta=1e-6)

    def testSkyBrightnessForFilter(self):
        ofilter = 'y'
        mjd = 59580.033829
        ra = 1.676483
        dec = -1.082473
        sb = self.sky.getSkyBrightnessForFilter(ra, dec, ofilter, mjd)
        self.assertAlmostEqual(sb, 16.46207046, delta=1e-7)

if __name__ == "__main__":
    unittest.main()