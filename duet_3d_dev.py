import requests


class Duet3dDev(object):
    # Create new object
    def __init__(self):
        self.ip_address = 'cataloger.local'


    # Home all the axes
    def home_axes(self):
        # G28 homes all the axes
        self.send_gcode('G28')


    # Move the X axis relative to its current position
    def move_x_relative(self, value):
        self.send_gcode('G91')

        gcode = f'G1 X{value}'
        self.send_gcode(gcode)

    # Move the Y axis relative to its current position
    def move_y_relative(self, value):
        self.send_gcode('G91')

        gcode = f'G1 Y{value}'
        self.send_gcode(gcode)

    # Move the Z axis relative to its current position
    def move_z_relative(self, value):
        self.send_gcode('G91')

        gcode = f'G1 Z{value}'
        self.send_gcode(gcode)


    # Move the X axis to an absolute position
    def move_x_absolute(self, value):
        self.send_gcode('G90')

        gcode = f'G1 X{value}'
        self.send_gcode(gcode)

    # Move the Y axis to an absolute position
    def move_y_absolute(self, value):
        self.send_gcode('G90')

        gcode = f'G1 Y{value}'
        self.send_gcode(gcode)

    # Move the Z axis to an absolute position
    def move_z_absolute(self, value):
        self.send_gcode('G90')

        gcode = f'G1 Z{value}'
        self.send_gcode(gcode)


    # Set the temperature of the extruder
    def set_temperature(self, temperature):
        gcode = f'M104 S{temperature}'
        self.send_gcode(gcode)

    # Send any gcode to the Duet 3D
    def send_gcode(self, gcode):
        params = {'gcode': gcode}
        response = requests.get(f'http://{self.ip_address}/rr_gcode', params)
        if response.status_code == 200:
            return response
        else:
            return 'Error'