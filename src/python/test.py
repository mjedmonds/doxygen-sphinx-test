class SimpleBleDevice():
    """This is a conceptual class representation of a simple BLE device (GATT Server). It is essentially an extended combination of the :class:`bluepy.btle.Peripheral` and :class:`bluepy.btle.ScanEntry` classes

    :param client: A handle to the :class:`simpleble.SimpleBleClient` client object that detected the device
    :type client: class:`simpleble.SimpleBleClient`
    :param addr: Device MAC address, defaults to None
    :type addr: str, optional
    :param addrType: Device address type - one of ADDR_TYPE_PUBLIC or ADDR_TYPE_RANDOM, defaults to ADDR_TYPE_PUBLIC
    :type addrType: str, optional
    :param iface: Bluetooth interface number (0 = /dev/hci0) used for the connection, defaults to 0
    :type iface: int, optional
    :param data: A list of tuples (adtype, description, value) containing the AD type code, human-readable description and value for all available advertising data items, defaults to None
    :type data: list, optional
    :param rssi: Received Signal Strength Indication for the last received broadcast from the device. This is an integer value measured in dB, where 0 dB is the maximum (theoretical) signal strength, and more negative numbers indicate a weaker signal, defaults to 0
    :type rssi: int, optional
    :param connectable: `True` if the device supports connections, and `False` otherwise (typically used for advertising ‘beacons’)., defaults to `False`
    :type connectable: bool, optional
    :param updateCount: Integer count of the number of advertising packets received from the device so far, defaults to 0
    :type updateCount: int, optional
    """

    def __init__(self, client, addr=None, addrType=0, iface=0, data=None, rssi=0, connectable=False, updateCount=0):
        """Constructor method
        """
        self.addr = addr
        self.addrType = addrType
        self.iface = iface
        self.rssi = rssi
        self.connectable = connectable
        self.updateCount = updateCount
        self.data = data
        self._connected = False
        self._services = []
        self._characteristics = []
        self._client = client

    def getServices(self, uuids=None):
        """Returns a list of :class:`bluepy.blte.Service` objects representing the services offered by the device. This will perform Bluetooth service discovery if this has not already been done; otherwise it will return a cached list of services immediately..

        :param uuids: A list of string service UUIDs to be discovered, defaults to None
        :type uuids: list, optional
        :return: A list of the discovered :class:`bluepy.blte.Service` objects, which match the provided ``uuids``
        :rtype: list On Python 3.x, this returns a dictionary view object, not a list
        """
        return []

    def setNotificationCallback(self, callback):
        """
        Set
        :param callback: A function handle of the form ``callback(client, characteristic, data)``, where ``client`` is a handle to the :class:`simpleble.SimpleBleClient` that invoked the callback, ``characteristic`` is the notified :class:`bluepy.blte.Characteristic` object and data is a `bytearray` containing the updated value. Defaults to None
        :type callback: function, optional
        """
        pass

    def getCharacteristics(self, startHnd=1, endHnd=0xFFFF, uuids=None):
        """
        Ret
        :param startHnd: Start index, defaults to 1
        :type startHnd: int, optional
        :param endHnd: End index, defaults to 0xFFFF
        :type endHnd: int, optional
        :param uuids: a list of UUID strings, defaults to None
        :type uuids: list, optional
        :return: List of returned :class:`bluepy.btle.Characteristic` objects
        :rtype: list
        """
        return []

    def connect(self):
        """
        Att
        :return: `True` if connection was successful, `False` otherwise
        :rtype: bool
        """
        return True

    def disconnect(self):
        """
        Dro"""
        super().disconnect()
        self._connected = False

    def isConnected(self):
        """
        Che
        :return: `True` if connected, `False` otherwise
        :rtype: bool
        """
        return self._connected

    def printInfo(self):
        """
        Print
        """
        print("Device %s (%s), RSSI=%d dB" %
            (self.addr, self.addrType, self.rssi))
        for (adtype, desc, value) in self.data:
            print("  %s = %s" % (desc, value))