## ------------------------------------------
## Generated by Transwarp
##
## THIS FILE IS AUTOMATICALLY GENERATED.
## DO NOT EDIT. ALL CHANGES WILL BE LOST.
## ------------------------------------------

import enum
from dataclasses import dataclass
import json
from .amtypes import *
from .megajank import mqtt_checksum_add, mqtt_checksum_remove, mqtt_aes_encrypt, mqtt_aes_decrypt

class MqttPktType(enum.IntEnum):
    Single      = 0xc0 # Whole message in a single packet. No further packets in this stream
    MultiBegin  = 0xc1 # Reallocate buffer memory, *then* append to message. Unless this is used
    MultiAppend = 0xc2 # Append to existing message buffer.
    MultiFinish = 0xc3 # Append data, then handle complete message.

    @classmethod
    def parse(cls, p):
        return cls(struct.unpack("B", p[:1])[0]), p[1:]

    def pack(self):
        return struct.pack("B", self)

class MqttMsgType(enum.IntEnum):
    ZZ_MQTT_CMD_EVENT_NOTIFY           = 0x03e8 # 
    ZZ_MQTT_CMD_PRINT_SCHEDULE         = 0x03e9 # 
    ZZ_MQTT_CMD_FIRMWARE_VERSION       = 0x03ea # Returns firmware version string
    ZZ_MQTT_CMD_NOZZLE_TEMP            = 0x03eb # Set nozzle temperature in units of 1/100th deg C (i.e.31337 is 313.37C)
    ZZ_MQTT_CMD_HOTBED_TEMP            = 0x03ec # Set hotbed temperature in units of 1/100th deg C (i.e. 1337 is 13.37C)
    ZZ_MQTT_CMD_FAN_SPEED              = 0x03ed # Set fan speed
    ZZ_MQTT_CMD_PRINT_SPEED            = 0x03ee # ? Set print speed
    ZZ_MQTT_CMD_AUTO_LEVELING          = 0x03ef # (probably) Perform auto-levelling procedure
    ZZ_MQTT_CMD_PRINT_CONTROL          = 0x03f0 # 
    ZZ_MQTT_CMD_FILE_LIST_REQUEST      = 0x03f1 # Request on-board file list (value == 1) or usb file list (value != 1)
    ZZ_MQTT_CMD_GCODE_FILE_REQUEST     = 0x03f2 # 
    ZZ_MQTT_CMD_ALLOW_FIRMWARE_UPDATE  = 0x03f3 # 
    ZZ_MQTT_CMD_GCODE_FILE_DOWNLOAD    = 0x03fc # 
    ZZ_MQTT_CMD_Z_AXIS_RECOUP          = 0x03fd # ?
    ZZ_MQTT_CMD_EXTRUSION_STEP         = 0x03fe # (probably) run the extrusion stepper
    ZZ_MQTT_CMD_ENTER_OR_QUIT_MATERIEL = 0x03ff # maybe related to filament change?
    ZZ_MQTT_CMD_MOVE_STEP              = 0x0400 # 
    ZZ_MQTT_CMD_MOVE_DIRECTION         = 0x0401 # 
    ZZ_MQTT_CMD_MOVE_ZERO              = 0x0402 # (probably) Move to home position
    ZZ_MQTT_CMD_APP_QUERY_STATUS       = 0x0403 # 
    ZZ_MQTT_CMD_ONLINE_NOTIFY          = 0x0404 # 
    ZZ_MQTT_CMD_RECOVER_FACTORY        = 0x0405 # Factory reset printer
    ZZ_MQTT_CMD_BLE_ONOFF              = 0x0407 # (probably) Enable/disable Bluetooth Low Energy ("ble") radio
    ZZ_MQTT_CMD_DELETE_GCODE_FILE      = 0x0408 # (probably) Delete specified gcode file
    ZZ_MQTT_CMD_RESET_GCODE_PARAM      = 0x0409 # ?
    ZZ_MQTT_CMD_DEVICE_NAME_SET        = 0x040a # 
    ZZ_MQTT_CMD_DEVICE_LOG_UPLOAD      = 0x040b # 
    ZZ_MQTT_CMD_ONOFF_MODAL            = 0x040c # ?
    ZZ_MQTT_CMD_MOTOR_LOCK             = 0x040d # ?
    ZZ_MQTT_CMD_PREHEAT_CONFIG         = 0x040e # ?
    ZZ_MQTT_CMD_BREAK_POINT            = 0x040f # 
    ZZ_MQTT_CMD_AI_CALIB               = 0x0410 # 
    ZZ_MQTT_CMD_VIDEO_ONOFF            = 0x0411 # ?
    ZZ_MQTT_CMD_ADVANCED_PARAMETERS    = 0x0412 # ?
    ZZ_MQTT_CMD_GCODE_COMMAND          = 0x0413 # Run custom GCode command
    ZZ_MQTT_CMD_PREVIEW_IMAGE_URL      = 0x0414 # 
    ZZ_MQTT_CMD_SYSTEM_CHECK           = 0x0419 # ?
    ZZ_MQTT_CMD_AI_SWITCH              = 0x041a # ?
    ZZ_MQTT_CMD_AI_INFO_CHECK          = 0x041b # ?
    ZZ_MQTT_CMD_MODEL_LAYER            = 0x041c # ?
    ZZ_MQTT_CMD_MODEL_DL_PROCESS       = 0x041d # ?
    ZZ_MQTT_CMD_PRINT_MAX_SPEED        = 0x041f # ?
    ZZ_MQTT_CMD_ALEXA_MSG              = 0x0bb8 # 

    @classmethod
    def parse(cls, p):
        return cls(struct.unpack("B", p[:1])[0]), p[1:]

    def pack(self):
        return struct.pack("B", self)

