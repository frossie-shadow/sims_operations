import base
import utils

__all__ = ["UnscheduledDowntime"]

class UnscheduledDowntime(base.DowntimeConfig):
    """
    List of unscheduled downtimes.
    DO NOT MODIFY UNLESS YOU TALK TO CHUCK CLAVER!
    """
    _rawEvents = (('intermediate event', 3, 3),
                  ('minor event', 22, 1),
                  ('minor event', 30, 1),
                  ('minor event', 44, 1),
                  ('minor event', 246, 1),
                  ('intermediate event', 296, 3),
                  ('minor event', 356, 1),
                  ('minor event', 402, 1),
                  ('minor event', 436, 1),
                  ('major event', 486, 7),
                  ('minor event', 507, 1),
                  ('minor event', 571, 1),
                  ('intermediate event', 710, 3),
                  ('intermediate event', 733, 3),
                  ('minor event', 757, 1),
                  ('intermediate event', 880, 3),
                  ('major event', 939, 7),
                  ('minor event', 958, 1),
                  ('major event', 1020, 7),
                  ('intermediate event', 1148, 3),
                  ('minor event', 1156, 1),
                  ('minor event', 1161, 1),
                  ('intermediate event', 1178, 3),
                  ('minor event', 1201, 1),
                  ('minor event', 1212, 1),
                  ('minor event', 1223, 1),
                  ('minor event', 1274, 1),
                  ('intermediate event', 1288, 3),
                  ('minor event', 1307, 1),
                  ('minor event', 1316, 1),
                  ('intermediate event', 1334, 3),
                  ('minor event', 1517, 1),
                  ('minor event', 1526, 1),
                  ('catastrophic event', 1591, 14),
                  ('minor event', 1637, 1),
                  ('minor event', 1707, 1),
                  ('minor event', 1738, 1),
                  ('major event', 1762, 7),
                  ('minor event', 1813, 1),
                  ('minor event', 1822, 1),
                  ('major event', 1847, 7),
                  ('minor event', 1883, 1),
                  ('minor event', 1888, 1),
                  ('minor event', 2065, 1),
                  ('minor event', 2087, 1),
                  ('minor event', 2119, 1),
                  ('intermediate event', 2158, 3),
                  ('minor event', 2237, 1),
                  ('minor event', 2269, 1),
                  ('minor event', 2301, 1),
                  ('minor event', 2315, 1),
                  ('intermediate event', 2356, 3),
                  ('minor event', 2376, 1),
                  ('minor event', 2378, 1),
                  ('minor event', 2524, 1),
                  ('minor event', 2527, 1),
                  ('intermediate event', 2583, 3),
                  ('minor event', 2698, 1),
                  ('minor event', 2702, 1),
                  ('intermediate event', 2724, 3),
                  ('minor event', 2738, 1),
                  ('intermediate event', 2758, 3),
                  ('minor event', 2799, 1),
                  ('intermediate event', 2812, 3),
                  ('minor event', 2825, 1),
                  ('intermediate event', 2991, 3),
                  ('intermediate event', 3027, 3),
                  ('intermediate event', 3089, 3),
                  ('intermediate event', 3135, 3),
                  ('minor event', 3218, 1),
                  ('minor event', 3219, 1),
                  ('minor event', 3307, 1),
                  ('minor event', 3310, 1),
                  ('intermediate event', 3328, 3),
                  ('minor event', 3354, 1),
                  ('minor event', 3378, 1),
                  ('minor event', 3381, 1),
                  ('minor event', 3424, 1),
                  ('minor event', 3440, 1),
                  ('intermediate event', 3644, 3))

    def setDefaults(self):
        """
        Create the list of downtime events.
        """
        base.DowntimeConfig.setDefaults(self)
        elist = []
        for ev in self._rawEvents:
            elist.append(base.DowntimeEventConfig(activity=ev[0],
                                                  startNight=ev[1],
                                                  duration=ev[2]))

        self.events = utils.makeIntDict(elist)
