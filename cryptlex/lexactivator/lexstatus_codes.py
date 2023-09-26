class LexStatusCodes:
    LA_OK = 0

    LA_FAIL = 1

    LA_EXPIRED = 20

    LA_SUSPENDED = 21

    LA_GRACE_PERIOD_OVER = 22

    LA_TRIAL_EXPIRED = 25

    LA_LOCAL_TRIAL_EXPIRED = 26

    LA_RELEASE_UPDATE_AVAILABLE = 30

    LA_RELEASE_NO_UPDATE_AVAILABLE = 31 # deprecated

    LA_RELEASE_UPDATE_NOT_AVAILABLE = 31

    LA_RELEASE_UPDATE_AVAILABLE_NOT_ALLOWED = 32

    LA_E_FILE_PATH = 40

    LA_E_PRODUCT_FILE = 41

    LA_E_PRODUCT_DATA = 42

    LA_E_PRODUCT_ID = 43

    LA_E_SYSTEM_PERMISSION = 44

    LA_E_FILE_PERMISSION = 45

    LA_E_WMIC = 46

    LA_E_TIME = 47

    LA_E_INET = 48

    LA_E_NET_PROXY = 49

    LA_E_HOST_URL = 50

    LA_E_BUFFER_SIZE = 51

    LA_E_APP_VERSION_LENGTH = 52

    LA_E_REVOKED = 53

    LA_E_LICENSE_KEY = 54

    LA_E_LICENSE_TYPE = 55

    LA_E_OFFLINE_RESPONSE_FILE = 56

    LA_E_OFFLINE_RESPONSE_FILE_EXPIRED = 57

    LA_E_ACTIVATION_LIMIT = 58

    LA_E_ACTIVATION_NOT_FOUND = 59

    LA_E_DEACTIVATION_LIMIT = 60

    LA_E_TRIAL_NOT_ALLOWED = 61

    LA_E_TRIAL_ACTIVATION_LIMIT = 62

    LA_E_MACHINE_FINGERPRINT = 63

    LA_E_METADATA_KEY_LENGTH = 64

    LA_E_METADATA_VALUE_LENGTH = 65

    LA_E_ACTIVATION_METADATA_LIMIT = 66

    LA_E_TRIAL_ACTIVATION_METADATA_LIMIT = 67

    LA_E_METADATA_KEY_NOT_FOUND = 68

    LA_E_TIME_MODIFIED = 69

    LA_E_RELEASE_VERSION_FORMAT = 70

    LA_E_AUTHENTICATION_FAILED = 71

    LA_E_METER_ATTRIBUTE_NOT_FOUND = 72

    LA_E_METER_ATTRIBUTE_USES_LIMIT_REACHED = 73

    LA_E_CUSTOM_FINGERPRINT_LENGTH = 74

    LA_E_PRODUCT_VERSION_NOT_LINKED = 75

    LA_E_FEATURE_FLAG_NOT_FOUND = 76

    LA_E_RELEASE_VERSION_NOT_ALLOWED = 77

    LA_E_RELEASE_PLATFORM_LENGTH = 78

    LA_E_RELEASE_CHANNEL_LENGTH = 79

    LA_E_VM = 80

    LA_E_COUNTRY = 81

    LA_E_IP = 82

    LA_E_CONTAINER = 83

    LA_E_RELEASE_VERSION = 84

    LA_E_RELEASE_PLATFORM = 85

    LA_E_RELEASE_CHANNEL = 86

    LA_E_USER_NOT_AUTHENTICATED = 87

    LA_E_TWO_FACTOR_AUTHENTICATION_CODE_MISSING = 88

    LA_E_TWO_FACTOR_AUTHENTICATION_CODE_INVALID = 89

    LA_E_RATE_LIMIT = 90

    LA_E_SERVER = 91

    LA_E_CLIENT = 92

    LA_E_LOGIN_TEMPORARILY_LOCKED = 100

    LA_E_AUTHENTICATION_ID_TOKEN  = 101

    LA_E_OIDC_SSO_NOT_ENABLED = 102

    LA_E_USERS_LIMIT_REACHED = 103
