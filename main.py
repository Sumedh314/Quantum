from duet_3d_dev import Duet3dDev
from ScopeFoundry import BaseMicroscopeApp


class Duet3d(BaseMicroscopeApp):

    name = 'microscope'

    def setup(self):
        from duet_3d_hw import Duet3dHW
        self.add_hardware(Duet3dHW(self))

        self.ui.show()
        self.ui.activateWindow()


duet = Duet3dDev()

if __name__ == '__main__':
    import sys
    
    app = Duet3d(sys.argv)
    sys.exit(app.exec_())