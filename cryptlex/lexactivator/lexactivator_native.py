from ctypes import *
import os
import sys
import platform
import inspect
import subprocess
import ctypes
import ctypes.util


def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
            and type._type_ != "P"):
        return type
    else:
        return c_void_p


def is_os_64bit():
    return platform.machine().endswith('64')

def get_arch():
    is_64bits = sys.maxsize > 2**32
    machine = platform.machine().lower()
    if 'arm' in machine or 'aarch64' in machine:
        if is_64bits:
            return 'arm64'
        else:
            return 'armhf'
    elif is_64bits:
        return 'x86_64'
    else:
        return 'x86'

def is_musl():
    command = ['ldd', '--version']
    try:
        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT).decode()
    except subprocess.CalledProcessError as e:
        output = e.output.decode()
    if 'musl' in output:
        return True
    return False


def get_library_path():
    compiler = 'gcc'
    arch = get_arch()
    # Get the working directory of this file
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    dir_path = os.path.dirname(os.path.abspath(filename))

    if not os.path.exists(dir_path):
        dir_path = os.path.abspath(os.path.dirname(__file__))

    if sys.platform == 'darwin':
        return os.path.join(dir_path, "libs/macos/"+arch+"/libLexActivator.dylib")
    elif sys.platform.startswith('linux'):
        if(is_musl()):
            compiler = 'musl'
        return os.path.join(dir_path, "libs/linux/"+compiler+"/"+arch+"/libLexActivator.so")
    elif sys.platform == 'win32':
        return os.path.join(dir_path, "libs/win32/"+arch+"/LexActivator.dll")
    else:
        raise TypeError("Platform not supported!")


def load_library(path):
    if sys.platform == 'darwin':
        return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
    elif sys.platform.startswith('linux'):
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


def get_ctype_string_buffer(size):
    if sys.platform == 'win32':
        return ctypes.create_unicode_buffer(size)
    else:
        return ctypes.create_string_buffer(size)


def get_ctype_string(input):
    if sys.platform == 'win32':
        return ctypes.c_wchar_p(input)
    else:
        return ctypes.c_char_p(input.encode('utf-8'))


def byte_to_string(input):
    if sys.platform == 'win32':
        return input
    else:
        return input.decode('utf-8')


library = load_library(get_library_path())

# define types
CSTRTYPE = get_char_type()
STRTYPE = get_char_type()

CallbackType = CFUNCTYPE(UNCHECKED(None), c_uint32)


SetProductFile = library.SetProductFile
SetProductFile.argtypes = [CSTRTYPE]
SetProductFile.restype = c_int

SetProductData = library.SetProductData
SetProductData.argtypes = [CSTRTYPE]
SetProductData.restype = c_int

SetProductId = library.SetProductId
SetProductId.argtypes = [CSTRTYPE, c_uint32]
SetProductId.restype = c_int

SetDataDirectory = library.SetDataDirectory
SetDataDirectory.argtypes = [CSTRTYPE]
SetDataDirectory.restype = c_int

SetDebugMode = library.SetDebugMode
SetDebugMode.argtypes = [c_uint32]
SetDebugMode.restype = c_int

SetCustomDeviceFingerprint = library.SetCustomDeviceFingerprint
SetCustomDeviceFingerprint.argtypes = [CSTRTYPE]
SetCustomDeviceFingerprint.restype = c_int

SetLicenseKey = library.SetLicenseKey
SetLicenseKey.argtypes = [CSTRTYPE]
SetLicenseKey.restype = c_int

SetLicenseUserCredential = library.SetLicenseUserCredential
SetLicenseUserCredential.argtypes = [CSTRTYPE, CSTRTYPE]
SetLicenseUserCredential.restype = c_int

SetLicenseCallback = library.SetLicenseCallback
SetLicenseCallback.argtypes = [CallbackType]
SetLicenseCallback.restype = c_int

SetActivationLeaseDuration = library.SetActivationLeaseDuration
SetActivationLeaseDuration.argtypes = [c_uint32]
SetActivationLeaseDuration.restype = c_int

