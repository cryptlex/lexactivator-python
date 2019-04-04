import sys, ctypes, time
import LexActivator

# Refer to following link for LexActivator API docs:
# https://github.com/cryptlex/lexactivator-c/blob/master/examples/LexActivator.h
# https://github.com/cryptlex/lexactivator-c/blob/master/examples/LexStatusCodes.h


def init():
    #status = LexActivator.SetProductFile("ABSOLUTE_PATH_OF_PRODUCT.DAT_FILE")
    status = LexActivator.SetProductData("PASTE_CONTENT_OF_PRODUCT.DAT_FILE")
    if LexActivator.StatusCodes.LA_OK != status:
        print("Error code: ", status)
        sys.exit(status)

    status = LexActivator.SetProductId("PASTE_PRODUCT_ID",
                                       LexActivator.PermissionFlags.LA_USER)
    if LexActivator.StatusCodes.LA_OK != status:
        print("Error code: ", status)
        sys.exit(status)

    status = LexActivator.SetAppVersion("PASTE_YOUR_APP_VERION")
    if LexActivator.StatusCodes.LA_OK != status:
        print("Error code: ", status)
        sys.exit(status)
    return

# License callback is invoked when IsLicenseGenuine() completes a server sync
def licence_callback(status):
    print("License status: ", status)

# reference the callback to keep it alive
licence_callback_fn = LexActivator.CallbackType(licence_callback)

# Software release update callback is invoked when CheckForReleaseUpdate() gets a response from the server
def software_release_update_callback(status):
    print("Release status: ", status)

# reference the callback to keep it alive
software_release_update_callback_fn = LexActivator.CallbackType(software_release_update_callback)

def get_string_buffer(size):
    if sys.platform == 'win32':
        return ctypes.create_unicode_buffer(size)
    else:
        return ctypes.create_string_buffer(size)

def activate():
    status = LexActivator.SetLicenseKey("PASTE_LICENCE_KEY")
    if LexActivator.StatusCodes.LA_OK != status:
        print("Error code: ", status)
        sys.exit(status)

    status = LexActivator.SetActivationMetadata("key1", "value1")
    if LexActivator.StatusCodes.LA_OK != status:
        print("Error code: ", status)
        sys.exit(status)

    status = LexActivator.ActivateLicense()
    if LexActivator.StatusCodes.LA_OK == status | LexActivator.StatusCodes.LA_EXPIRED == status | LexActivator.StatusCodes.LA_SUSPENDED == status:
        print("License activated successfully: ", status)
    else:
        print("License activation failed: ", status)
    return


def activateTrial():
    status = LexActivator.SetTrialActivationMetadata("key1", "value1")
    if LexActivator.StatusCodes.LA_OK != status:
        print("Error code: ", status)
        sys.exit(status)

    status = LexActivator.ActivateTrial()
    if LexActivator.StatusCodes.LA_OK == status:
        print("Product trial activated successfully!")
    elif LexActivator.StatusCodes.LA_TRIAL_EXPIRED == status:
        print("Product trial has expired!")
    else:
        print("Product trial activation failed: ", status)
    return


def main():
    init()
    # Setting license callback is recommended for floating licenses
	# LexActivator.SetLicenseCallback(licence_callback_fn);
    status = LexActivator.IsLicenseGenuine()
    if LexActivator.StatusCodes.LA_OK == status:
        expiryDate = ctypes.c_uint()
        LexActivator.GetLicenseExpiryDate(ctypes.byref(expiryDate))
        daysLeft = (expiryDate.value - time.time()) / 86500
        print("Days left: ", daysLeft)
        bufferSize = 256
        name = get_string_buffer(bufferSize)
        LexActivator.GetLicenseUserName(name, bufferSize)
        print("License user: ", name.value)
        print("License is genuinely activated!")

        print("Checking for software release update...")
        status = LexActivator.CheckForReleaseUpdate("windows", "1.0.0", "stable", software_release_update_callback_fn)
        if LexActivator.StatusCodes.LA_OK != status:
            print("Error checking for software release update:", status)
    elif LexActivator.StatusCodes.LA_EXPIRED == status:
        print("License is genuinely activated but has expired!")
    elif LexActivator.StatusCodes.LA_SUSPENDED == status:
        print("License is genuinely activated but has been suspended!")
    elif LexActivator.StatusCodes.LA_GRACE_PERIOD_OVER == status:
        print("License is genuinely activated but grace period is over!")
    else:
        trialStatus = LexActivator.IsTrialGenuine()
        if LexActivator.StatusCodes.LA_OK == trialStatus:
            trialExpiryDate = ctypes.c_uint()
            LexActivator.GetTrialExpiryDate(ctypes.byref(trialExpiryDate))
            daysLeft = (trialExpiryDate.value - time.time()) / 86500
            print("Trial days left: ", daysLeft)
        elif LexActivator.StatusCodes.LA_TRIAL_EXPIRED == trialStatus:
            print("Trial has expired!")
            # Time to buy the license and activate the app
            activate()
        else:
            print("Either trial has not started or has been tampered: ", trialStatus)
            # Activating the trial
            activateTrial()
        return


main()
