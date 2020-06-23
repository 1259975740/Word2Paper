# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Tab1.py'],
             pathex=['E:\\java-2020-03\\eclipse\\workspace\\Word2write\\GUI'],
             binaries=[],
             datas=[],
             hiddenimports=['docx'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Tab1',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='app.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Tab1')