SetActivationMetadata = library.SetActivationMetadata
SetActivationMetadata.argtypes = [CSTRTYPE, CSTRTYPE]
SetActivationMetadata.restype = c_int

SetTrialActivationMetadata = library.SetTrialActivationMetadata
SetTrialActivationMetadata.argtypes = [CSTRTYPE, CSTRTYPE]
SetTrialActivationMetadata.restype = c_int

SetAppVersion = library.SetAppVersion
SetAppVersion.argtypes = [CSTRTYPE]
SetAppVersion.restype = c_int

SetReleaseVersion = library.SetReleaseVersion
SetReleaseVersion.argtypes = [CSTRTYPE]
SetReleaseVersion.restype = c_int

SetReleasePublishedDate = library.SetReleasePublishedDate
SetReleasePublishedDate.argtypes = [c_uint32]
SetReleasePublishedDate.restype = c_int

SetReleasePlatform = library.SetReleasePlatform
SetReleasePlatform.argtypes = [CSTRTYPE]
SetReleasePlatform.restype = c_int

SetReleaseChannel = library.SetReleaseChannel
SetReleaseChannel.argtypes = [CSTRTYPE]
SetReleaseChannel.restype = c_int

SetOfflineActivationRequestMeterAttributeUses = library.SetOfflineActivationRequestMeterAttributeUses
SetOfflineActivationRequestMeterAttributeUses.argtypes = [CSTRTYPE, c_uint32]
SetOfflineActivationRequestMeterAttributeUses.restype = c_int

SetNetworkProxy = library.SetNetworkProxy
SetNetworkProxy.argtypes = [CSTRTYPE]
SetNetworkProxy.restype = c_int

SetCryptlexHost = library.SetCryptlexHost
SetCryptlexHost.argtypes = [CSTRTYPE]
SetCryptlexHost.restype = c_int

GetProductMetadata = library.GetProductMetadata
GetProductMetadata.argtypes = [CSTRTYPE, STRTYPE, c_uint32]
GetProductMetadata.restype = c_int

GetProductVersionName = library.GetProductVersionName
GetProductVersionName.argtypes = [STRTYPE,c_uint32]
GetProductVersionName.restype = c_int

GetProductVersionDisplayName = library.GetProductVersionDisplayName
GetProductVersionDisplayName.argtypes = [STRTYPE,c_uint32]
GetProductVersionDisplayName.restype = c_int

GetProductVersionFeatureFlag = library.GetProductVersionFeatureFlag
GetProductVersionFeatureFlag.argtypes = [CSTRTYPE, POINTER(c_uint32), STRTYPE, c_uint32]
GetProductVersionFeatureFlag.restype = c_int

GetLicenseMetadata = library.GetLicenseMetadata
GetLicenseMetadata.argtypes = [CSTRTYPE, STRTYPE, c_uint32]
GetLicenseMetadata.restype = c_int

GetLicenseMeterAttribute = library.GetLicenseMeterAttribute
GetLicenseMeterAttribute.argtypes = [CSTRTYPE, POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32)]
GetLicenseMeterAttribute.restype = c_int

GetLicenseKey = library.GetLicenseKey
GetLicenseKey.argtypes = [STRTYPE, c_uint32]
GetLicenseKey.restype = c_int

GetLicenseAllowedActivations = library.GetLicenseAllowedActivations
GetLicenseAllowedActivations.argtypes = [POINTER(c_uint32)]
GetLicenseAllowedActivations.restype = c_int

GetLicenseTotalActivations = library.GetLicenseTotalActivations
GetLicenseTotalActivations.argtypes = [POINTER(c_uint32)]
GetLicenseTotalActivations.restype = c_int

GetLicenseExpiryDate = library.GetLicenseExpiryDate
GetLicenseExpiryDate.argtypes = [POINTER(c_uint32)]
GetLicenseExpiryDate.restype = c_int

