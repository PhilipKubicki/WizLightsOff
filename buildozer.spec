[app]
title = WizLightsOff
package.name = wizlightsoff
package.domain = com.example
source.dir = .
version = 1.0.0  # Required version field

# Ensure the correct Python version is used
requirements = python3,kivy,pywizlight,libffi,pyjnius

# Enable logcat debugging for troubleshooting
log_level = 2
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# Specify API level and platform versions
android.api = 31
android.minapi = 21
android.ndk = 23b
android.sdk = 27
android.ndk_path = $ANDROID_NDK_HOME

# Ensure AIDL is installed
android.aidl = True

# Ensure build tools are present
android.build_tools_version = 30.0.3

# Permissions
android.permissions = INTERNET

# Set orientation
android.orientation = portrait