class MqttPrintEvent(enum.IntEnum):
    ZZ_MQTT_PRINT_EVENT_IDLE          = 0x00 # 
    ZZ_MQTT_PRINT_EVENT_PRINTING      = 0x01 # 
    ZZ_MQTT_PRINT_EVENT_PAUSED        = 0x02 # 
    ZZ_MQTT_PRINT_EVENT_STOPPED       = 0x03 # 
    ZZ_MQTT_PRINT_EVENT_COMPLETED     = 0x04 # 
    ZZ_MQTT_PRINT_EVENT_LEVELING      = 0x05 # 
    ZZ_MQTT_PRINT_EVENT_DOWNLOADING   = 0x06 # 
    ZZ_MQTT_PRINT_EVENT_LEVEL_HEATING = 0x07 # 
    ZZ_MQTT_PRINT_EVENT_HEATING       = 0x08 # 
    ZZ_MQTT_PRINT_EVENT_PREHEAT       = 0x09 # 
    ZZ_MQTT_PRINT_EVENT_PRINT_DL      = 0x0a # 
    ZZ_MQTT_PRINT_EVENT_MAX           = 0x0b # 

    @classmethod
    def parse(cls, p):
        return cls(struct.unpack("B", p[:1])[0]), p[1:]

    def pack(self):
        return struct.pack("B", self)

