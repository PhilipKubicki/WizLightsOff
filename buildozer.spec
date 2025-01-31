[app]

# (str) Title of your application
title = WizLightsOff

# (str) Package name
package.name = wizlightsoff

# (str) Package domain (needed for android/ios packaging)
package.domain = org.wizlightsoff

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (leave empty to include all)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3==3.11, kivy, pywizlight

# (str) Application versioning
version = 0.1

# (list) Supported orientations (landscape, portrait, etc.)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Android permissions
android.permissions = INTERNET

# (int) Target Android API level (must be 31+ for modern devices)
android.api = 34

# (int) Minimum Android API level
android.minapi = 23

# (str) Android entry point (default for Kivy apps)
android.entrypoint = main.py

# (bool) Enable Android auto backup feature (Android API >=23)
android.allow_backup = True

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable logging for debugging (set to 1 to disable)
android.disable_logging = 0

# (str) Force specific Android SDK build-tools version
android.build_tools_version = 34.0.0

# (str) Force specific Android NDK version
android.ndk = 25.1.8937393

# (bool) Accept Android SDK license automatically
android.accept_sdk_license = True

# (str) Manually specify SDK path
android.sdk_path = $ANDROID_SDK_ROOT

# (str) Package format (apk, aab, etc.)
android.package_format = apk
