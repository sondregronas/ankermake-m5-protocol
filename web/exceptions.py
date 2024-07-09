class AnkerBaseException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        log.debug(msg)


# Currently not used anywhere
class AnkerPrinterOffline(AnkerBaseException):
    # To be raised when the printer is offline
    # (vs AnkerConnectionLost which is for when we lose connection to the printer)
    pass


class AnkerCriticalError(AnkerBaseException):
    def __init__(self, msg):
        super().__init__(msg)
        log.critical(msg)


class AnkerConnectionLost(AnkerCriticalError):
    # TODO: This might be a bad name for this exception, its not meant for "printer lost network connection"
    #       but rather for "we lost connection to the presumed _online_ printer" (hence the "critical" part)
    #       If the printer is offline this should be a different exception
    pass
