[app]
title = WizLightsOff
package.name = wizlightsoff
package.domain = com.yourdomain
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pywizlight
orientation = portrait
fullscreen = 0
android.api = 34
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.gradle_dependencies = 
android.ndk = 25.1.8937393
android.build_tools_version = 34.0.0
android.sdk = 34
android.permissions = INTERNET
android.allow_cleartext_default = False
android.logcat_filters = *:S python:D
p4a.branch = master
p4a.bootstrap = sdl2
p4a.source_dir = 
p4a.local_recipes = 
p4a.python_version = 3
p4a.fallback_sdk_version = 34
p4a.fallback_ndk_version = 25.1.8937393
android.ndk_dir = $ANDROID_NDK_HOME
android.sdk_dir = $ANDROID_SDK_ROOT
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = .buildozer
bin_dir = bin
