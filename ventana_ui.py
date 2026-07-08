# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet(u"\n"
"    QMainWindow { background-color: #1a1a2e; }\n"
"    QLabel { color: white; }\n"
"    QGroupBox {\n"
"        color: white;\n"
"        border: 2px solid #16213e;\n"
"        border-radius: 10px;\n"
"        margin-top: 10px;\n"
"        font-weight: bold;\n"
"    }\n"
"    QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 10px;\n"
"        padding: 0 5px 0 5px;\n"
"    }\n"
"    QPushButton {\n"
"        background-color: #0f3460;\n"
"        color: white;\n"
"        border: none;\n"
"        padding: 8px 16px;\n"
"        border-radius: 8px;\n"
"        font-weight: bold;\n"
"    }\n"
"    QPushButton:hover { background-color: #0a2647; }\n"
"    QLineEdit, QTextEdit, QComboBox, QSpinBox {\n"
"        background-color: #0f3460;\n"
"        border: 2px solid #16213e;\n"
"        border-radius: 8px;\n"
"        padding: 8px;\n"
"        color: white;\n"
"    }\n"
"    QLineEdit:focus, QTextEdit:focus, QComboBox:focus {\n"
"        border-color: #e94560;\n"
"    }\n"
"   ")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionAcercaDe = QAction(MainWindow)
        self.actionAcercaDe.setObjectName(u"actionAcercaDe")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"\n"