class MqttMarlinEvent(enum.IntEnum):
    ZZ_MQTT_MARLIN_ALERT_HALTED      = 0x01 # 
    ZZ_MQTT_MARLIN_ALERT_OFFLINE     = 0x02 # 
    ZZ_MQTT_MARLIN_ALERT_NOZZEL_HEAT = 0x03 # 
    ZZ_MQTT_MARLIN_ALERT_PANEL_HEAT  = 0x04 # 
    ZZ_MQTT_MARLIN_ALERT_PRINT       = 0x05 # 
    ZZ_MQTT_MARLIN_ALERT_BLANKING    = 0x06 # 
    ZZ_MQTT_MARLIN_ALERT_BLOCKING    = 0x07 # 
    ZZ_MQTT_MARLIN_ALERT_LEVELING    = 0x08 # 
    ZZ_MQTT_MARLIN_COMM_ERR          = 0x09 # 
    ZZ_MQTT_LBOARD_COMM_ERR          = 0x0a # 
    ZZ_MQTT_NOZZLE_HIGH_TEMP         = 0x0b # 
    ZZ_MQTT_HEATBED_HIGH_TEMP        = 0x0c # 
    ZZ_MQTT_HEATBED_MOS1             = 0x0d # 
    ZZ_MQTT_LEVEL_FAILED             = 0x0e # 
    ZZ_MQTT_HEATBED_MOS2             = 0x0f # 
    ZZ_MQTT_NOZZLE_LOW_TEMP          = 0x10 # 
    ZZ_MQTT_MARLIN_AUTO_PAUSE        = 0x11 # 
    ZZ_MQTT_PRINT_DL_FAILED          = 0x12 # 
    ZZ_MQTT_MARLIN_ALERT_MAX         = 0x13 # 

    @classmethod
    def parse(cls, p):
        return cls(struct.unpack("B", p[:1])[0]), p[1:]

    def pack(self):
        return struct.pack("B", self)

@dataclass
class _MqttMsg:
    signature  : bytes = field(repr=False, kw_only=True, default=b'MA') # Signature: 'MA'
    size       : u16le # length of packet, including header and checksum (minimum 65).
    m3         : u8 # Magic constant: 5
    m4         : u8 # Magic constant: 1
    m5         : u8 # Magic constant: 2
    m6         : u8 # Magic constant: 5
    m7         : u8 # Magic constant: 'F'
    packet_type: MqttPktType # Packet type
    packet_num : u16le # maybe for fragmented messages?set to 1 for unfragmented messages.
    time       : u32le # `gettimeofday()` in whole seconds
    device_guid: bytes # device guid, as hex string
    padding    : bytes = field(repr=False, kw_only=True, default='\x00' * 11) # padding bytes, allways zero
    data       : bytes # payload data

    @classmethod
    def parse(cls, p):
        signature, p = Magic.parse(p, 2, b'MA')
        size, p = u16le.parse(p)
        m3, p = u8.parse(p)
        m4, p = u8.parse(p)
        m5, p = u8.parse(p)
        m6, p = u8.parse(p)
        m7, p = u8.parse(p)
        packet_type, p = MqttPktType.parse(p)
        packet_num, p = u16le.parse(p)
        time, p = u32le.parse(p)
        device_guid, p = String.parse(p, 37)
        padding, p = Zeroes.parse(p, 11)
        data, p = Tail.parse(p)
        return cls(signature=signature, size=size, m3=m3, m4=m4, m5=m5, m6=m6, m7=m7, packet_type=packet_type, packet_num=packet_num, time=time, device_guid=device_guid, padding=padding, data=data), p

    def pack(self):
        p  = Magic.pack(self.signature, 2, b'MA')
        p += u16le.pack(self.size)
        p += u8.pack(self.m3)
        p += u8.pack(self.m4)
        p += u8.pack(self.m5)
        p += u8.pack(self.m6)
        p += u8.pack(self.m7)
        p += MqttPktType.pack(self.packet_type)
        p += u16le.pack(self.packet_num)
        p += u32le.pack(self.time)
        p += String.pack(self.device_guid, 37)
        p += Zeroes.pack(self.padding, 11)
        p += Tail.pack(self.data)
        return p


class MqttMsg(_MqttMsg):

    @classmethod
    def parse(cls, p, key):
        p = mqtt_checksum_remove(p)
        if p[6] != 2:
            raise ValueError(f"Unsupported mqtt message format (expected 2, but found {p[6]})")
        body, data = p[:64], mqtt_aes_decrypt(p[64:], key)
        res = super().parse(body + data)
        assert res[0].size == (len(p) + 1)
        return res

    def pack(self, key):
        data = mqtt_aes_encrypt(self.data, key)
        self.size = 64 + len(data) + 1
        body = super().pack()[:64]
        final = mqtt_checksum_add(body + data)
        return final

    def getjson(self):
        return json.loads(self.data.decode())

    def setjson(self, val):
        self.data = json.dumps(val).encode()
