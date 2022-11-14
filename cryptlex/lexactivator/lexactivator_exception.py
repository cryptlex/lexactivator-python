from cryptlex.lexactivator.lexstatus_codes import LexStatusCodes


class LexActivatorException(Exception):
    def __init__(self, code):
        super(LexActivatorException, self).__init__(
            LexActivatorException.get_error_message(code))
        self.message = LexActivatorException.get_error_message(code)
        self.code = code

    @staticmethod
    def get_error_message(code):
        if code == LexStatusCodes.LA_E_FILE_PATH:
            return 'Invalid file path.'
        if code == LexStatusCodes.LA_E_PRODUCT_FILE:
            return 'Invalid or corrupted product file.'
        if code == LexStatusCodes.LA_E_PRODUCT_DATA:
            return 'Invalid product data.'
        if code == LexStatusCodes.LA_E_PRODUCT_ID:
            return 'The product id is incorrect.'
        if code == LexStatusCodes.LA_E_SYSTEM_PERMISSION:
            return 'Insufficient system permissions.'
        if code == LexStatusCodes.LA_E_FILE_PERMISSION:
            return 'No permission to write to file.'
        if code == LexStatusCodes.LA_E_WMIC:
            return 'Fingerprint couldn\'t be generated because Windows Management Instrumentation (WMI) service has been disabled.'
        if code == LexStatusCodes.LA_E_TIME:
            return 'The difference between the network time and the system time is more than allowed clock offset.'
        if code == LexStatusCodes.LA_E_INET:
            return 'Failed to connect to the server due to network error.'
        if code == LexStatusCodes.LA_E_NET_PROXY:
            return 'Invalid network proxy.'
        if code == LexStatusCodes.LA_E_HOST_URL:
            return 'Invalid Cryptlex host url.'
        if code == LexStatusCodes.LA_E_BUFFER_SIZE:
            return 'The buffer size was smaller than required.'
        if code == LexStatusCodes.LA_E_APP_VERSION_LENGTH:
            return 'App version length is more than 256 characters.'
        if code == LexStatusCodes.LA_E_REVOKED:
            return 'The license has been revoked.'
        if code == LexStatusCodes.LA_E_LICENSE_KEY:
            return 'Invalid license key.'
        if code == LexStatusCodes.LA_E_LICENSE_TYPE:
            return 'Invalid license type. Make sure floating license is not being used.'
        if code == LexStatusCodes.LA_E_OFFLINE_RESPONSE_FILE:
            return 'Invalid offline activation response file.'
        if code == LexStatusCodes.LA_E_OFFLINE_RESPONSE_FILE_EXPIRED:
            return 'The offline activation response has expired.'
        if code == LexStatusCodes.LA_E_ACTIVATION_LIMIT:
            return 'The license has reached it\'s allowed activations limit.'
        if code == LexStatusCodes.LA_E_ACTIVATION_NOT_FOUND:
            return 'The license activation was deleted on the server.'
        if code == LexStatusCodes.LA_E_DEACTIVATION_LIMIT:
            return 'The license has reached it\'s allowed deactivations limit.'
        if code == LexStatusCodes.LA_E_TRIAL_NOT_ALLOWED:
            return 'Trial not allowed for the product.'
        if code == LexStatusCodes.LA_E_TRIAL_ACTIVATION_LIMIT:
            return 'Your account has reached it\'s trial activations limit.'
        if code == LexStatusCodes.LA_E_MACHINE_FINGERPRINT:
            return 'Machine fingerprint has changed since activation.'
        if code == LexStatusCodes.LA_E_METADATA_KEY_LENGTH:
            return 'Metadata key length is more than 256 characters.'
        if code == LexStatusCodes.LA_E_METADATA_VALUE_LENGTH:
            return 'Metadata value length is more than 256 characters.'
        if code == LexStatusCodes.LA_E_ACTIVATION_METADATA_LIMIT:
            return 'The license has reached it\'s metadata fields limit.'
        if code == LexStatusCodes.LA_E_TRIAL_ACTIVATION_METADATA_LIMIT:
            return 'The trial has reached it\'s metadata fields limit.'
        if code == LexStatusCodes.LA_E_METADATA_KEY_NOT_FOUND:
            return 'The metadata key does not exist.'
        if code == LexStatusCodes.LA_E_TIME_MODIFIED:
            return 'The system time has been tampered (backdated).'
        if code == LexStatusCodes.LA_E_RELEASE_VERSION_FORMAT:
            return 'Invalid version format.'
        if code == LexStatusCodes.LA_E_AUTHENTICATION_FAILED:
            return 'Incorrect email or password.'
        if code == LexStatusCodes.LA_E_METER_ATTRIBUTE_NOT_FOUND:
            return 'The meter attribute does not exist.'
        if code == LexStatusCodes.LA_E_METER_ATTRIBUTE_USES_LIMIT_REACHED:
            return 'The meter attribute has reached it\'s usage limit.'
        if code == LexStatusCodes.LA_E_CUSTOM_FINGERPRINT_LENGTH:
            return 'Custom device fingerprint length is less than 64 characters or more than 256 characters.'
        if code == LexStatusCodes.LA_E_PRODUCT_VERSION_NOT_LINKED:
            return 'No product version is linked with the license.'
        if code == LexStatusCodes.LA_E_FEATURE_FLAG_NOT_FOUND:
            return 'The product version feature flag does not exist.'
        if code == LexStatusCodes.LA_E_RELEASE_VERSION_NOT_ALLOWED:
            return 'The release version is not allowed.'
        if code == LexStatusCodes.LA_E_RELEASE_PLATFORM_LENGTH:
            return 'Release platform length is more than 256 characters.'
        if code == LexStatusCodes.LA_E_RELEASE_CHANNEL_LENGTH:
            return 'Release channel length is more than 256 characters.'
        if code == LexStatusCodes.LA_E_VM:
            return 'Application is being run inside a virtual machine / hypervisor, and activation has been disallowed in the VM.'
        if code == LexStatusCodes.LA_E_COUNTRY:
            return 'Country is not allowed.'
        if code == LexStatusCodes.LA_E_IP:
            return 'IP address is not allowed.'
        if code == LexStatusCodes.LA_E_CONTAINER:
            return 'Application is being run inside a container and activation has been disallowed in the container.'
        if code == LexStatusCodes.LA_E_RATE_LIMIT:
            return 'Rate limit for API has reached, try again later.'
        if code == LexStatusCodes.LA_E_SERVER:
            return 'Server error.'
        if code == LexStatusCodes.LA_E_CLIENT:
            return 'Client error.'
        return 'Unknown error!'