"        QTabWidget::pane {\n"
"            border: 2px solid #16213e;\n"
"            border-radius: 10px;\n"
"            background-color: #1a1a2e;\n"
"        }\n"
"        QTabBar::tab {\n"
"            background-color: #16213e;\n"
"            color: white;\n"
"            padding: 10px 20px;\n"
"            margin: 5px;\n"
"            border-radius: 10px;\n"
"            font-weight: bold;\n"
"        }\n"
"        QTabBar::tab:selected { background-color: #e94560; }\n"
"        QTabBar::tab:hover { background-color: #0f3460; }\n"
"       ")
        self.tabGrabadora = QWidget()
        self.tabGrabadora.setObjectName(u"tabGrabadora")
        self.verticalLayout_2 = QVBoxLayout(self.tabGrabadora)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelGrabadora = QLabel(self.tabGrabadora)
        self.labelGrabadora.setObjectName(u"labelGrabadora")
        self.labelGrabadora.setStyleSheet(u"font-size: 24px; font-weight: bold; color: #e94560;")
        self.labelGrabadora.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelGrabadora)

        self.horizontalLayoutGrabadora = QHBoxLayout()
        self.horizontalLayoutGrabadora.setObjectName(u"horizontalLayoutGrabadora")
        self.btnGrabar = QPushButton(self.tabGrabadora)
        self.btnGrabar.setObjectName(u"btnGrabar")
        self.btnGrabar.setCheckable(True)
        self.btnGrabar.setStyleSheet(u"\n"
"              QPushButton {\n"
"                  background-color: #e94560;\n"
"                  color: white;\n"
"                  border: none;\n"
"                  padding: 15px 30px;\n"
"                  border-radius: 30px;\n"
"                  font-size: 16px;\n"
"                  font-weight: bold;\n"
"              }\n"
"              QPushButton:hover { background-color: #c73e54; }\n"
"              QPushButton:checked { background-color: #533483; }\n"
"             ")

        self.horizontalLayoutGrabadora.addWidget(self.btnGrabar)

        self.btnDetenerGrabacion = QPushButton(self.tabGrabadora)
        self.btnDetenerGrabacion.setObjectName(u"btnDetenerGrabacion")
        self.btnDetenerGrabacion.setStyleSheet(u"\n"
"              QPushButton {\n"
"                  background-color: #533483;\n"
"                  color: white;\n"
"                  border: none;\n"
"                  padding: 15px 30px;\n"
"                  border-radius: 30px;\n"
"                  font-size: 16px;\n"
"                  font-weight: bold;\n"
"              }\n"
"              QPushButton:hover { background-color: #3d2766; }\n"
"             ")

        self.horizontalLayoutGrabadora.addWidget(self.btnDetenerGrabacion)


        self.verticalLayout_2.addLayout(self.horizontalLayoutGrabadora)

        self.frameVisualizador = QFrame(self.tabGrabadora)
        self.frameVisualizador.setObjectName(u"frameVisualizador")
        self.frameVisualizador.setMinimumSize(QSize(0, 150))
        self.frameVisualizador.setStyleSheet(u"\n"
"            QFrame {\n"
"                background-color: #1a1a2e;\n"
"                border-radius: 10px;\n"
"                border: 2px solid #16213e;\n"
"            }\n"
"           ")
        self.frameVisualizador.setFrameShape(QFrame.StyledPanel)
        self.frameVisualizador.setFrameShadow(QFrame.Raised)
        self.labelVisualizador = QLabel(self.frameVisualizador)
        self.labelVisualizador.setObjectName(u"labelVisualizador")
        self.labelVisualizador.setGeometry(QRect(450, 50, 151, 41))
        self.labelVisualizador.setStyleSheet(u"color: #888; font-size: 14px;")

        self.verticalLayout_2.addWidget(self.frameVisualizador)

        self.labelEstadoGrabacion = QLabel(self.tabGrabadora)
        self.labelEstadoGrabacion.setObjectName(u"labelEstadoGrabacion")
        self.labelEstadoGrabacion.setStyleSheet(u"color: #888; font-size: 14px;")

        self.verticalLayout_2.addWidget(self.labelEstadoGrabacion)

        self.groupGrabaciones = QGroupBox(self.tabGrabadora)
        self.groupGrabaciones.setObjectName(u"groupGrabaciones")
        self.groupGrabaciones.setStyleSheet(u"\n"
"            QGroupBox {\n"
"                font-weight: bold;\n"
"                border: 2px solid #16213e;\n"
"                border-radius: 10px;\n"
"                margin-top: 10px;\n"
"            }\n"
"            QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                left: 10px;\n"
"                padding: 0 5px 0 5px;\n"
"            }\n"
"           ")
        self.verticalLayout_3 = QVBoxLayout(self.groupGrabaciones)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listGrabaciones = QListWidget(self.groupGrabaciones)
        QListWidgetItem(self.listGrabaciones)
        QListWidgetItem(self.listGrabaciones)
        QListWidgetItem(self.listGrabaciones)
        QListWidgetItem(self.listGrabaciones)
        QListWidgetItem(self.listGrabaciones)
        self.listGrabaciones.setObjectName(u"listGrabaciones")
        self.listGrabaciones.setStyleSheet(u"\n"
"               QListWidget {\n"
"                   background-color: #0f3460;\n"
"                   border: 1px solid #16213e;\n"
"                   border-radius: 5px;\n"
"                   color: white;\n"
"               }\n"
"               QListWidget::item:selected { background-color: #e94560; }\n"
"              ")

        self.verticalLayout_3.addWidget(self.listGrabaciones)

        self.horizontalLayoutBotonesGrabacion = QHBoxLayout()
        self.horizontalLayoutBotonesGrabacion.setObjectName(u"horizontalLayoutBotonesGrabacion")
        self.btnReproducirGrabacion = QPushButton(self.groupGrabaciones)
        self.btnReproducirGrabacion.setObjectName(u"btnReproducirGrabacion")

        self.horizontalLayoutBotonesGrabacion.addWidget(self.btnReproducirGrabacion)

        self.btnEliminarGrabacion = QPushButton(self.groupGrabaciones)
        self.btnEliminarGrabacion.setObjectName(u"btnEliminarGrabacion")

        self.horizontalLayoutBotonesGrabacion.addWidget(self.btnEliminarGrabacion)


        self.verticalLayout_3.addLayout(self.horizontalLayoutBotonesGrabacion)


        self.verticalLayout_2.addWidget(self.groupGrabaciones)

        self.tabWidget.addTab(self.tabGrabadora, "")
        self.tabVisualizacion = QWidget()
        self.tabVisualizacion.setObjectName(u"tabVisualizacion")
        self.verticalLayout_4 = QVBoxLayout(self.tabVisualizacion)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelVisualizacion = QLabel(self.tabVisualizacion)
        self.labelVisualizacion.setObjectName(u"labelVisualizacion")
        self.labelVisualizacion.setStyleSheet(u"font-size: 24px; font-weight: bold; color: #e94560;")
        self.labelVisualizacion.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelVisualizacion)

        self.frameVisualizadorGrande = QFrame(self.tabVisualizacion)
        self.frameVisualizadorGrande.setObjectName(u"frameVisualizadorGrande")
        self.frameVisualizadorGrande.setMinimumSize(QSize(0, 300))
        self.frameVisualizadorGrande.setStyleSheet(u"\n"
"            QFrame {\n"
"                background-color: #1a1a2e;\n"
"                border-radius: 10px;\n"
"                border: 2px solid #16213e;\n"
"            }\n"
"           ")
        self.frameVisualizadorGrande.setFrameShape(QFrame.StyledPanel)
        self.frameVisualizadorGrande.setFrameShadow(QFrame.Raised)
        self.labelVisualizadorGrande = QLabel(self.frameVisualizadorGrande)
        self.labelVisualizadorGrande.setObjectName(u"labelVisualizadorGrande")
        self.labelVisualizadorGrande.setGeometry(QRect(450, 130, 151, 41))
        self.labelVisualizadorGrande.setStyleSheet(u"color: #888; font-size: 14px;")

        self.verticalLayout_4.addWidget(self.frameVisualizadorGrande)

        self.horizontalLayoutVisualizacion = QHBoxLayout()
        self.horizontalLayoutVisualizacion.setObjectName(u"horizontalLayoutVisualizacion")
        self.btnCargarAudio = QPushButton(self.tabVisualizacion)
        self.btnCargarAudio.setObjectName(u"btnCargarAudio")

        self.horizontalLayoutVisualizacion.addWidget(self.btnCargarAudio)

        self.btnReproducirVisualizacion = QPushButton(self.tabVisualizacion)
        self.btnReproducirVisualizacion.setObjectName(u"btnReproducirVisualizacion")

        self.horizontalLayoutVisualizacion.addWidget(self.btnReproducirVisualizacion)

        self.btnDetenerVisualizacion = QPushButton(self.tabVisualizacion)
        self.btnDetenerVisualizacion.setObjectName(u"btnDetenerVisualizacion")

        self.horizontalLayoutVisualizacion.addWidget(self.btnDetenerVisualizacion)


        self.verticalLayout_4.addLayout(self.horizontalLayoutVisualizacion)

        self.groupInfoAudio = QGroupBox(self.tabVisualizacion)
        self.groupInfoAudio.setObjectName(u"groupInfoAudio")
        self.verticalLayout_5 = QVBoxLayout(self.groupInfoAudio)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.labelInfoArchivo = QLabel(self.groupInfoAudio)
        self.labelInfoArchivo.setObjectName(u"labelInfoArchivo")

        self.verticalLayout_5.addWidget(self.labelInfoArchivo)

        self.labelDuracion = QLabel(self.groupInfoAudio)
        self.labelDuracion.setObjectName(u"labelDuracion")

        self.verticalLayout_5.addWidget(self.labelDuracion)

        self.labelFormato = QLabel(self.groupInfoAudio)
        self.labelFormato.setObjectName(u"labelFormato")

        self.verticalLayout_5.addWidget(self.labelFormato)


        self.verticalLayout_4.addWidget(self.groupInfoAudio)

        self.tabWidget.addTab(self.tabVisualizacion, "")
        self.tabDescargar = QWidget()
        self.tabDescargar.setObjectName(u"tabDescargar")
        self.verticalLayout_6 = QVBoxLayout(self.tabDescargar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.labelDescargar = QLabel(self.tabDescargar)
        self.labelDescargar.setObjectName(u"labelDescargar")
        self.labelDescargar.setStyleSheet(u"font-size: 24px; font-weight: bold; color: #e94560;")
        self.labelDescargar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.labelDescargar)

        self.horizontalLayoutURL = QHBoxLayout()
        self.horizontalLayoutURL.setObjectName(u"horizontalLayoutURL")
        self.labelURL = QLabel(self.tabDescargar)
        self.labelURL.setObjectName(u"labelURL")
        self.labelURL.setStyleSheet(u"font-size: 14px;")

        self.horizontalLayoutURL.addWidget(self.labelURL)

        self.lineURL = QLineEdit(self.tabDescargar)
        self.lineURL.setObjectName(u"lineURL")
        self.lineURL.setStyleSheet(u"\n"
"              QLineEdit {\n"
"                  background-color: #0f3460;\n"
"                  border: 2px solid #16213e;\n"
"                  border-radius: 10px;\n"
"                  padding: 10px;\n"
"                  color: white;\n"
"                  font-size: 14px;\n"
"              }\n"
"              QLineEdit:focus { border-color: #e94560; }\n"
"             ")

        self.horizontalLayoutURL.addWidget(self.lineURL)


        self.verticalLayout_6.addLayout(self.horizontalLayoutURL)

        self.horizontalLayoutCalidad = QHBoxLayout()
        self.horizontalLayoutCalidad.setObjectName(u"horizontalLayoutCalidad")
        self.labelCalidad = QLabel(self.tabDescargar)
        self.labelCalidad.setObjectName(u"labelCalidad")

        self.horizontalLayoutCalidad.addWidget(self.labelCalidad)

        self.comboCalidad = QComboBox(self.tabDescargar)
        self.comboCalidad.addItem("")
        self.comboCalidad.addItem("")
        self.comboCalidad.addItem("")
        self.comboCalidad.setObjectName(u"comboCalidad")

        self.horizontalLayoutCalidad.addWidget(self.comboCalidad)


        self.verticalLayout_6.addLayout(self.horizontalLayoutCalidad)

        self.btnDescargar = QPushButton(self.tabDescargar)
        self.btnDescargar.setObjectName(u"btnDescargar")
        self.btnDescargar.setStyleSheet(u"\n"
"            QPushButton {\n"
"                background-color: #e94560;\n"
"                color: white;\n"
"                border: none;\n"
"                padding: 15px;\n"
"                border-radius: 15px;\n"
"                font-size: 16px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover { background-color: #c73e54; }\n"
"           ")

        self.verticalLayout_6.addWidget(self.btnDescargar)

        self.progressDescarga = QProgressBar(self.tabDescargar)
        self.progressDescarga.setObjectName(u"progressDescarga")
        self.progressDescarga.setValue(0)
        self.progressDescarga.setStyleSheet(u"\n"
"            QProgressBar {\n"
"                border: 2px solid #16213e;\n"
"                border-radius: 10px;\n"
"                background-color: #0f3460;\n"
"                height: 30px;\n"
"            }\n"
"            QProgressBar::chunk {\n"
"                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                    stop:0 #e94560, stop:1 #533483);\n"
"                border-radius: 10px;\n"
"            }\n"
"           ")

        self.verticalLayout_6.addWidget(self.progressDescarga)

        self.labelEstadoDescarga = QLabel(self.tabDescargar)
        self.labelEstadoDescarga.setObjectName(u"labelEstadoDescarga")
        self.labelEstadoDescarga.setStyleSheet(u"color: #888; font-size: 14px;")

        self.verticalLayout_6.addWidget(self.labelEstadoDescarga)

        self.groupDescargas = QGroupBox(self.tabDescargar)
        self.groupDescargas.setObjectName(u"groupDescargas")
        self.verticalLayout_7 = QVBoxLayout(self.groupDescargas)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.listDescargas = QListWidget(self.groupDescargas)
        QListWidgetItem(self.listDescargas)
        QListWidgetItem(self.listDescargas)
        QListWidgetItem(self.listDescargas)
        QListWidgetItem(self.listDescargas)
        QListWidgetItem(self.listDescargas)
        self.listDescargas.setObjectName(u"listDescargas")

        self.verticalLayout_7.addWidget(self.listDescargas)


        self.verticalLayout_6.addWidget(self.groupDescargas)

        self.tabWidget.addTab(self.tabDescargar, "")
        self.tabExtractor = QWidget()
        self.tabExtractor.setObjectName(u"tabExtractor")
        self.verticalLayout_8 = QVBoxLayout(self.tabExtractor)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelExtractor = QLabel(self.tabExtractor)
        self.labelExtractor.setObjectName(u"labelExtractor")
        self.labelExtractor.setStyleSheet(u"font-size: 24px; font-weight: bold; color: #e94560;")
        self.labelExtractor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.labelExtractor)

        self.horizontalLayoutArchivo = QHBoxLayout()
        self.horizontalLayoutArchivo.setObjectName(u"horizontalLayoutArchivo")
        self.labelArchivoSeleccionado = QLabel(self.tabExtractor)
        self.labelArchivoSeleccionado.setObjectName(u"labelArchivoSeleccionado")
        self.labelArchivoSeleccionado.setStyleSheet(u"color: #888; font-size: 14px;")

        self.horizontalLayoutArchivo.addWidget(self.labelArchivoSeleccionado)

        self.btnSeleccionarMP4 = QPushButton(self.tabExtractor)
        self.btnSeleccionarMP4.setObjectName(u"btnSeleccionarMP4")

        self.horizontalLayoutArchivo.addWidget(self.btnSeleccionarMP4)


        self.verticalLayout_8.addLayout(self.horizontalLayoutArchivo)

        self.horizontalLayoutBitrate = QHBoxLayout()
        self.horizontalLayoutBitrate.setObjectName(u"horizontalLayoutBitrate")
        self.labelBitrate = QLabel(self.tabExtractor)
        self.labelBitrate.setObjectName(u"labelBitrate")

        self.horizontalLayoutBitrate.addWidget(self.labelBitrate)

        self.comboBitrate = QComboBox(self.tabExtractor)
        self.comboBitrate.addItem("")
        self.comboBitrate.addItem("")
        self.comboBitrate.addItem("")
        self.comboBitrate.setObjectName(u"comboBitrate")

        self.horizontalLayoutBitrate.addWidget(self.comboBitrate)


        self.verticalLayout_8.addLayout(self.horizontalLayoutBitrate)

        self.btnExtraerMP3 = QPushButton(self.tabExtractor)
        self.btnExtraerMP3.setObjectName(u"btnExtraerMP3")
        self.btnExtraerMP3.setStyleSheet(u"\n"
"            QPushButton {\n"
"                background-color: #e94560;\n"
"                color: white;\n"
"                border: none;\n"
"                padding: 15px;\n"
"                border-radius: 15px;\n"
"                font-size: 16px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover { background-color: #c73e54; }\n"
"           ")

        self.verticalLayout_8.addWidget(self.btnExtraerMP3)

        self.progressExtraccion = QProgressBar(self.tabExtractor)
        self.progressExtraccion.setObjectName(u"progressExtraccion")
        self.progressExtraccion.setValue(0)

        self.verticalLayout_8.addWidget(self.progressExtraccion)

        self.labelEstadoExtraccion = QLabel(self.tabExtractor)
        self.labelEstadoExtraccion.setObjectName(u"labelEstadoExtraccion")
        self.labelEstadoExtraccion.setStyleSheet(u"color: #888; font-size: 14px;")

        self.verticalLayout_8.addWidget(self.labelEstadoExtraccion)

        self.groupExtraidos = QGroupBox(self.tabExtractor)
        self.groupExtraidos.setObjectName(u"groupExtraidos")
        self.verticalLayout_9 = QVBoxLayout(self.groupExtraidos)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.listExtraidos = QListWidget(self.groupExtraidos)
        QListWidgetItem(self.listExtraidos)
        QListWidgetItem(self.listExtraidos)
        QListWidgetItem(self.listExtraidos)
        QListWidgetItem(self.listExtraidos)
        QListWidgetItem(self.listExtraidos)
        self.listExtraidos.setObjectName(u"listExtraidos")

        self.verticalLayout_9.addWidget(self.listExtraidos)


        self.verticalLayout_8.addWidget(self.groupExtraidos)

        self.tabWidget.addTab(self.tabExtractor, "")
        self.tabAudiolibro = QWidget()
        self.tabAudiolibro.setObjectName(u"tabAudiolibro")
        self.verticalLayout_10 = QVBoxLayout(self.tabAudiolibro)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.labelAudiolibro = QLabel(self.tabAudiolibro)
        self.labelAudiolibro.setObjectName(u"labelAudiolibro")
        self.labelAudiolibro.setStyleSheet(u"font-size: 24px; font-weight: bold; color: #e94560;")
        self.labelAudiolibro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.labelAudiolibro)

        self.groupPlayerAudiolibro = QGroupBox(self.tabAudiolibro)
        self.groupPlayerAudiolibro.setObjectName(u"groupPlayerAudiolibro")
        self.verticalLayout_11 = QVBoxLayout(self.groupPlayerAudiolibro)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayoutControles = QHBoxLayout()
        self.horizontalLayoutControles.setObjectName(u"horizontalLayoutControles")
        self.btnPlayAudiolibro = QPushButton(self.groupPlayerAudiolibro)
        self.btnPlayAudiolibro.setObjectName(u"btnPlayAudiolibro")
        self.btnPlayAudiolibro.setStyleSheet(u"\n"
"                 QPushButton {\n"
"                     background-color: #e94560;\n"
"                     color: white;\n"
"                     border: none;\n"
"                     padding: 10px 20px;\n"
"                     border-radius: 20px;\n"
"                     font-weight: bold;\n"
"                 }\n"
"                 QPushButton:hover { background-color: #c73e54; }\n"
"                ")

        self.horizontalLayoutControles.addWidget(self.btnPlayAudiolibro)

        self.btnPauseAudiolibro = QPushButton(self.groupPlayerAudiolibro)
        self.btnPauseAudiolibro.setObjectName(u"btnPauseAudiolibro")
        self.btnPauseAudiolibro.setStyleSheet(u"\n"
"                 QPushButton {\n"
"                     background-color: #16213e;\n"
"                     color: white;\n"
"                     border: none;\n"
"                     padding: 10px 20px;\n"
"                     border-radius: 20px;\n"
"                     font-weight: bold;\n"
"                 }\n"
"                 QPushButton:hover { background-color: #0f3460; }\n"
"                ")

        self.horizontalLayoutControles.addWidget(self.btnPauseAudiolibro)

        self.btnStopAudiolibro = QPushButton(self.groupPlayerAudiolibro)
        self.btnStopAudiolibro.setObjectName(u"btnStopAudiolibro")
        self.btnStopAudiolibro.setStyleSheet(u"\n"
"                 QPushButton {\n"
"                     background-color: #533483;\n"
"                     color: white;\n"
"                     border: none;\n"
"                     padding: 10px 20px;\n"
"                     border-radius: 20px;\n"
"                     font-weight: bold;\n"
"                 }\n"
"                 QPushButton:hover { background-color: #3d2766; }\n"
"                ")

        self.horizontalLayoutControles.addWidget(self.btnStopAudiolibro)


        self.verticalLayout_11.addLayout(self.horizontalLayoutControles)

        self.progressAudiolibro = QProgressBar(self.groupPlayerAudiolibro)
        self.progressAudiolibro.setObjectName(u"progressAudiolibro")
        self.progressAudiolibro.setValue(0)
        self.progressAudiolibro.setStyleSheet(u"\n"
"               QProgressBar {\n"
"                   border: 2px solid #16213e;\n"
"                   border-radius: 10px;\n"
"                   background-color: #0f3460;\n"
"                   height: 20px;\n"
"               }\n"
"               QProgressBar::chunk {\n"
"                   background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                       stop:0 #e94560, stop:1 #533483);\n"
"                   border-radius: 10px;\n"
"               }\n"
"              ")

        self.verticalLayout_11.addWidget(self.progressAudiolibro)

        self.groupInfoLibro = QGroupBox(self.groupPlayerAudiolibro)
        self.groupInfoLibro.setObjectName(u"groupInfoLibro")
        self.verticalLayout_12 = QVBoxLayout(self.groupInfoLibro)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.labelTituloLibro = QLabel(self.groupInfoLibro)
        self.labelTituloLibro.setObjectName(u"labelTituloLibro")

        self.verticalLayout_12.addWidget(self.labelTituloLibro)

        self.labelAutorLibro = QLabel(self.groupInfoLibro)
        self.labelAutorLibro.setObjectName(u"labelAutorLibro")

        self.verticalLayout_12.addWidget(self.labelAutorLibro)

        self.labelDuracionLibro = QLabel(self.groupInfoLibro)
        self.labelDuracionLibro.setObjectName(u"labelDuracionLibro")

        self.verticalLayout_12.addWidget(self.labelDuracionLibro)


        self.verticalLayout_11.addWidget(self.groupInfoLibro)

        self.btnCargarAudiolibro = QPushButton(self.groupPlayerAudiolibro)
        self.btnCargarAudiolibro.setObjectName(u"btnCargarAudiolibro")
        self.btnCargarAudiolibro.setStyleSheet(u"\n"
"               QPushButton {\n"
"                   background-color: #0f3460;\n"
"                   color: white;\n"
"                   border: none;\n"
"                   padding: 10px;\n"
"                   border-radius: 10px;\n"
"                   font-weight: bold;\n"
"               }\n"
"               QPushButton:hover { background-color: #0a2647; }\n"
"              ")

        self.verticalLayout_11.addWidget(self.btnCargarAudiolibro)


        self.verticalLayout_10.addWidget(self.groupPlayerAudiolibro)

        self.groupBiblioteca = QGroupBox(self.tabAudiolibro)
        self.groupBiblioteca.setObjectName(u"groupBiblioteca")
        self.verticalLayout_13 = QVBoxLayout(self.groupBiblioteca)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.listBiblioteca = QListWidget(self.groupBiblioteca)
        QListWidgetItem(self.listBiblioteca)
        QListWidgetItem(self.listBiblioteca)
        QListWidgetItem(self.listBiblioteca)
        QListWidgetItem(self.listBiblioteca)
        QListWidgetItem(self.listBiblioteca)
        self.listBiblioteca.setObjectName(u"listBiblioteca")

        self.verticalLayout_13.addWidget(self.listBiblioteca)


        self.verticalLayout_10.addWidget(self.groupBiblioteca)

        self.tabWidget.addTab(self.tabAudiolibro, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 28))
        self.menubar.setStyleSheet(u"\n"
"     QMenuBar {\n"
"         background-color: #1a1a2e;\n"
"         color: white;\n"
"         border-bottom: 2px solid #16213e;\n"
"     }\n"
"     QMenuBar::item:selected { background-color: #e94560; }\n"
"     QMenu {\n"
"         background-color: #1a1a2e;\n"
"         color: white;\n"
"         border: 1px solid #16213e;\n"
"     }\n"
"     QMenu::item:selected { background-color: #e94560; }\n"
"    ")
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"\n"
"     QStatusBar {\n"
"         background-color: #1a1a2e;\n"
"         color: white;\n"
"         border-top: 2px solid #16213e;\n"
"     }\n"
"    ")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcercaDe)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\U0001f3b5 Audio Studio Pro", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir...", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionAcercaDe.setText(QCoreApplication.translate("MainWindow", u"Acerca de", None))
        self.labelGrabadora.setText(QCoreApplication.translate("MainWindow", u"\U0001f3a4 Grabadora de Voz", None))
        self.btnGrabar.setText(QCoreApplication.translate("MainWindow", u"\U0001f534 Grabar", None))
        self.btnDetenerGrabacion.setText(QCoreApplication.translate("MainWindow", u"\u23f9 Detener", None))
        self.labelVisualizador.setText(QCoreApplication.translate("MainWindow", u"\U0001f3b5 Sin datos de audio", None))
        self.labelEstadoGrabacion.setText(QCoreApplication.translate("MainWindow", u"\u23f9 No grabando", None))
        self.groupGrabaciones.setTitle(QCoreApplication.translate("MainWindow", u"Grabaciones Guardadas", None))

        __sortingEnabled = self.listGrabaciones.isSortingEnabled()
        self.listGrabaciones.setSortingEnabled(False)
        ___qlistwidgetitem = self.listGrabaciones.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c4 Grabaci\U000000f3n_1.wav", None))
        ___qlistwidgetitem1 = self.listGrabaciones.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c4 Grabaci\U000000f3n_2.wav", None))
        ___qlistwidgetitem2 = self.listGrabaciones.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c4 Grabaci\U000000f3n_3.wav", None))
        ___qlistwidgetitem3 = self.listGrabaciones.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c4 Grabaci\U000000f3n_4.wav", None))
        ___qlistwidgetitem4 = self.listGrabaciones.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c4 Grabaci\U000000f3n_5.wav", None))
        self.listGrabaciones.setSortingEnabled(__sortingEnabled)

        self.btnReproducirGrabacion.setText(QCoreApplication.translate("MainWindow", u"\u25b6 Reproducir", None))
        self.btnEliminarGrabacion.setText(QCoreApplication.translate("MainWindow", u"\U0001f5d1 Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGrabadora), QCoreApplication.translate("MainWindow", u"\U0001f3a4 Grabadora", None))
        self.labelVisualizacion.setText(QCoreApplication.translate("MainWindow", u"\U0001f4ca Visualizaci\U000000f3n de Audio", None))
        self.labelVisualizadorGrande.setText(QCoreApplication.translate("MainWindow", u"\U0001f3b5 Sin datos de audio", None))
        self.btnCargarAudio.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c2 Cargar Audio", None))
        self.btnReproducirVisualizacion.setText(QCoreApplication.translate("MainWindow", u"\u25b6 Reproducir", None))
        self.btnDetenerVisualizacion.setText(QCoreApplication.translate("MainWindow", u"\u23f9 Detener", None))
        self.groupInfoAudio.setTitle(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n del Audio", None))
        self.labelInfoArchivo.setText(QCoreApplication.translate("MainWindow", u"Archivo: No cargado", None))
        self.labelDuracion.setText(QCoreApplication.translate("MainWindow", u"Duraci\u00f3n: 00:00:00", None))
        self.labelFormato.setText(QCoreApplication.translate("MainWindow", u"Formato: No disponible", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVisualizacion), QCoreApplication.translate("MainWindow", u"\U0001f4ca Visualizaci\U000000f3n", None))
        self.labelDescargar.setText(QCoreApplication.translate("MainWindow", u"\U0001f4e5 Descargar Videos MP4", None))
        self.labelURL.setText(QCoreApplication.translate("MainWindow", u"URL del video:", None))
        self.lineURL.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://www.youtube.com/watch?v=...", None))
        self.labelCalidad.setText(QCoreApplication.translate("MainWindow", u"Calidad:", None))
        self.comboCalidad.setItemText(0, QCoreApplication.translate("MainWindow", u"MP4 (Alta Calidad)", None))
        self.comboCalidad.setItemText(1, QCoreApplication.translate("MainWindow", u"MP4 (Media)", None))
        self.comboCalidad.setItemText(2, QCoreApplication.translate("MainWindow", u"MP4 (Baja)", None))

        self.btnDescargar.setText(QCoreApplication.translate("MainWindow", u"\u2b07\ufe0f Descargar", None))
        self.labelEstadoDescarga.setText(QCoreApplication.translate("MainWindow", u"Listo para descargar", None))
        self.groupDescargas.setTitle(QCoreApplication.translate("MainWindow", u"Descargas Recientes", None))

        __sortingEnabled1 = self.listDescargas.isSortingEnabled()
        self.listDescargas.setSortingEnabled(False)
        ___qlistwidgetitem5 = self.listDescargas.item(0)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\U0001f4f9 video_1.mp4", None))
        ___qlistwidgetitem6 = self.listDescargas.item(1)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\U0001f4f9 video_2.mp4", None))
        ___qlistwidgetitem7 = self.listDescargas.item(2)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\U0001f4f9 video_3.mp4", None))
        ___qlistwidgetitem8 = self.listDescargas.item(3)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\U0001f4f9 video_4.mp4", None))
        ___qlistwidgetitem9 = self.listDescargas.item(4)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\U0001f4f9 video_5.mp4", None))
        self.listDescargas.setSortingEnabled(__sortingEnabled1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDescargar), QCoreApplication.translate("MainWindow", u"\U0001f4e5 Descargar MP4", None))
        self.labelExtractor.setText(QCoreApplication.translate("MainWindow", u"\U0001f3b5 Extraer MP3 de MP4", None))
        self.labelArchivoSeleccionado.setText(QCoreApplication.translate("MainWindow", u"Archivo: No seleccionado", None))
        self.btnSeleccionarMP4.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c2 Seleccionar MP4", None))
        self.labelBitrate.setText(QCoreApplication.translate("MainWindow", u"Calidad:", None))
        self.comboBitrate.setItemText(0, QCoreApplication.translate("MainWindow", u"128kbps", None))
        self.comboBitrate.setItemText(1, QCoreApplication.translate("MainWindow", u"192kbps", None))
        self.comboBitrate.setItemText(2, QCoreApplication.translate("MainWindow", u"320kbps", None))

        self.btnExtraerMP3.setText(QCoreApplication.translate("MainWindow", u"\U0001f3b5 Extraer MP3", None))
        self.labelEstadoExtraccion.setText(QCoreApplication.translate("MainWindow", u"Listo para extraer", None))
        self.groupExtraidos.setTitle(QCoreApplication.translate("MainWindow", u"Archivos Extra\u00eddos", None))

        __sortingEnabled2 = self.listExtraidos.isSortingEnabled()
        self.listExtraidos.setSortingEnabled(False)
        ___qlistwidgetitem10 = self.listExtraidos.item(0)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\U0001f3b5 audio_1.mp3", None))
        ___qlistwidgetitem11 = self.listExtraidos.item(1)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\U0001f3b5 audio_2.mp3", None))
        ___qlistwidgetitem12 = self.listExtraidos.item(2)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\U0001f3b5 audio_3.mp3", None))
        ___qlistwidgetitem13 = self.listExtraidos.item(3)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\U0001f3b5 audio_4.mp3", None))
        ___qlistwidgetitem14 = self.listExtraidos.item(4)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\U0001f3b5 audio_5.mp3", None))
        self.listExtraidos.setSortingEnabled(__sortingEnabled2)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabExtractor), QCoreApplication.translate("MainWindow", u"\U0001f3b5 Extraer MP3", None))
        self.labelAudiolibro.setText(QCoreApplication.translate("MainWindow", u"\U0001f4da Audiolibro", None))
        self.groupPlayerAudiolibro.setTitle(QCoreApplication.translate("MainWindow", u"\U0001f4da Reproducci\U000000f3n", None))
        self.btnPlayAudiolibro.setText(QCoreApplication.translate("MainWindow", u"\u25b6 Play", None))
        self.btnPauseAudiolibro.setText(QCoreApplication.translate("MainWindow", u"\u23f8 Pause", None))
        self.btnStopAudiolibro.setText(QCoreApplication.translate("MainWindow", u"\u23f9 Stop", None))
        self.groupInfoLibro.setTitle(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n del libro", None))
        self.labelTituloLibro.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo: No seleccionado", None))
        self.labelAutorLibro.setText(QCoreApplication.translate("MainWindow", u"Autor: No seleccionado", None))
        self.labelDuracionLibro.setText(QCoreApplication.translate("MainWindow", u"Duraci\u00f3n: 00:00:00", None))
        self.btnCargarAudiolibro.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c2 Cargar Audiolibro", None))
        self.groupBiblioteca.setTitle(QCoreApplication.translate("MainWindow", u"Biblioteca", None))

        __sortingEnabled3 = self.listBiblioteca.isSortingEnabled()
        self.listBiblioteca.setSortingEnabled(False)
        ___qlistwidgetitem15 = self.listBiblioteca.item(0)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\U0001f4da El Principito - Antoine de Saint-Exup\U000000e9ry", None))
        ___qlistwidgetitem16 = self.listBiblioteca.item(1)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\U0001f4da 1984 - George Orwell", None))
        ___qlistwidgetitem17 = self.listBiblioteca.item(2)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\U0001f4da Cien A\U000000f1os de Soledad - Gabriel Garc\U000000eda M\U000000e1rquez", None))
        ___qlistwidgetitem18 = self.listBiblioteca.item(3)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\U0001f4da Don Quijote - Miguel de Cervantes", None))
        ___qlistwidgetitem19 = self.listBiblioteca.item(4)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\U0001f4da La Metamorfosis - Franz Kafka", None))
        self.listBiblioteca.setSortingEnabled(__sortingEnabled3)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAudiolibro), QCoreApplication.translate("MainWindow", u"\U0001f4da Audiolibro", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"&Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"&Ayuda", None))
    # retranslateUi

