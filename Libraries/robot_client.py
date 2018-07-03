import sys
import socket
import errno
from rr_constants import *

MAX_MESSAGE_LEN = 4096


class RobotClient:
    """
    client for sending robot requests
    """

    ip = None
    port = None
    client_socket = None

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        # TODO read from conf file?

    def connect(self):
        """
        connect to robot service
        :param self:
        :return: True/False
        """
        server_address = (self.ip, self.port)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(server_address)
        self.client_socket.setblocking(1)

        return True # TODO handle exceptions

    def close(self):
        """
        close connection with the robot service
        :param self:
        :return: True/False
        """
        if self.client_socket is not None:
            self.client_socket.close()
            self.client_socket = None

        return True

    def send_message(self, message, msg_id):
        """
        Send message to robot service
        :param message: message to send
        :param id: message id
        :return:
        """
        response = ''

        try:
            if self.client_socket is None:
                self.connect()

            byte_array = self.add_crc16(message)  # add CRC
            print("Sending message: " + protocol_message_to_string(byte_array))
            self.client_socket.sendall(byte_array)

            if message[0] != ACK and message[0] != NAK and message[0] != EOT:   # wait for response
                response = self.receive_message(msg_id)

        except socket.error:
            print("Error: socket connection")

        return response

    def receive_message(self, msg_id):
        """
        recevie message from robot service, verify CRC
        :param max_bytes_to_read: maximum bytes to read
        :param msg_id: messge id
        :return:
        """
        if self.client_socket is None:
            return ''
        message = self.read_message()

        if len(message) > 3:
            # check crc
            calc_crc = self.crc16(message[:-2])

            rcv_crc = message[len(message)-2] & 0x00ff
            rcv_crc = rcv_crc << 8
            rcv_crc += message[len(message)-1] & 0x00ff

            if calc_crc != rcv_crc:
                print('Calculated CRC: ' + format(calc_crc, '#04x'))
                print('Received CRC:   ' + format(rcv_crc, '#04x'))
                response = bytearray()
                response += bytearray([NAK])
                response.extend(map(ord, str(msg_id).zfill(2)))
                self.send_message(response, msg_id)
                # TODO count for EOT
            else:
                response = bytearray()
                response += bytearray([ACK])
                response.extend(map(ord, str(msg_id).zfill(2)))
                self.send_message(response, msg_id)
        # TODO verify message ID

        return message

    def read_message(self):
        """
        Read message from robot service
        :return: bytearray of message
        """
        data = bytearray()
        while True:    # TODO add timeout
            try:
                data += self.client_socket.recv(1)

                if len(data) >= 3:
                    if data[-3] == ACK or data[-3] == NAK or data[-3] == EOT or data[-3] == ETX:
                        break

            except socket.error as e:
                if e.errno == errno.EAGAIN:
                    continue
                else:
                    print('socket error: ' + str(e.errno))
                    break

        print('received: ' + protocol_message_to_string(data))

        return data

    @staticmethod
    def crc16(data):
        """
        calculate CRC16 over given data
        :param data: data to calculate CRC16 on
        :return: CRC16 over data
        """
        crc = 0xffff

        for j in range(0, len(data)):
            crc = ((crc >> 8) | (crc << 8)) & 0xffff
            crc ^= (data[j] & 0xff)
            crc ^= ((crc & 0xff) >> 4)
            crc ^= (crc << 12) & 0xffff
            crc ^= ((crc & 0xFF) << 5) & 0xffff

        crc &= 0xffff;
        # print('Calculated CRC: ' + format(crc, '#04x'))
        return crc

    def add_crc16(self, message):
        """
        catenate CRC16 to data
        :param message: data to calculate CRC16 on
        :return: catenate of message and CRC16
        """
        crc = self.crc16(message)
        message += bytearray([(crc & 0xff00) >> 8])
        message += bytearray([crc & 0x00ff])

        return message


def protocol_message_to_string(message):
    str_message = ''

    for c in message:
        if c == STX:
            str_message += "<STX>"
        elif c == ETX:
            str_message += "<ETX>"
        elif c == EOT:
            str_message += "<EOT>"
        elif c == ACK:
            str_message += "<ACK>"
        elif c == NAK:
            str_message += "<NAK>"
        elif c == FS:
            str_message += "<FS>"
        elif c == RS:
            str_message += "<RS>"
        elif ord(' ') <= c <= ord('~'):    # printable characters
            str_message += chr(c)
        elif c == 0:
            str_message = str_message   # do nothing
        else:
            str_message += '\\x' + format(c, '02x');

    return str_message