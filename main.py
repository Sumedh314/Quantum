from duet_3d_dev import Duet3dDev
from ScopeFoundry import BaseApp


class duet3d(BaseApp):
    def setup(self):
        pass


duet = Duet3dDev

if __name__ == '__main__':
    import sys
    
    app = duet3d(sys.argv)
    sys.exit(app.exec_())