import sys
from robot_client import RobotClient
from rr_constants import *

MAX_ID = 99


class RequestParser:
    """
    Parse robot requests
    """
    init_id = False
    msg_id = 1
    client = None

    def __init__(self, address, port):
        """
        Initialize request parser
        :param address: robot service address
        :param port: robot service port
        """
        self.client = RobotClient(address, port)

    def get_next_id(self):
        """
        increment and return message id
        :return: message id
        """
        self.msg_id = (self.msg_id + 2) % MAX_ID
        return self.msg_id

    @staticmethod
    def add_string_to_byte_array(array, string):
        """
        add string to byte array
        :param array: array to add to
        :param string: string to add
        :return: array with string at the end
        """
        tmp_array = bytearray()
        tmp_array.extend(map(ord, string))
        return array + tmp_array

    def build_protocol_message(self, fileds_arr):
        """
        build protocol message with given fields
        :param fileds_arr: fields array
        :return: protocol command from given fields
        """
        message = bytearray()

        message += bytearray([STX])

        for field in fileds_arr:
            message = self.add_string_to_byte_array(message, field)
            message += bytearray([FS])

        message += bytearray([ETX])

        return message

    def send_action_command(self, message, msg_id):
        """
        send robot action command using robot client
        :param message: message to send
        :param msg_id: message id
        :return: response from robot service as byte array
        """
        self.client.connect()

        response = self.client.send_message(message, msg_id)

        if response[0] != ACK:
            print('Error: failure in sending message to robot service')

        self.client.close()

        return response

    @staticmethod
    def extract_response(response):
        if response is None:
            print("Error: response is None")
            return response
        elif response[0] == ACK:
            return RESPONSE_ACK
        elif response[0] == NAK:
            return RESPONSE_NAK
        elif response[0] == EOT:
            return RESPONSE_EOT
        elif response[4] == ord('6') and response[5] == ord('9'):
            return RESPONSE_DENIED
        elif response[4] == ord('6') and response[5] == ord('8'):
            return RESPONSE_ACCEPTED
        else:
            print("Error: response is not defined")
            return None

    def serialize_command_acquire(self, unit_id, timeout):
        """
        create a robot command according to protocol
        :param unit_id: unit id
        :param timeout: timeout for acquire
        :return: robot acquire command according to protocol
        """
        filed_arr = list()

        filed_arr.append(str(self.get_next_id()).zfill(2))
        filed_arr.append(RTYPE_R_ACQUIRE)
        filed_arr.append(unit_id)
        filed_arr.append(timeout)

        return self.build_protocol_message(filed_arr)

    def serialize_command_release(self, unit_id):
        """
        create a robot release command according to protocol
        :param unit_id: unit id
        :return: robot release command according to protocol
        """
        filed_arr = list()

        filed_arr.append(str(self.get_next_id()).zfill(2))
        filed_arr.append(RTYPE_R_RELEASE)
        filed_arr.append(unit_id)

        return self.build_protocol_message(filed_arr)

    def serialize_command_abort(self, unit_id):
        """
        create a robot abort command according to protocol
        :param unit_id: unit id
        :return: robot release command according to protocol
        """
        filed_arr = list()

        filed_arr.append(str(self.get_next_id()).zfill(2))
        filed_arr.append(RTYPE_R_ABORT)
        filed_arr.append(unit_id)

        return self.build_protocol_message(filed_arr)

    def serialize_command_ctls(self, unit_id, card_label, action, timeout, iterations, delay):
        """
        create a robot CTLS command according to protocol
        :param unit_id: unit id
        :param card_label: card label
        :param action: action (I - introduce, R - remove, F - full)
        :param timeout: timeout for F action
        :param iterations: number of iterations
        :param delay: delay before start of operations
        :return: robot CTLS command according to protocol
        """
        filed_arr = list()

        filed_arr.append(str(self.get_next_id()).zfill(2))
        filed_arr.append(RTYPE_R_CTLS)
        filed_arr.append(unit_id)
        filed_arr.append(card_label)
        filed_arr.append(action)
        filed_arr.append(timeout)
        filed_arr.append(iterations)
        filed_arr.append(delay)

        return self.build_protocol_message(filed_arr)

    def serialize_command_msr(self, unit_id, card_label, direction, speed, iterations, delay):
        """
        create a robot MSr command according to protocol
        :param unit_id: unit id
        :param card_label: card label
        :param direction: action (N - normal, R - reverse)
        :param speed: swipe speed
        :param iterations: number of iterations
        :param delay: delay before start of operations
        :return: robot MSR command according to protocol
        """
        filed_arr = list()

        filed_arr.append(str(self.get_next_id()).zfill(2))
        filed_arr.append(RTYPE_R_MSR)
        filed_arr.append(unit_id)
        filed_arr.append(card_label)
        filed_arr.append(direction)
        filed_arr.append(speed)
        filed_arr.append(iterations)
        filed_arr.append(delay)

        return self.build_protocol_message(filed_arr)

    def serialize_command_scr(self, unit_id, card_label, action, timeout, iterations, delay):
        """
        create a robot SCR command according to protocol
        :param unit_id: unit id
        :param card_label: card label
        :param action: action (I - insert, R - remove, F - full)
        :param timeout: timeout for F action
        :param iterations: number of iterations
        :param delay: delay before start of operations
        :return: robot SCR command according to protocol
        """
        filed_arr = list()

        filed_arr.append(str(self.get_next_id()).zfill(2))
        filed_arr.append(RTYPE_R_SCR)
        filed_arr.append(unit_id)
        filed_arr.append(card_label)
        filed_arr.append(action)
        filed_arr.append(timeout)
        filed_arr.append(iterations)
        filed_arr.append(delay)

        return self.build_protocol_message(filed_arr)

    def serialize_command_keypad(self, unit_id, sequence, inter_daley, iterations, delay):
        """
        create a robot keypad command according to protocol
        :param unit_id: unit id
        :param sequence: key press sequence
        :param inter_daley: delay between presses
        :param iterations: number of iterations
        :param delay: delay before start of operations
        :return: robot keypad command according to protocol
        """
        filed_arr = list()

        filed_arr.append(str(self.get_next_id()).zfill(2))
        filed_arr.append(RTYPE_R_KEYPAD)
        filed_arr.append(unit_id)
        filed_arr.append(sequence)
        filed_arr.append(inter_daley)
        filed_arr.append(iterations)
        filed_arr.append(delay)

        return self.build_protocol_message(filed_arr)

    def serialize_command_touch(self, unit_id, input_type, sequence, speed, iterations, delay):
        """
        create a robot touch command according to protocol
        :param unit_id: unit id
        :param input_type: S - sequence, F - file id
        :param sequence: key press sequence
        :param speed: speed of movement in mm/s
        :param delay: delay before start of operations
        :return: robot touch command according to protocol
        """
        filed_arr = list()

        filed_arr.append(str(self.get_next_id()).zfill(2))
        filed_arr.append(RTYPE_R_TOUCH)
        filed_arr.append(unit_id)
        filed_arr.append(input_type)
        filed_arr.append(sequence)
        filed_arr.append(speed)
        filed_arr.append(iterations)
        filed_arr.append(delay)

        return self.build_protocol_message(filed_arr)

    def serialize_command_barcode(self, unit_id, barcode_id, action, duration, speed, distance, rotation):
        """
        create a robot touch command according to protocol
        :param unit_id: unit id
        :param barcode_id: barcode id
        :param action: FS - full, FS - full & rotate, I - introduce, R - remove, AtoB - from A to B
        :param duration: duration in msec
        :param speed: speed of movement in mm/s
        :param distance: Millimeters from base position
        :param rotation: rotation in in degrees/mm (Xrotation, Yrotation, Zrotation, step)
        :return: robot touch command according to protocol
        """
        filed_arr = list()

        filed_arr.append(str(self.get_next_id()).zfill(2))
        filed_arr.append(RTYPE_R_BARCODE)
        filed_arr.append(unit_id)
        filed_arr.append(barcode_id)
        filed_arr.append(action)
        filed_arr.append(duration)
        filed_arr.append(speed)
        filed_arr.append(distance)
        filed_arr.append(rotation)

        return self.build_protocol_message(filed_arr)

    def serialize_command_nfc(self, unit_id, phone_id, app, card_label, position, pos_details, duration):
        """
        create a robot NFC command according to protocol
        :param unit_id: unit_id: unit id
        :param phone_id: phone id
        :param app: application name
        :param card_label: card label
        :param position: P - portrait / L - Landscape / F - Flipped portrait
        :param pos_details: rotation in in degrees/mm (X rotation, Y rotation, Z rotation, step)
        :param duration: duration to leave phone next to unit in miliseconds
        :return: robot NFC command according to protocol
        """
        filed_arr = list()

        filed_arr.append(str(self.get_next_id()).zfill(2))
        filed_arr.append(RTYPE_R_NFC)
        filed_arr.append(unit_id)
        filed_arr.append(phone_id)
        filed_arr.append(app)
        filed_arr.append(card_label)
        filed_arr.append(position)
        filed_arr.append(pos_details)
        filed_arr.append(duration)

        return self.build_protocol_message(filed_arr)

    def send_acquire_command(self, unit_id):
        """
        send a robot acquire command to robot service
        :param unit_id: unit id of the unit to acquire
        :return: robot service response as byte array
        """
        message = self.serialize_command_acquire(unit_id, '120')

        self.client.connect()
        response = self.client.send_message(message, self.msg_id)

        if response[0] == ACK:
            response = self.client.receive_message(self.msg_id)

        self.client.close()
        return response

    def send_release_command(self, unit_id):
        """
        send a robot release command to robot service
        :param unit_id: unit id of the unit to release
        :return: robot service response as byte array
        """
        message = self.serialize_command_release(unit_id)

        return self.send_action_command(message, self.msg_id)

    def send_ctls_command(self, unit_id, card_label, action, timeout, iterations, delay):
        """
        send a robot CTLS command to robot service
        :param unit_id: unit id
        :param card_label: card label
        :param action: action (I - introduce, R - remove, F - full)
        :param timeout: timeout for F action
        :param iterations: number of iterations
        :param delay: delay before start of operations
        :return: robot service response as byte array
        """
        message = self.serialize_command_ctls(unit_id, card_label, action, timeout, iterations, delay)

        return self.send_action_command(message, self.msg_id)

    def send_msr_command(self, unit_id, card_label, direction, speed, iterations, delay):
        """
        send a robot MSR command to robot service
        :param unit_id: unit id
        :param card_label: card label
        :param direction: action (N - normal, R - reverse)
        :param speed: swipe speed
        :param iterations: number of iterations
        :param delay: delay before start of operations
        :return: robot service response as byte array
        """
        message = self.serialize_command_msr(unit_id, card_label, direction, speed, iterations, delay)

        return self.send_action_command(message, self.msg_id)

    def send_scr_command(self, unit_id, card_label, action, timeout, iterations, delay):
        """
        send a robot SCR command to robot service
        :param unit_id: unit id
        :param card_label: card label
        :param action: action (I - insert, R - remove, F - full)
        :param timeout: timeout for F action
        :param iterations: number of iterations
        :param delay: delay before start of operations
        :return: robot service response as byte array
        """
        message = self.serialize_command_scr(unit_id, card_label, action, timeout, iterations, delay)

        return self.send_action_command(message, self.msg_id)

    def send_keypad_command(self, unit_id, sequence, inter_daley, iterations, delay):
        """
        send a robot keypad command to robot service
        :param unit_id: unit id
        :param sequence: key press sequence
        :param inter_daley: delay between presses
        :param iterations: number of iterations
        :param delay: delay before start of operations
        :return: robot service response as byte array
        """
        message = self.serialize_command_keypad(unit_id, sequence, inter_daley, iterations, delay)

        return self.send_action_command(message, self.msg_id)

    def send_touch_command(self, unit_id, input_type, sequence, speed, iterations, delay):
        """
        send a robot touch command robot service
        :param unit_id: unit id
        :param input_type: S - sequence, F - file id
        :param sequence: key press sequence
        :param speed: speed of movement in mm/s
        :param delay: delay before start of operations
        :return: robot service response as byte array
        """
        message = self.serialize_command_touch(unit_id, input_type, sequence, speed, iterations, delay)

        return self.send_action_command(message, self.msg_id)

    def send_barcode_command(self, unit_id, barcode_id, action, duration, speed, distance, rotation):
        """
        send a robot barcode command to robot service
        :param unit_id: unit id
        :param barcode_id: barcode id
        :param action: FS - full, FS - full & rotate, I - introduce, R - remove, AtoB - from A to B
        :param duration: duration in msec
        :param speed: speed of movement in mm/s
        :param distance: Millimeters from base position
        :param rotation: rotation in in degrees/mm (X rotation, Y rotation, Z rotation, step)
        :return: robot service response as byte array
        """
        message = self.serialize_command_barcode(unit_id, barcode_id, action, duration, speed, distance, rotation)

        return self.send_action_command(message, self.msg_id)

    def send_nfc_command(self, unit_id, phone_id, app, card_label, position, pos_details, duration):
        """
        send a robot NFC command to robot service
        :param unit_id: unit_id: unit id
        :param phone_id: phone id
        :param app: application name
        :param card_label: card label
        :param position: P - portrait / L - Landscape / F - Flipped portrait
        :param pos_details: rotation in in degrees/mm (X rotation, Y rotation, Z rotation, step)
        :param duration: duration to leave phone next to unit in miliseconds
        :return: robot service response as byte array
        """
        message = self.serialize_command_nfc(unit_id, phone_id, app, card_label, position, pos_details, duration)

        return self.send_action_command(message, self.msg_id)