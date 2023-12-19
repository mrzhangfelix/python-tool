# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['UI.py'],
             pathex=['C:\\Users\\felix\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2',
             'D:\\code\\python-tool\\yys\\client'],
             binaries=[],
             datas=[('img1280','img1280')],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='UI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
