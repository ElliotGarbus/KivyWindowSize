# -*- mode: python -*-

block_cipher = None
from kivy.tools.packaging.pyinstaller_hooks import get_deps_all, hookspath, runtime_hooks

a = Analysis(['../main.py'],
             pathex=['../KivyWindowSizeDist'],
             binaries=[],
             datas=[],
             # hiddenimports=[],
             hookspath=hookspath(),
             runtime_hooks=runtime_hooks(),
             # excludes=['_tkinter', 'Tkinter', 'enchant', 'twisted'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False,
             **get_deps_all())

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='KWS',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False )
coll = COLLECT(exe, Tree('../', excludes=['.git', 'screenshots', 'KivyWindowSizeDist','__pycache__','.idea','*.bat']),
               Tree('/Library/Frameworks/SDL2_ttf.framework/Versions/A/Frameworks/FreeType.framework'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='KWS')
app = BUNDLE(coll,
             name='KWS.app',
             icon='',
             bundle_identifier=None,
              )
