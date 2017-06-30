class Player:
    def __init__(self, name, sex, vocation, level, ach_points, world, residence, last_log):#, acc_status):
        self.name = name
        self.sex = sex
        self.vocation = vocation
        self.level = level
        self.ach_points = ach_points
        self.world = world
        self.residence = residence
        self.last_log = last_log
        # Complex - To be developed
        # self.acc_status = acc_status

    @property
    def name(self):
        """I'm the 'name' property."""
        print("getter of name called")
        return self._name

    @property
    def sex(self):
        """I'm the 'sex' property."""
        print("getter of sex called")
        return self._sex

    @property
    def vocation(self):
        """I'm the 'vocation' property."""
        print("getter of vocation called")
        return self._vocation

    @property
    def level(self):
        """I'm the 'level' property."""
        print("getter of level called")
        return self._level

    @property
    def ach_points(self):
        """I'm the 'ach_points' property."""
        print("getter of ach_points called")
        return self._ach_points

    @property
    def world(self):
        """I'm the 'world' property."""
        print("getter of world called")
        return self._world

    @property
    def residence(self):
        """I'm the 'residence' property."""
        print("getter of residence called")
        return self._residence

    @property
    def last_log(self):
        """I'm the 'last_log' property."""
        print("getter of last_log called")
        return self._last_log

    # @property
    # def acc_status(self):
    #     """I'm the 'acc_status' property."""
    #     print("getter of acc_status called")
    #     return self._acc_status