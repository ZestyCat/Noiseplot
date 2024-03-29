# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('./img/drop.png', './img/'), ('./img/file.png', './img/'), ('./img/go.png', './img/'), ('./img/tabs.png', './img/'), ('./img/del.png', './img/'), ('./img/aeso_padded.png', './img/'), ('./data/operation_data.csv', './data/'), ('./omega/Omega10.exe', './omega'), ('./omega/Flight01.dat', './omega'), ('./omega/Omega11.exe', './omega'), ('./omega/Static01.dat', './omega')],
    hiddenimports=[],
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
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
