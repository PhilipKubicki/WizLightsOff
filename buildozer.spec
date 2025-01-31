[app]
title = WizLightsOff
package.name = wizlightsoff
package.domain = org.kivy
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pywizlight
orientation = portrait
fullscreen = 0
android.arch = arm64-v8a,armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1

[app]
package.domain = com.yourdomain
package.name = wizlightsoff
package.version = 1.0
package.org = org.kivy

[android]
android.api = 34
android.minapi = 21
android.ndk = 25.1.8937393
android.accept_sdk_license = True
android.build_tools_version = 33.0.2
android.sdk = 34
android.ndk_api = 21
android.archs = arm64-v8a,armeabi-v7a
android.gradle_dependencies = 

[buildozer]
android.p4a_dir = $HOME/.buildozer/android/platform/python-for-android
