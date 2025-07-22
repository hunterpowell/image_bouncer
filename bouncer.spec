# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['bouncer.py'],
    pathex=[],
    binaries=[],
    datas=[('taco_baco.mp3', '.')],  # Add the mp3 file to the root of the exe
    hiddenimports=['playsound3'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='bouncer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Set to True to show console window for debugging
    disable_windowed_traceback=False,
    icon=None,  # Add icon='icon.ico' if you have an icon file
    onefile=True,  # This creates a single executable file
)