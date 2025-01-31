[app]
title = WizLightsOff
package.name = wizlightsoff
package.domain = org.example
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pywizlight
orientation = portrait
fullscreen = 0
source.exclude_exts = spec
source.exclude_dirs = tests
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 34
android.minapi = 21
android.ndk = 25.1.8937393
android.gradle_dependencies = "org.python:jython-standalone:2.7.2"
android.bootstrap = sdl2
android.archs = arm64-v8a armeabi-v7a
android.allow_presplash_rotation = False
android.build_tools_version = 34.0.0
