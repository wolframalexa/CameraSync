// NEW VARIABLE
HANDLE depthStream;

bool initKinect() {
    // Get a working kinect sensor
    int numSensors;
    if (NuiGetSensorCount(&numSensors) < 0 || numSensors < 1) return false;
    if (NuiCreateSensorByIndex(0, &sensor) < 0) return false;

    // Initialize sensor
    sensor->NuiInitialize(NUI_INITIALIZE_FLAG_USES_DEPTH | NUI_INITIALIZE_FLAG_USES_COLOR);

        // --------------- START CHANGED CODE -----------------
    sensor->NuiImageStreamOpen(
        NUI_IMAGE_TYPE_DEPTH,                     // Depth camera or rgb camera?
        NUI_IMAGE_RESOLUTION_640x480,             // Image resolution
        NUI_IMAGE_STREAM_FLAG_ENABLE_NEAR_MODE,   // Image stream flags, e.g. near mode
        2,      // Number of frames to buffer
        NULL,   // Event handle
        &depthStream);
        // --------------- END CHANGED CODE -----------------
    return sensor;
}



const USHORT* curr = (const USHORT*) LockedRect.pBits;
        const USHORT* dataEnd = curr + (width*height);

        while (curr < dataEnd) {
            // Get depth in millimeters
            USHORT depth = NuiDepthPixelToDepth(*curr++);

            // Draw a grayscale image of the depth:
            // B,G,R are all set to depth%256, alpha set to 1.
            for (int i = 0; i < 3; ++i)
                *dest++ = (BYTE) depth%256;
            *dest++ = 0xff;
        }
