import sys
import time

from cryptlex.lexactivator import LexActivator, LexStatusCodes, PermissionFlags, ReleaseFlags, LexActivatorException
# from cryptlex.lexactivator import *


def init():
    LexActivator.SetProductData("PASTE_CONTENT_OF_PRODUCT.DAT_FILE")
    LexActivator.SetProductId("PASTE_PRODUCT_ID", PermissionFlags.LA_USER)
    LexActivator.SetReleasePlatform('RELEASE_PLATFORM') # set the actual platform of the release e.g windows
    LexActivator.SetReleaseChannel('RELEASE_CHANNEL') # set the actual channel of the release e.g stable
    LexActivator.SetReleaseVersion("1.0.0") # Set this to the release version of your app

# License callback is invoked when IsLicenseGenuine() completes a server sync


def licence_callback(status):
    print("License status: ", status)

# Software release update callback is invoked when CheckForReleaseUpdate() gets a response from the server


def software_release_update_callback(status, release, user_data):
    try:
        if status == LexStatusCodes.LA_RELEASE_UPDATE_AVAILABLE:
            print('Release update available!')
            print('Release notes: ', release.notes)
        elif status == LexStatusCodes.LA_RELEASE_UPDATE_AVAILABLE_NOT_ALLOWED:
            print('Release update available but not allowed!')
            print('Release notes: ', release.notes)
        elif status == LexStatusCodes.LA_RELEASE_NO_UPDATE_AVAILABLE:
            print('No release update available.')
    except LexActivatorException as exception:
        print('Error code:', exception.code, exception.message)


def activate():
    LexActivator.SetLicenseKey("PASTE_LICENCE_KEY")
    LexActivator.SetActivationMetadata("key1", "value1")
    status = LexActivator.ActivateLicense()
    if LexStatusCodes.LA_OK == status or LexStatusCodes.LA_EXPIRED == status or LexStatusCodes.LA_SUSPENDED == status:
        print("License activated successfully: ", status)
    else:
        print("License activation failed: ", status)


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
            # LexActivator.CheckReleaseUpdate(software_release_update_callback, ReleaseFlags.LA_RELEASES_ALL, None)
        elif LexStatusCodes.LA_EXPIRED == status:
            print("License is genuinely activated but has expired!")
        elif LexStatusCodes.LA_SUSPENDED == status:
            print("License is genuinely activated but has been suspended!")
        elif LexStatusCodes.LA_GRACE_PERIOD_OVER == status:
            print("License is genuinely activated but grace period is over!")
        else:
            trialStatus = LexActivator.IsTrialGenuine()
            if LexStatusCodes.LA_OK == trialStatus:
                trialExpiryDate = LexActivator.GetTrialExpiryDate()
                daysLeft = (trialExpiryDate - time.time()) / 86400
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
        print('Error code:', exception.code, exception.message)


main()
input("Press Enter to continue...")
