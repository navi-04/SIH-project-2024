import ctypes

# Load the MFS100 DLL (ensure the path is correct and the file exists)
mfs100_dll = ctypes.WinDLL(r"C:\Program Files\Mantra\MFS100\Driver\Driver\Win-10-X64\MFS100CI.dll")

# Initialize the sensor (assuming the function exists in the DLL)
try:
    # Check if Init function exists
    if hasattr(mfs100_dll, '_Init@12'):
        # Define Init function's argument and return types
        mfs100_dll.Init.argtypes = []
        mfs100_dll.Init.restype = ctypes.c_int

        # Call Init function
        init_sensor = mfs100_dll._Init@12()
        if init_sensor != 0:
            print("Failed to initialize the sensor")
        else:
            print("Sensor initialized successfully")
    else:
        print("Init function not found in DLL")
        exit(1)

    # Capture fingerprint function (assuming CaptureFingerprint exists)
    if hasattr(mfs100_dll, 'CaptureFingerprint'):
        mfs100_dll.CaptureFingerprint.argtypes = []
        mfs100_dll.CaptureFingerprint.restype = ctypes.c_int

        # Call CaptureFingerprint function
        capture_fingerprint = mfs100_dll.CaptureFingerprint()
        if capture_fingerprint != 0:
            print("Failed to capture fingerprint")
        else:
            print("Fingerprint captured successfully")
    else:
        print("CaptureFingerprint function not found in DLL")
        exit(1)

    # Get fingerprint data (assuming GetFingerprintData exists)
    if hasattr(mfs100_dll, 'GetFingerprintData'):
        # Create a buffer to store the fingerprint data (adjust the buffer size as needed)
        data = ctypes.create_string_buffer(1024)

        # Define argument and return types for GetFingerprintData
        mfs100_dll.GetFingerprintData.argtypes = [ctypes.c_char_p]
        mfs100_dll.GetFingerprintData.restype = ctypes.c_int

        # Call GetFingerprintData function
        get_data = mfs100_dll.GetFingerprintData(data)
        if get_data == 0:
            print("Fingerprint data retrieved successfully")
            # Save fingerprint data to a file
            with open("fingerprint_data.bin", "wb") as f:
                f.write(data.raw)
        else:
            print("Failed to retrieve fingerprint data")
    else:
        print("GetFingerprintData function not found in DLL")

except Exception as e:
    print(f"An error occurred: {e}")
