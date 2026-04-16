[app]
title = D7 Miner
package.name = d7miner
package.domain = org.muminovic
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.0
requirements = python3,kivy

# (Nujno za Android)
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
