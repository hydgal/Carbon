import time
from request_parser import RequestParser
def send_message():
    rp = RequestParser('sjcwvcorafw1', 55555)
    response = rp.send_acquire_command("401-181-390")
    print(str(response))
    print "this is test"

def contactless():
    rp = RequestParser('sjcwvcorafw1', 55555)
    response = rp.send_acquire_command("401-181-390")
    print(str(response))

    rp.send_ctls_command("401-181-390", "2", "F", "1", "1", "0")
    time.sleep(1)
    #rp.send_touch_command("401-181-390", 'S', '(15, 20)', '200', '1', '0')
    #time.sleep(1)
    rp.send_release_command("401-181-390")



def chip_insert():
    rp = RequestParser('sjcwvcorafw1', 55555)
    response = rp.send_acquire_command("401-181-390")
    print(str(response))

    rp.send_scr_command("401-181-390", '1', 'F', '6', '1', '0')
    time.sleep(1)
    #rp.send_touch_command("401-181-390", 'S', '(15, 20)', '200', '1', '0')
    #time.sleep(1)
    rp.send_release_command("401-181-390")


def swipe_card():
    rp = RequestParser('sjcwvcorafw1', 55555)
    response = rp.send_acquire_command("401-181-390")
    print(str(response))

    rp.send_msr_command("401-181-390", 'ALL_TRACKS', 'N', '200', '1', '0')
    time.sleep(1)
    rp.send_touch_command("401-181-390", 'S', '(25, 14)', '200', '1', '0')
    #time.sleep(1)
    rp.send_release_command("401-181-390")