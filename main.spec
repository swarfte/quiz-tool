# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=["tool",
    "tool.database",
    "tool.database.DatabaseInterface",
    "tool.database.CsvDatabase",
    "tool.database.JsonDatabase",
    "tool.model",
    "tool.model.ModelInterface",
    "tool.model.BasicModel",
    "tool.controller",
    "tool.controller.ControllerInterface",
    "tool.controller.BasicController",
    "tool.observer",
    "tool.observer.ObserverInterface",
    "tool.view",
    "tool.view.ViewInterface",
    "tool.view.BasicView"],
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
