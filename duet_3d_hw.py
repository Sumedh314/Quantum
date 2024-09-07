from ScopeFoundry import HardwareComponent
from duet_3d_dev import Duet3dDev


class Duet3dHW(HardwareComponent):

    name = 'duet3d'

    # Add settings to the GUI
    def setup(self):
        self.settings.New(name='ip_address', dtype=str, initial='cataloger.local')
        self.settings.New(name='temperature', dtype=float, ro=True)
        self.settings.New(name='status', dtype=str, ro=True)

        self.settings.New(name='x_position', dtype=float, unit='mm')
        self.settings.New(name='y_position', dtype=float, unit='mm')
        self.settings.New(name='z_position', dtype=float, unit='mm')

    # Connect to device
    def connect(self):
        self.duet3d_dev = Duet3dDev()

        self.settings.ip_address.connect_to_hardware()
        self.settings.status.connect_to_hardware()

        self.settings.temperature.connect_to_hardware(
            write_func = self.duet3d_dev.set_temperature
        )

        self.settings.x_position.connect_to_hardware(
            write_func = self.duet3d_dev.move_x_absolute
        )
        self.settings.y_position.connect_to_hardware(
            write_func = self.duet3d_dev.move_y_absolute
        )
        self.settings.z_position.connect_to_hardware(
            write_func = self.duet3d_dev.move_z_absolute
        )
        
        self.read_from_hardware()

    # Remove connection to device
    def disconnect(self):
        self.settings.disconnect_all_from_hardware()

        if hasattr(self, 'duet3d_dev'):
            del self.duet3d_dev