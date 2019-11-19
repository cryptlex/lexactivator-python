import ctypes
from cryptlex.lexactivator import lexactivator_native as LexActivatorNative
from cryptlex.lexactivator.lexstatus_codes import LexStatusCodes
from cryptlex.lexactivator.lexactivator_exception import LexActivatorException

callback_list = []


class PermissionFlags:
    LA_USER = 1
    LA_SYSTEM = 2
    LA_IN_MEMORY = 4


class LicenseMeterAttribute(object):
    def __init__(self, name, allowed_uses, total_uses):
        self.name = name
        self.allowed_uses = allowed_uses
        self.total_uses = total_uses


class LexActivator:
    @staticmethod
    def SetProductFile(file_path):
        """Sets the absolute path of the Product.dat file.

        This function must be called on every start of your program before any other
        functions are called.

        Args:
                file_path (str): absolute path of the product file (Product.dat)

        Raises:
                LexActivatorException
        """
        cstring = LexActivatorNative.get_ctype_string(file_path)
        status = LexActivatorNative.SetProductFile(cstring)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def SetProductData(product_data):
        """Embeds the Product.dat file in the application.

        It can be used instead of SetProductFile() in case you want to embed the
        Product.dat file in your application.

        This function must be called on every start of your program before any other
        functions are called.

        Args:
                product_data (str): content of the Product.dat file

        Raises:
                LexActivatorException
        """
        cstring_product_data = LexActivatorNative.get_ctype_string(
            product_data)
        status = LexActivatorNative.SetProductData(cstring_product_data)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def SetProductId(product_id, flags):
        """Sets the product id of your application.

        This function must be called on every start of your program before any other
        functions are called, with the exception of SetProductFile() or
        SetProductData() function.

        Args:
                product_id (str): the unique product id of your application as mentioned on the product page in the dashboard
                flags (str): depending upon whether your application requires admin/root permissions to run or not, this parameter can have one of the following values: LA_SYSTEM, LA_USER, LA_IN_MEMORY

        Raises:
                LexActivatorException
        """
        cstring_product_id = LexActivatorNative.get_ctype_string(product_id)
        status = LexActivatorNative.SetProductId(cstring_product_id, flags)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def SetLicenseKey(license_key):
        """Sets the license key required to activate the license.

        Args:
                license_key (str): a valid license key

        Raises:
                LexActivatorException
        """
        cstring_license_key = LexActivatorNative.get_ctype_string(license_key)
        status = LexActivatorNative.SetLicenseKey(cstring_license_key)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def SetLicenseUserCredential(email, password):
        """Sets the license user email and password for authentication.

        This function must be called before ActivateLicense() or IsLicenseGenuine()
        function if requireAuthentication property of the license is set to true.

        Args:
                email (str): user email address
                password (str): user password

        Raises:
                LexActivatorException
        """
        cstring_email = LexActivatorNative.get_ctype_string(email)
        cstring_password = LexActivatorNative.get_ctype_string(password)

        status = LexActivatorNative.SetLicenseUserCredential(
            cstring_email, cstring_password)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def SetLicenseCallback(license_callback):
        """Sets server sync callback function.

        Whenever the server sync occurs in a separate thread, and server returns the
        response, event listener function gets invoked with the following status
        codes: LA_OK, LA_EXPIRED, LA_SUSPENDED, LA_E_REVOKED,
        LA_E_ACTIVATION_NOT_FOUND, LA_E_MACHINE_FINGERPRINT LA_E_COUNTRY, LA_E_INET,
        LA_E_SERVER, LA_E_RATE_LIMIT, LA_E_IP

        Args:
                license_callback (Callable[int]]): callback function

        Raises:
                LexActivatorException
        """
        license_callback_fn = LexActivatorNative.CallbackType(license_callback)
        callback_list.append(license_callback_fn)
        status = LexActivatorNative.SetLicenseCallback(license_callback_fn)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def SetActivationMetadata(key, value):
        """Sets the activation metadata.

        The metadata appears along with the activation details of the license in
        dashboard.

        Args:
                key (str): string of maximum length 256 characters with utf-8 encoding
                value (str): string of maximum length 256 characters with utf-8 encoding

        Raises:
                LexActivatorException
        """
        cstring_key = LexActivatorNative.get_ctype_string(key)
        cstring_value = LexActivatorNative.get_ctype_string(value)
        status = LexActivatorNative.SetActivationMetadata(
            cstring_key, cstring_value)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def SetTrialActivationMetadata(key, value):
        """Sets the trial activation metadata.

        The metadata appears along with the trial activation details of the product
        in dashboard.

        Args:
                key (str): string of maximum length 256 characters with utf-8 encoding
                value (str): string of maximum length 256 characters with utf-8 encoding

        Raises:
                LexActivatorException
        """
        cstring_key = LexActivatorNative.get_ctype_string(key)
        cstring_value = LexActivatorNative.get_ctype_string(value)
        status = LexActivatorNative.SetTrialActivationMetadata(
            cstring_key, cstring_value)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def SetAppVersion(app_version):
        """Sets the current app version of your application.

        The app version appears along with the activation details in dashboard. It is
        also used to generate app analytics.

        Args:
                app_version (str): string of maximum length 256 characters with utf-8 encoding.

        Raises:
                LexActivatorException
        """
        cstring_app_version = LexActivatorNative.get_ctype_string(app_version)

        status = LexActivatorNative.SetAppVersion(cstring_app_version)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def SetOfflineActivationRequestMeterAttributeUses(name, uses):
        """Sets the meter attribute uses for the offline activation request.

        This function should only be called before GenerateOfflineActivationRequest()
        function to set the meter attributes in case of offline activation.

        Args:
                name (str): name of the meter attribute
                uses (int): the uses value

        Raises:
                LexActivatorException
        """
        cstring_name = LexActivatorNative.get_ctype_string(name)
        status = LexActivatorNative.SetOfflineActivationRequestMeterAttributeUses(
            cstring_name, uses)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def SetNetworkProxy(proxy):
        """Sets the network proxy to be used when contacting CryptLex servers.

        The proxy format should be: [protocol://][username:password@]machine[:port]

        Note: 
                Proxy settings of the computer are automatically detected. So,
                in most of the cases you don't need to care whether your user is behind a
                proxy server or not.

        Args:
                proxy (str): proxy having correct proxy format

        Raises:
                LexActivatorException
        """
        cstring_proxy = LexActivatorNative.get_ctype_string(proxy)

        status = LexActivatorNative.SetNetworkProxy(cstring_proxy)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def SetCryptlexHost(host):
        """In case you are running Cryptlex on-premise, you can set the host for your
        on-premise server.

        Args:
                host (str): the address of the Cryptlex on-premise server

        Raises:
                LexActivatorException
        """
        cstring_host = LexActivatorNative.get_ctype_string(host)
        status = LexActivatorNative.SetCryptlexHost(cstring_host)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def GetProductMetadata(key):
        """Gets the product metadata as set in the dashboard.

        Args:
                key (str): metadata key to retrieve the value

        Raises:
                LexActivatorException

        Returns:
                str: value of metadata for the key
        """
        cstring_key = LexActivatorNative.get_ctype_string(key)
        buffer_size = 256
        buffer = LexActivatorNative.get_ctype_string_buffer(buffer_size)
        status = LexActivatorNative.GetProductMetadata(
            cstring_key, buffer, buffer_size)
        if status != LexStatusCodes.LA_OK:
            raise LexActivatorException(status)
        return LexActivatorNative.byte_to_string(buffer.value)

    @staticmethod
    def GetLicenseMetadata(key):
        """Gets the license metadata as set in the dashboard.

        Args:
                key (str): metadata key to retrieve the value

        Raises:
                LexActivatorException

        Returns:
                str: value of metadata for the key
        """
        cstring_key = LexActivatorNative.get_ctype_string(key)
        buffer_size = 256
        buffer = LexActivatorNative.get_ctype_string_buffer(buffer_size)
        status = LexActivatorNative.GetLicenseMetadata(
            cstring_key, buffer, buffer_size)
        if status != LexStatusCodes.LA_OK:
            raise LexActivatorException(status)
        return LexActivatorNative.byte_to_string(buffer.value)

    @staticmethod
    def GetLicenseMeterAttribute(name):
        """Gets the license meter attribute allowed uses and total uses.

        Args:
                name (str): name of the meter attribute

        Raises:
                LexActivatorException

        Returns:
                LicenseMeterAttribute: values of meter attribute allowed and total uses
        """
        cstring_name = LexActivatorNative.get_ctype_string(name)
        allowed_uses = ctypes.c_uint()
        total_uses = ctypes.c_uint()
        status = LexActivatorNative.GetLicenseMeterAttribute(
            cstring_name, ctypes.byref(allowed_uses), ctypes.byref(total_uses))
        if status == LexStatusCodes.LA_OK:
            return LicenseMeterAttribute(name, allowed_uses.value, total_uses.value)
        else:
            raise LexActivatorException(status)

    @staticmethod
    def GetLicenseKey():
        """Gets the license key used for activation.

        Raises:
                LexActivatorException

        Returns:
                str: the license key
        """
        buffer_size = 256
        buffer = LexActivatorNative.get_ctype_string_buffer(buffer_size)
        status = LexActivatorNative.GetLicenseKey(buffer, buffer_size)
        if status != LexStatusCodes.LA_OK:
            raise LexActivatorException(status)
        return LexActivatorNative.byte_to_string(buffer.value)

    @staticmethod
    def GetLicenseExpiryDate():
        """Gets the license expiry date timestamp.

        Raises:
                LexActivatorException

        Returns:
                int: the timestamp
        """
        expiry_date = ctypes.c_uint()
        status = LexActivatorNative.GetLicenseExpiryDate(
            ctypes.byref(expiry_date))
        if status == LexStatusCodes.LA_OK:
            return expiry_date.value
        elif status == LexStatusCodes.LA_FAIL:
            return 0
        else:
            raise LexActivatorException(status)

    @staticmethod
    def GetLicenseUserEmail():
        """Gets the email associated with license user.

        Raises:
                LexActivatorException

        Returns:
                str: the license user email
        """
        buffer_size = 256
        buffer = LexActivatorNative.get_ctype_string_buffer(buffer_size)
        status = LexActivatorNative.GetLicenseUserEmail(buffer, buffer_size)
        if status != LexStatusCodes.LA_OK:
            raise LexActivatorException(status)
        return LexActivatorNative.byte_to_string(buffer.value)

    @staticmethod
    def GetLicenseUserName():
        """Gets the name associated with the license user.

        Raises:
                LexActivatorException

        Returns:
                str: the license user name
        """
        buffer_size = 256
        buffer = LexActivatorNative.get_ctype_string_buffer(buffer_size)
        status = LexActivatorNative.GetLicenseUserName(buffer, buffer_size)
        if status != LexStatusCodes.LA_OK:
            raise LexActivatorException(status)
        return LexActivatorNative.byte_to_string(buffer.value)

    @staticmethod
    def GetLicenseUserCompany():
        """Gets the company associated with the license user.

        Raises:
                LexActivatorException

        Returns:
                str: the license user company
        """
        buffer_size = 256
        buffer = LexActivatorNative.get_ctype_string_buffer(buffer_size)
        status = LexActivatorNative.GetLicenseUserCompany(buffer, buffer_size)
        if status != LexStatusCodes.LA_OK:
            raise LexActivatorException(status)
        return LexActivatorNative.byte_to_string(buffer.value)

    @staticmethod
    def GetLicenseUserMetadata(key):
        """Gets the metadata associated with the license user.

        Args:
                key (str): metadata key to retrieve the value

        Raises:
                LexActivatorException

        Returns:
                str: value of metadata for the key
        """
        cstring_key = LexActivatorNative.get_ctype_string(key)
        buffer_size = 256
        buffer = LexActivatorNative.get_ctype_string_buffer(buffer_size)
        status = LexActivatorNative.GetLicenseUserMetadata(
            cstring_key, buffer, buffer_size)
        if status != LexStatusCodes.LA_OK:
            raise LexActivatorException(status)
        return LexActivatorNative.byte_to_string(buffer.value)

    @staticmethod
    def GetLicenseType():
        """Gets the license type.

        Raises:
                LexActivatorException

        Returns:
                str: the license type - node-locked or hosted-floating
        """
        buffer_size = 256
        buffer = LexActivatorNative.get_ctype_string_buffer(buffer_size)
        status = LexActivatorNative.GetLicenseType(buffer, buffer_size)
        if status != LexStatusCodes.LA_OK:
            raise LexActivatorException(status)
        return LexActivatorNative.byte_to_string(buffer.value)

    @staticmethod
    def GetActivationMetadata(key):
        """Gets the activation metadata.

        Args:
                key (str): metadata key to retrieve the value

        Raises:
                LexActivatorException

        Returns:
                str: value of metadata for the key
        """
        cstring_key = LexActivatorNative.get_ctype_string(key)
        buffer_size = 256
        buffer = LexActivatorNative.get_ctype_string_buffer(buffer_size)
        status = LexActivatorNative.GetActivationMetadata(
            cstring_key, buffer, buffer_size)
        if status != LexStatusCodes.LA_OK:
            raise LexActivatorException(status)
        return LexActivatorNative.byte_to_string(buffer.value)

    @staticmethod
    def GetActivationMeterAttributeUses(name):
        """Gets the meter attribute uses consumed by the activation.

        Args:
                name (str): name of the meter attribute

        Raises:
                LexActivatorException

        Returns:
                int: value of meter attribute uses by the activation
        """
        cstring_name = LexActivatorNative.get_ctype_string(name)
        uses = ctypes.c_uint()
        status = LexActivatorNative.GetActivationMeterAttributeUses(
            cstring_name, ctypes.byref(uses))
        if status == LexStatusCodes.LA_OK:
            return uses.value
        else:
            raise LexActivatorException(status)

    @staticmethod
    def GetServerSyncGracePeriodExpiryDate():
        """Gets the server sync grace period expiry date timestamp.

        Raises:
                LexActivatorException

        Returns:
                int: the timestamp
        """
        expiry_date = ctypes.c_uint()
        status = LexActivatorNative.GetServerSyncGracePeriodExpiryDate(
            ctypes.byref(expiry_date))
        if status == LexStatusCodes.LA_OK:
            return expiry_date.value
        elif status == LexStatusCodes.LA_FAIL:
            return 0
        else:
            raise LexActivatorException(status)

    @staticmethod
    def GetTrialActivationMetadata(key):
        """Gets the trial activation metadata.

        Args:
                key (str): metadata key to retrieve the value

        Raises:
                LexActivatorException

        Returns:
                str: value of metadata for the key
        """
        cstring_key = LexActivatorNative.get_ctype_string(key)
        buffer_size = 256
        buffer = LexActivatorNative.get_ctype_string_buffer(buffer_size)
        status = LexActivatorNative.GetTrialActivationMetadata(
            cstring_key, buffer, buffer_size)
        if status != LexStatusCodes.LA_OK:
            raise LexActivatorException(status)
        return LexActivatorNative.byte_to_string(buffer.value)

    @staticmethod
    def GetTrialExpiryDate():
        """Gets the trial expiry date timestamp.

        Raises:
                LexActivatorException

        Returns:
                int: the timestamp
        """
        expiry_date = ctypes.c_uint()
        status = LexActivatorNative.GetTrialExpiryDate(
            ctypes.byref(expiry_date))
        if status == LexStatusCodes.LA_OK:
            return expiry_date.value
        elif status == LexStatusCodes.LA_FAIL:
            return 0
        else:
            raise LexActivatorException(status)

    @staticmethod
    def GetTrialId():
        """Gets the trial activation id. Used in case of trial extension.

        Raises:
                LexActivatorException

        Returns:
                str: the trial id
        """
        buffer_size = 256
        buffer = LexActivatorNative.get_ctype_string_buffer(buffer_size)
        status = LexActivatorNative.GetTrialId(buffer, buffer_size)
        if status != LexStatusCodes.LA_OK:
            raise LexActivatorException(status)
        return LexActivatorNative.byte_to_string(buffer.value)

    @staticmethod
    def GetLocalTrialExpiryDate():
        """Gets the local trial expiry date timestamp.

        Raises:
                LexActivatorException

        Returns:
                int: the timestamp
        """
        expiry_date = ctypes.c_uint()
        status = LexActivatorNative.GetLocalTrialExpiryDate(
            ctypes.byref(expiry_date))
        if status == LexStatusCodes.LA_OK:
            return expiry_date.value
        elif status == LexStatusCodes.LA_FAIL:
            return 0
        else:
            raise LexActivatorException(status)

    @staticmethod
    def CheckForReleaseUpdate(platform, version, channel, release_callback):
        """Checks whether a new release is available for the product.

        This function should only be used if you manage your releases through
        Cryptlex release management API.

        Args:
                platform (str): release platform e.g. windows, macos, linux
                version (str): current release version
                channel (str): release channel e.g. stable
                release_callback (Callable[int]]): callback function

        Raises:
                LexActivatorException
        """
        cstring_platform = LexActivatorNative.get_ctype_string(platform)
        cstring_version = LexActivatorNative.get_ctype_string(version)
        cstring_channel = LexActivatorNative.get_ctype_string(channel)

        release_callback_fn = LexActivatorNative.CallbackType(release_callback)
        callback_list.append(release_callback_fn)
        status = LexActivatorNative.CheckForReleaseUpdate(
            cstring_platform, cstring_version, cstring_channel, release_callback_fn)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def ActivateLicense():
        """Activates the license by contacting the Cryptlex servers. It validates the
        key and returns with encrypted and digitally signed token which it stores and
        uses to activate your application.

        This function should be executed at the time of registration, ideally on a
        button click.

        Raises:
                LexActivatorException

        Returns:
                int: LA_OK, LA_EXPIRED, LA_SUSPENDED, LA_FAIL
        """
        status = LexActivatorNative.ActivateLicense()
        if LexStatusCodes.LA_OK == status:
            return LexStatusCodes.LA_OK
        elif LexStatusCodes.LA_EXPIRED == status:
            return LexStatusCodes.LA_EXPIRED
        elif LexStatusCodes.LA_SUSPENDED == status:
            return LexStatusCodes.LA_SUSPENDED
        elif LexStatusCodes.LA_FAIL == status:
            return LexStatusCodes.LA_FAIL
        else:
            raise LexActivatorException(status)

    @staticmethod
    def ActivateLicenseOffline(file_path):
        """Activates the license using the offline activation response file.

        Args:
                file_path (str): path of the offline activation response file.

        Raises:
                LexActivatorException

        Returns:
                int: LA_OK, LA_EXPIRED, LA_SUSPENDED, LA_FAIL
        """
        cstring_file_path = LexActivatorNative.get_ctype_string(file_path)
        status = LexActivatorNative.ActivateLicenseOffline(cstring_file_path)
        if LexStatusCodes.LA_OK == status:
            return LexStatusCodes.LA_OK
        elif LexStatusCodes.LA_EXPIRED == status:
            return LexStatusCodes.LA_EXPIRED
        elif LexStatusCodes.LA_SUSPENDED == status:
            return LexStatusCodes.LA_SUSPENDED
        elif LexStatusCodes.LA_FAIL == status:
            return LexStatusCodes.LA_FAIL
        else:
            raise LexActivatorException(status)

    @staticmethod
    def GenerateOfflineActivationRequest(file_path):
        """Generates the offline activation request needed for generating offline
        activation response in the dashboard.

        Args:
                file_path (str): path of the file for the offline request.

        Raises:
                LexActivatorException
        """
        cstring_file_path = LexActivatorNative.get_ctype_string(file_path)
        status = LexActivatorNative.GenerateOfflineActivationRequest(
            cstring_file_path)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def DeactivateLicense():
        """Deactivates the license activation and frees up the correponding activation
        slot by contacting the Cryptlex servers.

        Raises:
                LexActivatorException

        Returns:
                int: LA_OK, LA_FAIL
        """
        status = LexActivatorNative.DeactivateLicense()
        if LexStatusCodes.LA_OK == status:
            return LexStatusCodes.LA_OK
        elif LexStatusCodes.LA_FAIL == status:
            return LexStatusCodes.LA_FAIL
        else:
            raise LexActivatorException(status)

    @staticmethod
    def GenerateOfflineDeactivationRequest(file_path):
        """Generates the offline deactivation request needed for deactivation of the
        license in the dashboard and deactivates the license locally.

        A valid offline deactivation file confirms that the license has been
        successfully deactivated on the user's machine.

        Args:
                file_path (str): path of the file for the offline deactivation request

        Raises:
                LexActivatorException

        Returns:
                int: LA_OK, LA_FAIL
        """
        cstring_file_path = LexActivatorNative.get_ctype_string(file_path)
        status = LexActivatorNative.GenerateOfflineDeactivationRequest(
            cstring_file_path)
        if LexStatusCodes.LA_OK == status:
            return LexStatusCodes.LA_OK
        elif LexStatusCodes.LA_FAIL == status:
            return LexStatusCodes.LA_FAIL
        else:
            raise LexActivatorException(status)

    @staticmethod
    def IsLicenseGenuine():
        """It verifies whether your app is genuinely activated or not. The verification
        is done locally by verifying the cryptographic digital signature fetched at
        the time of activation.

        After verifying locally, it schedules a server check in a separate thread.
        After the first server sync it periodically does further syncs at a frequency
        set for the license.

        In case server sync fails due to network error, and it continues to fail for
        fixed number of days (grace period), the function returns
        LA_GRACE_PERIOD_OVER instead of LA_OK.

        This function must be called on every start of your program to verify the
        activation of your app.

        Note: 
                If application was activated offline using ActivateLicenseOffline() function, 
                you may want to set grace period to 0 to ignore grace period.

        Raises:
                LexActivatorException

        Returns:
                int: LA_OK, LA_EXPIRED, LA_SUSPENDED, LA_GRACE_PERIOD_OVER, LA_FAIL
        """
        status = LexActivatorNative.IsLicenseGenuine()
        if LexStatusCodes.LA_OK == status:
            return LexStatusCodes.LA_OK
        elif LexStatusCodes.LA_EXPIRED == status:
            return LexStatusCodes.LA_EXPIRED
        elif LexStatusCodes.LA_SUSPENDED == status:
            return LexStatusCodes.LA_SUSPENDED
        elif LexStatusCodes.LA_GRACE_PERIOD_OVER == status:
            return LexStatusCodes.LA_GRACE_PERIOD_OVER
        elif LexStatusCodes.LA_FAIL == status:
            return LexStatusCodes.LA_FAIL
        else:
            raise LexActivatorException(status)

    @staticmethod
    def IsLicenseValid():
        """It verifies whether your app is genuinely activated or not. The verification
        is done locally by verifying the cryptographic digital signature fetched at
        the time of activation.

        This is just an auxiliary function which you may use in some specific cases,
        when you want to skip the server sync.

        Note: 
                You may want to set grace period to 0 to ignore grace period.

        Raises:
                LexActivatorException

        Returns:
                int: LA_OK, LA_EXPIRED, LA_SUSPENDED, LA_GRACE_PERIOD_OVER, LA_FAIL
        """
        status = LexActivatorNative.IsLicenseValid()
        if LexStatusCodes.LA_OK == status:
            return LexStatusCodes.LA_OK
        elif LexStatusCodes.LA_EXPIRED == status:
            return LexStatusCodes.LA_EXPIRED
        elif LexStatusCodes.LA_SUSPENDED == status:
            return LexStatusCodes.LA_SUSPENDED
        elif LexStatusCodes.LA_GRACE_PERIOD_OVER == status:
            return LexStatusCodes.LA_GRACE_PERIOD_OVER
        elif LexStatusCodes.LA_FAIL == status:
            return LexStatusCodes.LA_FAIL
        else:
            raise LexActivatorException(status)

    @staticmethod
    def ActivateTrial():
        """Starts the verified trial in your application by contacting the Cryptlex
        servers.

        This function should be executed when your application starts first time on
        the user's computer, ideally on a button click.

        Raises:
                LexActivatorException

        Returns:
                int: LA_OK, LA_TRIAL_EXPIRED
        """
        status = LexActivatorNative.ActivateTrial()
        if LexStatusCodes.LA_OK == status:
            return LexStatusCodes.LA_OK
        elif LexStatusCodes.LA_TRIAL_EXPIRED == status:
            return LexStatusCodes.LA_TRIAL_EXPIRED
        elif LexStatusCodes.LA_FAIL == status:
            return LexStatusCodes.LA_FAIL
        else:
            raise LexActivatorException(status)

    @staticmethod
    def ActivateTrialOffline(file_path):
        """Activates the trial using the offline activation response file.

        Args:
                file_path (str): path of the offline activation response file

        Raises:
                LexActivatorException

        Returns:
                int: LA_OK, LA_TRIAL_EXPIRED, LA_FAIL
        """
        cstring_file_path = LexActivatorNative.get_ctype_string(file_path)
        status = LexActivatorNative.ActivateTrialOffline(cstring_file_path)
        if LexStatusCodes.LA_OK == status:
            return LexStatusCodes.LA_OK
        elif LexStatusCodes.LA_TRIAL_EXPIRED == status:
            return LexStatusCodes.LA_TRIAL_EXPIRED
        elif LexStatusCodes.LA_FAIL == status:
            return LexStatusCodes.LA_FAIL
        else:
            raise LexActivatorException(status)

    @staticmethod
    def GenerateOfflineTrialActivationRequest(file_path):
        """Generates the offline trial activation request needed for generating offline
        trial activation response in the dashboard.

        Args:
                file_path (str): path of the file for the offline request

        Raises:
                LexActivatorException
        """
        cstring_file_path = LexActivatorNative.get_ctype_string(file_path)
        status = LexActivatorNative.GenerateOfflineTrialActivationRequest(
            cstring_file_path)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def IsTrialGenuine():
        """It verifies whether trial has started and is genuine or not. The verification
        is done locally by verifying the cryptographic digital signature fetched at
        the time of trial activation.

        This function must be called on every start of your program during the trial
        period.

        Raises:
                LexActivatorException

        Returns:
                int: LA_OK, LA_TRIAL_EXPIRED, LA_FAIL
        """
        status = LexActivatorNative.IsTrialGenuine()
        if LexStatusCodes.LA_OK == status:
            return LexStatusCodes.LA_OK
        elif LexStatusCodes.LA_TRIAL_EXPIRED == status:
            return LexStatusCodes.LA_TRIAL_EXPIRED
        elif LexStatusCodes.LA_FAIL == status:
            return LexStatusCodes.LA_FAIL
        else:
            raise LexActivatorException(status)

    @staticmethod
    def ActivateLocalTrial(trialLength):
        """Starts the local (unverified) trial.

        This function should be executed when your application starts first time on
        the user's computer, ideally on a button click.

        Args:
                trialLength (int): trial length in days

        Raises:
                LexActivatorException

        Returns:
                int: LA_OK, LA_LOCAL_TRIAL_EXPIRED, LA_FAIL
        """
        status = LexActivatorNative.ActivateLocalTrial(trialLength)
        if LexStatusCodes.LA_OK == status:
            return LexStatusCodes.LA_OK
        elif LexStatusCodes.LA_TRIAL_EXPIRED == status:
            return LexStatusCodes.LA_LOCAL_TRIAL_EXPIRED
        elif LexStatusCodes.LA_FAIL == status:
            return LexStatusCodes.LA_FAIL
        else:
            raise LexActivatorException(status)

    @staticmethod
    def IsLocalTrialGenuine():
        """It verifies whether trial has started and is genuine or not. The verification
        is done locally.

        This function must be called on every start of your program during the trial period.

        Raises:
                LexActivatorException

        Returns:
                int: LA_OK, LA_LOCAL_TRIAL_EXPIRED, LA_FAIL
        """
        status = LexActivatorNative.IsLocalTrialGenuine()
        if LexStatusCodes.LA_OK == status:
            return LexStatusCodes.LA_OK
        elif LexStatusCodes.LA_TRIAL_EXPIRED == status:
            return LexStatusCodes.LA_LOCAL_TRIAL_EXPIRED
        elif LexStatusCodes.LA_FAIL == status:
            return LexStatusCodes.LA_FAIL
        else:
            raise LexActivatorException(status)

    @staticmethod
    def ExtendLocalTrial(trialExtensionLength):
        """Extends the local trial.

        This function is only meant for unverified trials.

        Args:
                trialExtensionLength (int): number of days to extend the trial

        Raises:
                LexActivatorException

        Returns:
                int: LA_OK, LA_FAIL
        """
        status = LexActivatorNative.ExtendLocalTrial(trialExtensionLength)
        if LexStatusCodes.LA_OK == status:
            return LexStatusCodes.LA_OK
        elif LexStatusCodes.LA_FAIL == status:
            return LexStatusCodes.LA_FAIL
        else:
            raise LexActivatorException(status)

    @staticmethod
    def IncrementActivationMeterAttributeUses(name, increment):
        """Increments the meter attribute uses of the activation.

        Args:
                name (str):  name of the meter attribute
                increment (int): the increment value

        Raises:
                LexActivatorException
        """
        cstring_name = LexActivatorNative.get_ctype_string(name)
        status = LexActivatorNative.IncrementActivationMeterAttributeUses(
            cstring_name, increment)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def DecrementActivationMeterAttributeUses(name, decrement):
        """Decrements the meter attribute uses of the activation.

        Args:
                name (str): name of the meter attribute
                decrement (int): the decrement value

        Raises:
                LexActivatorException
        """
        cstring_name = LexActivatorNative.get_ctype_string(name)
        status = LexActivatorNative.DecrementActivationMeterAttributeUses(
            cstring_name, decrement)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def ResetActivationMeterAttributeUses(name):
        """Resets the meter attribute uses of the activation.

        Args:
                name (str): name of the meter attribute

        Raises:
                LexActivatorException
        """
        cstring_name = LexActivatorNative.get_ctype_string(name)
        status = LexActivatorNative.ResetActivationMeterAttributeUses(
            cstring_name)
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)

    @staticmethod
    def Reset():
        """Resets the activation and trial data stored in the machine.

        This function is meant for developer testing only.

        Raises:
                LexActivatorException
        """
        status = LexActivatorNative.Reset()
        if LexStatusCodes.LA_OK != status:
            raise LexActivatorException(status)
