# apply_theme.py

import os
from importlib import import_module


def load_qt_modules():
	try:
		gui = import_module("PySide6.QtGui")
		widgets = import_module("PySide6.QtWidgets")
	except ModuleNotFoundError:
		try:
			gui = import_module("PyQt6.QtGui")
			widgets = import_module("PyQt6.QtWidgets")
		except ModuleNotFoundError as exc:
			raise RuntimeError(
				"PySide6 or PyQt6 is not installed. Install one with `pip install PySide6`."
			) from exc
	return {
		"QPalette": gui.QPalette,
		"QColor": gui.QColor,
		"QApplication": widgets.QApplication
	}

qt = load_qt_modules()
QPalette = qt["QPalette"]
QColor = qt["QColor"]
QApplication = qt["QApplication"]


def apply_theme_to_app(app: QApplication, theme_name: str):
	if theme_name == "Light":
		app.setStyle("Fusion")
		palette = QPalette()
		app.setPalette(palette)
	elif theme_name == "Dark":
		app.setStyle("Fusion")
		palette = QPalette()
		palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
		palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
		palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
		palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
		palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
		palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))
		palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
		palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
		palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
		palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
		palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
		palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
		palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))
		app.setPalette(palette)
	else:
		app.setPalette(app.style().standardPalette())
