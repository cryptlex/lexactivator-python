import sys, ctypes, time
import grequests


from cryptlex.lexactivator import LexActivator, LexStatusCodes, PermissionFlags, LexActivatorException
# from cryptlex.lexactivator import *

def init():
    #status = LexActivator.SetProductFile("ABSOLUTE_PATH_OF_PRODUCT.DAT_FILE")
    LexActivator.SetProductData("PASTE_CONTENT_OF_PRODUCT.DAT_FILE")
    LexActivator.SetProductId("PASTE_PRODUCT_ID", PermissionFlags.LA_USER)
    LexActivator.SetAppVersion("PASTE_YOUR_APP_VERION")

# License callback is invoked when IsLicenseGenuine() completes a server sync
def licence_callback(status):
    print("License status: ", status)

# Software release update callback is invoked when CheckForReleaseUpdate() gets a response from the server
def software_release_update_callback(status):
    print("Release status: ", status)

def activate():
    LexActivator.SetLicenseKey("PASTE_LICENCE_KEY")
    LexActivator.SetActivationMetadata("key1", "value1")
    status = LexActivator.ActivateLicense()
    if LexStatusCodes.LA_OK == status or LexStatusCodes.LA_EXPIRED == status or LexStatusCodes.LA_SUSPENDED == status:
        print("License activated successfully: ", status)
    else:
        print("License activation failed: ", status, LexStatusCodes.LA_OK)


def activateTrial():
    LexActivator.SetTrialActivationMetadata("key1", "value1")
    status = LexActivator.ActivateTrial()
    if LexStatusCodes.LA_OK == status:
        print("Product trial activated successfully!")
    elif LexStatusCodes.LA_TRIAL_EXPIRED == status:
        print("Product trial has expired!")
    else:
        print("Product trial activation failed: ", status)
    

def main():
    try:
        init()
        # activate()
        # Setting license callback is recommended for floating licenses
        LexActivator.SetLicenseCallback(licence_callback)
        status = LexActivator.IsLicenseGenuine()
        if LexStatusCodes.LA_OK == status:
            expiryDate = LexActivator.GetLicenseExpiryDate()
            daysLeft = (expiryDate - time.time()) / 86400
            print("Days left: ", daysLeft)
            username = LexActivator.GetLicenseUserName()
            print("License user: ", username)
            print("License is genuinely activated!")

            # print("Checking for software release update...")
            # LexActivator.CheckForReleaseUpdate("windows", "1.0.0", "stable", software_release_update_callback)
        elif LexStatusCodes.LA_EXPIRED == status:
            print("License is genuinely activated but has expired!")
        elif LexStatusCodes.LA_SUSPENDED == status:
            print("License is genuinely activated but has been suspended!")
        elif LexStatusCodes.LA_GRACE_PERIOD_OVER == status:
            print("License is genuinely activated but grace period is over!")
        else:
            trialStatus = LexActivator.IsTrialGenuine()
            if LexStatusCodes.LA_OK == trialStatus:
                trialExpiryDate = ctypes.c_uint()
                LexActivator.GetTrialExpiryDate(ctypes.byref(trialExpiryDate))
                daysLeft = (trialExpiryDate.value - time.time()) / 86400
                print("Trial days left: ", daysLeft)
            elif LexStatusCodes.LA_TRIAL_EXPIRED == trialStatus:
                print("Trial has expired!")
                # Time to buy the license and activate the app
                activate()
            else:
                print("Either trial has not started or has been tampered: ", trialStatus)
                # Activating the trial
                activateTrial()
    except LexActivatorException as exception:
        print('Error code:',exception.code, exception.message)

main()
input("Press Enter to continue...")
