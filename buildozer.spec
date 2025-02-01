[app]
title = WizLightsOff
package.name = wizlightsoff
package.domain = com.example
source.dir = .
version = 1.0.0

requirements = python3,kivy,pywizlight,libffi,pyjnius

log_level = 2
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.ndk_path = $ANDROID_NDK_HOME

android.aidl = True
android.build_tools_version = 31.0.0
android.accept_sdk_license = True
