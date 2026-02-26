
from .AOTF import AOTF64Bit as AOTFclass
from time import sleep

def AOTF_init():
    my_aotf = AOTFclass()
    return my_aotf

def AOTF_boardID(my_aotf):
    if not my_aotf.getStatus():
        exit()
    else:
        res = my_aotf._sendCmd("BoardID serial")
        return res
    
def AOTF_enable(my_aotf):
    if not my_aotf.getStatus():
        exit()
    else:
        cmd = "dau en"
        res = my_aotf._sendCmd(cmd)
    return cmd + " | " + res

def AOTF_disable(my_aotf):
    if not my_aotf.getStatus():
        exit()
    else:
        cmd = "dau dis"
        res = my_aotf._sendCmd(cmd)
    return cmd + " | " + res

def AOTF_setPower(my_aotf, channel, power):
    if not my_aotf.getStatus():
        exit()
    else:
        cmd = "dds a " + str(channel) + " " + str(power)
        res = my_aotf._sendCmd(cmd)
    return cmd + " | " + res

def AOTF_setFrequency(my_aotf, channel, frequency):
    if not my_aotf.getStatus():
        exit()
    else:
        cmd = "dds f " + str(channel) + " " + str(frequency)
        res = my_aotf._sendCmd(cmd)
    return cmd + " | " + res

def AOTF_setPowerRed(my_aotf, power):
    if not my_aotf.getStatus():exit()
    else:
        cmd = "dds f " + str(7) + " " + str(96.20)
        res = my_aotf._sendCmd(cmd)
        cmd = "dds a " + str(7) + " " + str(power)
        res = my_aotf._sendCmd(cmd)
    return cmd + " | " + res

def AOTF_setPowerGreen(my_aotf, power):
    if not my_aotf.getStatus():exit()
    else:
        cmd = "dds f " + str(6) + " " + str(114.86)
        res = my_aotf._sendCmd(cmd)
        cmd = "dds a " + str(6) + " " + str(power)
        res = my_aotf._sendCmd(cmd)
    return cmd + " | " + res

def AOTF_setPowerBlue(my_aotf, power):
    if not my_aotf.getStatus():exit()
    else:
        cmd = "dds f " + str(5) + " " + str(137.52)
        res = my_aotf._sendCmd(cmd)
        cmd = "dds a " + str(5) + " " + str(power)
        res = my_aotf._sendCmd(cmd)
    return cmd + " | " + res

def AOTF_setOFF(my_aotf, channel):
    if not my_aotf.getStatus():
        exit()
    else:
        cmd = "dds a "+ str(channel) +" 0"
        res = my_aotf._sendCmd(cmd)
    return cmd + " | " + res

def AOTF_setAllOFF(my_aotf,power=0):
    if not my_aotf.getStatus():
        exit()
    else:
        return_res = ""
        for channel in range(8):
            cmd = "dds a "+ str(channel) +" 0"
            res = my_aotf._sendCmd(cmd)
            return_res = return_res + cmd + " | " + res + ""
        return_res = "dds a ALL 0 | dds a ALL 0\n"
    return return_res

def AOTF_setON(my_aotf, channel,freq, power):
    if not my_aotf.getStatus():
        exit()
    else:
        cmd1 = "dds f "+ str(channel) +" "+ str(freq)
        cmd2 = "dds a "+ str(channel) +" "+ str(power)
        res = my_aotf._sendCmd(cmd1)
        return_res = cmd1 + " | " + res
        res = my_aotf._sendCmd(cmd2)
    return return_res + "\n"+ cmd2 + " | " + res

def AOTF_shutdown(my_aotf):
    # my_aotf.shutDown()
    if not my_aotf.getStatus():
        exit()
    else:
        # my_aotf._sendCmd("shutdown")
        my_aotf.aotf_conn.close()
        my_aotf.aotf_proc.terminate()
        pass
    return "res: Closed"


if __name__=="__main__":
    from time import sleep
    my_aotf = AOTF_init()
    print(AOTF_boardID(my_aotf))
    print(AOTF_enable(my_aotf))
    # print(AOTF_setFrequency(my_aotf, 7, 96.2))
    # print(AOTF_setPower(my_aotf, 7, 9820))
    print(AOTF_setPowerRed(my_aotf,9820))
    sleep(5)
    # print(AOTF_setPower(my_aotf, 7, 0))
    # print(AOTF_disable(my_aotf))
    print(AOTF_setPowerRed(my_aotf,0))
    print(AOTF_disable(my_aotf))
    print(AOTF_shutdown(my_aotf))

