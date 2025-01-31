[app]
title = WizLightsOff
package.name = wizlightsoff
package.domain = com.example
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3, kivy, pywizlight
orientation = portrait
fullscreen = 0
android.api = 34
android.minapi = 21
android.ndk_api = 21
android.sdk = 34
p4a.fallback_sdk_version = 34
p4a.fallback_ndk_version = 25.1.8937393
android.build_tools_version = 34.0.0
android.archs = arm64-v8a, armeabi-v7a
android.gradle_dependencies = 'com.android.support:multidex:1.0.3'
android.ndk = 25.1.8937393
android.private_storage = True
android.permissions = INTERNET
android.allow_backup = False
p4a.branch = master
p4a.bootstrap = sdl2
android.manifest_intent_filters = 
    <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
    </intent-filter>
android.presplash_color = #000000
android.logcat_filters = *:S python:D
