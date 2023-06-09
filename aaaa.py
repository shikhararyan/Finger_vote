import pyfingerprint
from pyfingerprint.pyfingerprint import PyFingerprint


def verify_fingerprint(aadhar_number):
    try:
        # Initialize the fingerprint scanner
        f = PyFingerprint('Port_#0001.Hub_#0001', 57600, 0xFFFFFFFF, 0x00000000)

        # Check if the fingerprint sensor is connected and accessible
        if not f.verifyPassword():
            raise ValueError('The fingerprint sensor could not be accessed.')

        # Get the fingerprint template stored in the database for the given Aadhar number
        template_id = get_fingerprint_template_id(aadhar_number)
        if template_id is None:
            print('No fingerprint template found for the given Aadhar number.')
            return False

        # Wait for the finger to be placed on the sensor
        print('Place your finger on the fingerprint scanner...')
        while not f.readImage():
            pass

        # Convert the fingerprint image to characteristics
        f.convertImage(0x01)

        # Search for a matching fingerprint template
        result = f.searchTemplate()
        if result == template_id:
            print('Fingerprint matched. Voter verified.')
            return True
        else:
            print('Fingerprint did not match. Voter not verified.')
            return False

    except Exception as e:
        print('An error occurred while verifying the fingerprint:', str(e))
        return False

verify_fingerprint("1224")
