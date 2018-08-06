from ctypes import *
import os, sys, inspect
import ctypes
import ctypes.util


def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
            and type._type_ != "P"):
        return type
    else:
        return c_void_p


def get_library_path():
    # Get the working directory of this file
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    dir_path = os.path.dirname(os.path.abspath(filename))
    if sys.platform == 'darwin':
        return os.path.join(dir_path, "libLexActivator.dylib")
    elif sys.platform == 'linux':
        return os.path.join(dir_path, "libLexActivator.so")
    elif sys.platform == 'win32':
        return os.path.join(dir_path, "LexActivator.dll")
    else:
        raise TypeError("Platform not supported!")


def load_library(path):
    if sys.platform == 'darwin':
        return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
    elif sys.platform == 'linux':
        return ctypes.cdll.LoadLibrary(path)
    elif sys.platform == 'win32':
        return ctypes.cdll.LoadLibrary(path)
    else:
        raise TypeError("Platform not supported!")

def get_char_type():
    if sys.platform == 'win32':
        return c_wchar_p
    else:
        return c_char_p

library = load_library(get_library_path())

# define types
CSTRTYPE = get_char_type()
STRTYPE = get_char_type()

CallbackType = CFUNCTYPE(UNCHECKED(None), c_uint32)


class PermissionFlags:
    LA_USER = 1
    LA_SYSTEM = 2


SetProductFile = library.SetProductFile
SetProductFile.argtypes = [CSTRTYPE]
SetProductFile.restype = c_int

SetProductData = library.SetProductData
SetProductData.argtypes = [CSTRTYPE]
SetProductData.restype = c_int

SetProductId = library.SetProductId
SetProductId.argtypes = [CSTRTYPE, c_uint32]
SetProductId.restype = c_int

SetLicenseKey = library.SetLicenseKey
SetLicenseKey.argtypes = [CSTRTYPE]
SetLicenseKey.restype = c_int

SetLicenseCallback = library.SetLicenseCallback
SetLicenseCallback.argtypes = [CallbackType]
SetLicenseCallback.restype = c_int

SetActivationMetadata = library.SetActivationMetadata
SetActivationMetadata.argtypes = [CSTRTYPE, CSTRTYPE]
SetActivationMetadata.restype = c_int

SetTrialActivationMetadata = library.SetTrialActivationMetadata
SetTrialActivationMetadata.argtypes = [CSTRTYPE, CSTRTYPE]
SetTrialActivationMetadata.restype = c_int

SetAppVersion = library.SetAppVersion
SetAppVersion.argtypes = [CSTRTYPE]
SetAppVersion.restype = c_int

SetNetworkProxy = library.SetNetworkProxy
SetNetworkProxy.argtypes = [CSTRTYPE]
SetNetworkProxy.restype = c_int

GetProductMetadata = library.GetProductMetadata
GetProductMetadata.argtypes = [CSTRTYPE, STRTYPE, c_uint32]
GetProductMetadata.restype = c_int

GetLicenseMetadata = library.GetLicenseMetadata
GetLicenseMetadata.argtypes = [CSTRTYPE, STRTYPE, c_uint32]
GetLicenseMetadata.restype = c_int

GetLicenseKey = library.GetLicenseKey
GetLicenseKey.argtypes = [STRTYPE, c_uint32]
GetLicenseKey.restype = c_int

GetLicenseExpiryDate = library.GetLicenseExpiryDate
GetLicenseExpiryDate.argtypes = [POINTER(c_uint32)]
GetLicenseExpiryDate.restype = c_int

GetLicenseUserEmail = library.GetLicenseUserEmail
GetLicenseUserEmail.argtypes = [STRTYPE, c_uint32]
GetLicenseUserEmail.restype = c_int

GetLicenseUserName = library.GetLicenseUserName
GetLicenseUserName.argtypes = [STRTYPE, c_uint32]
GetLicenseUserName.restype = c_int

GetActivationMetadata = library.GetActivationMetadata
GetActivationMetadata.argtypes = [CSTRTYPE, STRTYPE, c_uint32]
GetActivationMetadata.restype = c_int

GetTrialActivationMetadata = library.GetTrialActivationMetadata
GetTrialActivationMetadata.argtypes = [CSTRTYPE, STRTYPE, c_uint32]
GetTrialActivationMetadata.restype = c_int

GetTrialExpiryDate = library.GetTrialExpiryDate
GetTrialExpiryDate.argtypes = [POINTER(c_uint32)]
GetTrialExpiryDate.restype = c_int

GetTrialId = library.GetTrialId
GetTrialId.argtypes = [STRTYPE, c_uint32]
GetTrialId.restype = c_int

GetLocalTrialExpiryDate = library.GetLocalTrialExpiryDate
GetLocalTrialExpiryDate.argtypes = [POINTER(c_uint32)]
GetLocalTrialExpiryDate.restype = c_int

ActivateLicense = library.ActivateLicense
ActivateLicense.argtypes = []
ActivateLicense.restype = c_int

ActivateLicenseOffline = library.ActivateLicenseOffline
ActivateLicenseOffline.argtypes = [CSTRTYPE]
ActivateLicenseOffline.restype = c_int

GenerateOfflineActivationRequest = library.GenerateOfflineActivationRequest
GenerateOfflineActivationRequest.argtypes = [CSTRTYPE]
GenerateOfflineActivationRequest.restype = c_int

DeactivateLicense = library.DeactivateLicense
DeactivateLicense.argtypes = []
DeactivateLicense.restype = c_int

GenerateOfflineDeactivationRequest = library.GenerateOfflineDeactivationRequest
GenerateOfflineDeactivationRequest.argtypes = [CSTRTYPE]
GenerateOfflineDeactivationRequest.restype = c_int

IsLicenseGenuine = library.IsLicenseGenuine
IsLicenseGenuine.argtypes = []
IsLicenseGenuine.restype = c_int

IsLicenseValid = library.IsLicenseValid
IsLicenseValid.argtypes = []
IsLicenseValid.restype = c_int

ActivateTrial = library.ActivateTrial
ActivateTrial.argtypes = []
ActivateTrial.restype = c_int

IsTrialGenuine = library.IsTrialGenuine
IsTrialGenuine.argtypes = []
IsTrialGenuine.restype = c_int

ActivateLocalTrial = library.ActivateLocalTrial
ActivateLocalTrial.argtypes = [c_uint32]
ActivateLocalTrial.restype = c_int

IsLocalTrialGenuine = library.IsLocalTrialGenuine
IsLocalTrialGenuine.argtypes = []
IsLocalTrialGenuine.restype = c_int

ExtendLocalTrial = library.ExtendLocalTrial
ExtendLocalTrial.argtypes = [c_uint32]
ExtendLocalTrial.restype = c_int

Reset = library.Reset
Reset.argtypes = []
Reset.restype = c_int


class StatusCodes:
    LA_OK = 0

    LA_FAIL = 1

    LA_EXPIRED = 20

    LA_SUSPENDED = 21

    LA_GRACE_PERIOD_OVER = 22

    LA_TRIAL_EXPIRED = 25

    LA_LOCAL_TRIAL_EXPIRED = 26

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

    LA_E_VM = 80

    LA_E_COUNTRY = 81

    LA_E_IP = 82

    LA_E_RATE_LIMIT = 90

    LA_E_SERVER = 91

    LA_E_CLIENT = 92
