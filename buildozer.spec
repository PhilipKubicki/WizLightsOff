[app]
title = WizLightsOff
package.name = wizlightsoff
package.domain = com.example
source.dir = .
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,pywizlight,libffi,pyjnius

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions needed for your app
android.permissions = INTERNET

# (str) Supported orientations (one of landscape, sensorLandscape, portrait or all)
android.orientation = portrait

# (bool) Enable or disable the compilation of the PyQt provider
android.allow_ndk = True

# (str) Package format to build for (one of: "armeabi-v7a", "arm64-v8a", "x86", "x86_64", or "all")
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# API level to target
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.ndk_path = $ANDROID_NDK_HOME

# (bool) Enable AIDL
android.aidl = True

# (str) Specify the build tools version
android.build_tools_version = 31.0.0

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True
