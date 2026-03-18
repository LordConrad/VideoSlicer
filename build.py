import PyInstaller.__main__
import sys

# Definice společných parametrů pro PyInstaller pro obě platformy
common_args = [
    'main.py',
    '--name=VideoSlicer',
    '--windowed',                  # Vypne konzolové okno aplikace za chodem (Důležité pro GUI Qt)
    '--noconfirm',                 # Při sestavování rovnou potvrdí přepsání minulé verze
    '--clean',
    '--hidden-import=PySide6.QtCore',
    '--hidden-import=PySide6.QtGui',
    '--hidden-import=PySide6.QtWidgets',
    '--hidden-import=PySide6.QtMultimedia',
    '--hidden-import=PySide6.QtMultimediaWidgets',
    '--add-data=icon.png:.'
]

if sys.platform.startswith('linux'):
    print("Spouštím build pro Linux...")
    linux_args = common_args + [
        '--onefile'                  # Vytvoří jenom jeden spustitelný .AppImage/Soubor
    ]   
    PyInstaller.__main__.run(linux_args)
    
elif sys.platform.startswith('win'):
    print("Spouštím build pro Windows...")
    windows_args = common_args + [
        '--onefile',                 # Použijeme onefile i na Windows, aby uživatelé nezkopírovali jen .exe bez složky _internal
        '--icon=icon.png' 
    ]
    PyInstaller.__main__.run(windows_args)
    
else:
    print(f"Nepodporovaný systém pro automatický build: {sys.platform}")