GetLicenseMaintenanceExpiryDate = library.GetLicenseMaintenanceExpiryDate
GetLicenseMaintenanceExpiryDate.argtypes = [POINTER(c_uint32)]
GetLicenseMaintenanceExpiryDate.restype = c_int

GetLicenseMaxAllowedReleaseVersion = library.GetLicenseMaxAllowedReleaseVersion
GetLicenseMaxAllowedReleaseVersion.argtypes = [STRTYPE, c_uint32]
GetLicenseMaxAllowedReleaseVersion.restype = c_int

GetLicenseUserEmail = library.GetLicenseUserEmail
GetLicenseUserEmail.argtypes = [STRTYPE, c_uint32]
GetLicenseUserEmail.restype = c_int

GetLicenseUserName = library.GetLicenseUserName
GetLicenseUserName.argtypes = [STRTYPE, c_uint32]
GetLicenseUserName.restype = c_int

GetLicenseUserCompany = library.GetLicenseUserCompany
GetLicenseUserCompany.argtypes = [STRTYPE, c_uint32]
GetLicenseUserCompany.restype = c_int

GetLicenseUserMetadata = library.GetLicenseUserMetadata
GetLicenseUserMetadata.argtypes = [CSTRTYPE, STRTYPE, c_uint32]
GetLicenseUserMetadata.restype = c_int

GetLicenseType = library.GetLicenseType
GetLicenseType.argtypes = [STRTYPE, c_uint32]
GetLicenseType.restype = c_int

GetActivationMetadata = library.GetActivationMetadata
GetActivationMetadata.argtypes = [CSTRTYPE, STRTYPE, c_uint32]
GetActivationMetadata.restype = c_int

GetActivationMode = library.GetActivationMode
GetActivationMode.argtypes = [STRTYPE, c_uint32, STRTYPE, c_uint32]
GetActivationMode.restype = c_int

GetActivationMeterAttributeUses = library.GetActivationMeterAttributeUses
GetActivationMeterAttributeUses.argtypes = [CSTRTYPE, POINTER(c_uint32)]
GetActivationMeterAttributeUses.restype = c_int

GetServerSyncGracePeriodExpiryDate = library.GetServerSyncGracePeriodExpiryDate
GetServerSyncGracePeriodExpiryDate.argtypes = [POINTER(c_uint32)]
GetServerSyncGracePeriodExpiryDate.restype = c_int

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

GetLibraryVersion = library.GetLibraryVersion
GetLibraryVersion.argtypes = [STRTYPE, c_uint32]
GetLibraryVersion.restype = c_int

CheckForReleaseUpdate = library.CheckForReleaseUpdate
CheckForReleaseUpdate.argtypes = [CSTRTYPE, CSTRTYPE, CSTRTYPE, CallbackType]
CheckForReleaseUpdate.restype = c_int

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

ActivateTrialOffline = library.ActivateTrialOffline
ActivateTrialOffline.argtypes = [CSTRTYPE]
ActivateTrialOffline.restype = c_int

GenerateOfflineTrialActivationRequest = library.GenerateOfflineTrialActivationRequest
GenerateOfflineTrialActivationRequest.argtypes = [CSTRTYPE]
GenerateOfflineTrialActivationRequest.restype = c_int

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

IncrementActivationMeterAttributeUses = library.IncrementActivationMeterAttributeUses
IncrementActivationMeterAttributeUses.argtypes = [CSTRTYPE, c_uint32]
IncrementActivationMeterAttributeUses.restype = c_int

DecrementActivationMeterAttributeUses = library.DecrementActivationMeterAttributeUses
DecrementActivationMeterAttributeUses.argtypes = [CSTRTYPE, c_uint32]
DecrementActivationMeterAttributeUses.restype = c_int

ResetActivationMeterAttributeUses = library.ResetActivationMeterAttributeUses
ResetActivationMeterAttributeUses.argtypes = [CSTRTYPE]
ResetActivationMeterAttributeUses.restype = c_int

Reset = library.Reset
Reset.argtypes = []
Reset.restype = c_int
