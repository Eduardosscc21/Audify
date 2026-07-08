# audify.py
from PySide6.QtWidgets import (QMainWindow, QSizeGrip, QFileDialog, QMessageBox, QVBoxLayout)
from PySide6.QtCore import Slot, Qt, QTimer
from PySide6 import QtCore
import sys
import os
import random
from datetime import datetime
from ventana_ui import Ui_MainWindow
import sounddevice as sd
from scipy.io.wavfile import write, read
import numpy as np 
import soundfile as sf
import threading
import time
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Variables de control
        self.is_recording = False
        self.current_audio_file = None
        self.fs = 44100
        self.recording = None
        self.audio_filename = None
        self.current_mp4_file = None
        self.current_audiobook = None
        
        ###################### Funcionalidades de las pestañas ######################
        
        # Pestaña 1: Grabadora de Voz
        self.ui.btnGrabar.toggled.connect(self.toggle_recording)
        self.ui.btnDetenerGrabacion.clicked.connect(self.stop_recording)
        self.ui.btnReproducirGrabacion.clicked.connect(self.play_recording)
        self.ui.btnEliminarGrabacion.clicked.connect(self.delete_recording)
        
        # Pestaña 2: Visualización
        self.ui.btnCargarAudio.clicked.connect(self.load_audio_file)
        self.ui.btnReproducirVisualizacion.clicked.connect(self.play_visualization)
        self.ui.btnDetenerVisualizacion.clicked.connect(self.stop_visualization)
        self.visual_audio = None
        self.visual_fs = None
        self.visual_thread = None
        self.stop_visual = False
        # Crear figura de matplotlib
        self.figure = Figure(figsize=(8,4))
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_facecolor("#1a1a2e")
        self.figure.patch.set_facecolor("#1a1a2e")
        self.ax.tick_params(colors="white")
        self.ax.spines["bottom"].set_color("white")
        self.ax.spines["left"].set_color("white")
        layout = QVBoxLayout(self.ui.frameVisualizadorGrande)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.canvas)
        self.cursor = None
        
        # Pestaña 3: Descargar MP4
        self.ui.btnDescargar.clicked.connect(self.start_download)
        
        # Pestaña 4: Extraer MP3
        self.ui.btnSeleccionarMP4.clicked.connect(self.select_mp4_file)
        self.ui.btnExtraerMP3.clicked.connect(self.extract_mp3)
        
        # Pestaña 5: Audiolibro
        self.ui.btnPlayAudiolibro.clicked.connect(self.play_audiobook)
        self.ui.btnPauseAudiolibro.clicked.connect(self.pause_audiobook)
        self.ui.btnStopAudiolibro.clicked.connect(self.stop_audiobook)
        self.ui.btnCargarAudiolibro.clicked.connect(self.load_audiobook)
        
        # Conexión de lista de audiolibros (doble clic)
        self.ui.listBiblioteca.itemDoubleClicked.connect(self.load_selected_audiobook)
        
        # Conexión de acciones del menú
        self.ui.actionAbrir.triggered.connect(self.open_file)
        self.ui.actionSalir.triggered.connect(self.close)
        self.ui.actionAcercaDe.triggered.connect(self.show_about)
        
        # Inicializar estado
        self.update_status("Listo")
        
        # Timers para simulaciones
        #self.visualization_timer = QTimer()
        #self.visualization_timer.timeout.connect(self.simulate_visualization)
        
        self.recording_timer = QTimer()
        self.recording_timer.timeout.connect(self.simulate_recording)
        self.recording_counter = 0
    
    ###################### Funciones de menú ######################
    def open_file(self):
        """Abrir archivo desde el menú"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Abrir Archivo", "",
            "Todos los archivos (*.*)"
        )
        if file_path:
            self.update_status(f"Archivo abierto: {file_path}")
    
    def show_about(self):
        """Mostrar diálogo Acerca de"""
        QMessageBox.about(self, "Acerca de Audio Studio Pro",
            """<h2>🎵 Audio Studio Pro</h2>
            <p>Versión: 1.0.0</p>
            <p>Una aplicación completa para herramientas de audio:</p>
            <ul>
                <li>🎤 Grabadora de voz</li>
                <li>📊 Visualización de audio</li>
                <li>📥 Descarga de videos MP4</li>
                <li>🎵 Extracción de MP3</li>
                <li>📚 Reproducción de audiolibros</li>
            </ul>
            <p>Desarrollado con PySide6</p>
            <p>© 2026 Audio Studio Pro</p>
            """)
    
    def update_status(self, message):
        """Actualizar barra de estado"""
        self.ui.statusbar.showMessage(message)
        self.ui.labelEstadoGrabacion.setText(message)
    
    ###################### Pestaña 1: Grabadora ######################
    @Slot()
    def toggle_recording(self, checked):
        #
        """Iniciar grabación real"""

        if checked:
            #
            self.is_recording = True
            self.ui.btnGrabar.setText("🔴 Grabando...")
            self.ui.labelEstadoGrabacion.setText("🔴 Grabando...")
            self.update_status("Grabando audio...")
            carpeta = os.path.join(os.getcwd(), "grabaciones")
            os.makedirs(carpeta, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.audio_filename = os.path.join(carpeta,f"Grabacion_{timestamp}.wav")
            # Comienza a grabar (hasta que se detenga)
            self.recording = sd.rec(int(3600 * self.fs), samplerate=self.fs,channels=2,dtype=np.int16)
            self.visualization_timer.start(100)
        else:
            #
            self.stop_recording()
    
    def stop_recording(self):
        """Detener grabación y guardar WAV"""
        #
        if not self.is_recording:
            return
        self.is_recording = False
        sd.stop()
        sd.wait()
        # Buscar cuántas muestras realmente se grabaron
        indice = sd.get_stream().latency if False else None
        audio = self.recording
        # Eliminar la parte vacía
        audio = audio[np.any(audio != 0, axis=1)]
        if len(audio) > 0:
            write(self.audio_filename,self.fs,audio)
            nombre = os.path.basename(self.audio_filename)
            self.ui.listGrabaciones.addItem(f"📄 {nombre}")
            self.current_audio_file = self.audio_filename
            QMessageBox.information(self,"Grabación",f"Audio guardado en:\n\n{self.audio_filename}")

        self.recording = None
        self.visualization_timer.stop()
        self.ui.btnGrabar.blockSignals(True)
        self.ui.btnGrabar.setChecked(False)
        self.ui.btnGrabar.blockSignals(False)
        self.ui.btnGrabar.setText("🔴 Grabar")
        self.ui.labelEstadoGrabacion.setText("⏹ Grabación detenida")
        self.ui.labelVisualizador.setText("🎵 Sin datos de audio")
        
    
    def simulate_recording(self):
        """Simular datos de grabación"""
        self.recording_counter += 1
        if self.recording_counter % 5 == 0:
            levels = [random.randint(0, 100) for _ in range(20)]
            bars = "".join(["▬" * (level // 10) for level in levels[:10]])
            self.ui.labelVisualizador.setText(f"🎵 {bars}")
    
    def play_recording(self):

        """Reproducir la grabación seleccionada"""
        item = self.ui.listGrabaciones.currentItem()

        if item is None:
            #
            QMessageBox.warning(self,"Error","Selecciona una grabación.")
            return
        nombre = item.text().replace("📄 ", "")

        ruta = os.path.join(os.getcwd(),"grabaciones",nombre)

        if not os.path.exists(ruta):
            QMessageBox.warning(self,"Error","No existe el archivo:\n" + ruta)
            return
        try:
            data, fs = sf.read(ruta)
            sd.stop()
            sd.play(data, fs)
            sd.wait()
        except Exception as e:
            QMessageBox.critical(self,"Error",str(e))
            
    
    def delete_recording(self):
        """Eliminar grabación seleccionada"""
        selected = self.ui.listGrabaciones.currentItem()
        if selected:
            reply = QMessageBox.question(self, "Confirmar", 
                f"¿Eliminar {selected.text()}?",
                QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.ui.listGrabaciones.takeItem(self.ui.listGrabaciones.currentRow())
                self.update_status(f"Eliminado: {selected.text()}")
        else:
            QMessageBox.warning(self, "Error", "Selecciona una grabación para eliminar")
    
    ###################### Pestaña 2: Visualización ######################
    def load_audio_file(self):

        file_path, _ = QFileDialog.getOpenFileName(self,"Seleccionar Audio","","Audio (*.wav *.mp3 *.flac)")

        if not file_path:
            return
        self.current_audio_file = file_path
        audio, fs = sf.read(file_path)

        if audio.ndim == 2:
            audio = audio.mean(axis=1)

        self.visual_audio = audio
        self.visual_fs = fs

        duracion = len(audio)/fs

        self.ui.labelInfoArchivo.setText(f"Archivo: {os.path.basename(file_path)}")

        self.ui.labelDuracion.setText(f"Duración: {duracion:.2f} segundos")

        self.ui.labelFormato.setText(f"Formato: {file_path.split('.')[-1].upper()}   {fs} Hz")

        self.draw_waveform()
        
    
    def play_visualization(self):
        if self.visual_audio is None:
            QMessageBox.warning(self,"Error","Carga un audio primero.")
            return
        self.stop_visual = False
        sd.stop()
        sd.play(self.visual_audio,self.visual_fs)
        self.visual_thread = threading.Thread(target=self.update_cursor,daemon=True)
        self.visual_thread.start()
        


    def stop_visualization(self):
        self.stop_visual = True
        sd.stop()
        if self.cursor is not None:
            self.cursor.set_xdata([0,0])
            self.canvas.draw_idle()
        
    
    def simulate_visualization(self):
        """Simular visualización de audio"""
        levels = [random.randint(0, 100) for _ in range(50)]
        
        # Actualizar visualizador pequeño
        bars_small = "".join(["▬" * (level // 10) for level in levels[:10]])
        self.ui.labelVisualizador.setText(f"🎵 {bars_small}")
        
        # Actualizar visualizador grande
        bars_large = "".join(["▓" * (level // 10) for level in levels[:20]])
        self.ui.labelVisualizadorGrande.setText(f"🎵 {bars_large}")

    def draw_waveform(self):
        self.ax.clear()

        datos = self.visual_audio

        if len(datos) > 50000:
            salto = len(datos)//50000
            datos = datos[::salto]

        self.ax.plot(datos,color="#00ff88")
        self.ax.set_title("Forma de onda",color="white")
        self.ax.set_xlim(0,len(datos))
        self.canvas.draw()
        self.cursor = self.ax.axvline(x=0,color="red",linewidth=2)
        self.canvas.draw()

    def update_cursor(self):
        #
        total = len(self.visual_audio)

        inicio = time.time()

        while not self.stop_visual:
            t = time.time() - inicio
            pos = int(t*self.visual_fs)

            if pos >= total:
                break

            self.cursor.set_xdata([pos,pos])
            self.canvas.draw_idle()
            time.sleep(0.02)


    
    ###################### Pestaña 3: Descargar MP4 ######################
    def start_download(self):
        """Iniciar descarga del video"""
        url = self.ui.lineURL.text().strip()
        if not url:
            QMessageBox.warning(self, "Error", "Ingresa una URL válida")
            return
        
        self.update_status("⏳ Descargando video...")
        self.ui.progressDescarga.setValue(0)
        self.ui.labelEstadoDescarga.setText("⏳ Descargando...")
        
        # Simular progreso de descarga
        #self.download_timer = QTimer()
        self.download_progress_value = 0
        
        def update_download():
            self.download_progress_value += 5
            self.ui.progressDescarga.setValue(self.download_progress_value)
            if self.download_progress_value >= 100:
                self.download_timer.stop()
                self.ui.labelEstadoDescarga.setText("✅ Descarga completada")
                self.update_status("Descarga completada exitosamente")
                timestamp = datetime.now().strftime("%H%M%S")
                self.ui.listDescargas.addItem(f"📹 video_{timestamp}.mp4")
                QMessageBox.information(self, "Completado", "¡Descarga finalizada!")
        
        self.download_timer.timeout.connect(update_download)
        self.download_timer.start(300)
    
    ###################### Pestaña 4: Extraer MP3 ######################
    def select_mp4_file(self):
        """Seleccionar archivo MP4 para extracción"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar Archivo MP4", "",
            "Archivos MP4 (*.mp4);;Todos los archivos (*.*)"
        )
        if file_path:
            self.current_mp4_file = file_path
            self.ui.labelArchivoSeleccionado.setText(f"Archivo: {os.path.basename(file_path)}")
            self.update_status(f"Archivo seleccionado: {file_path}")
    
    def extract_mp3(self):
        """Extraer MP3 del MP4 seleccionado"""
        if not hasattr(self, 'current_mp4_file') or not self.current_mp4_file:
            QMessageBox.warning(self, "Error", "Primero selecciona un archivo MP4")
            return
        
        self.update_status("⏳ Extrayendo MP3...")
        self.ui.progressExtraccion.setValue(0)
        self.ui.labelEstadoExtraccion.setText("⏳ Extrayendo...")
        
        # Simular extracción
        self.extract_timer = QTimer()
        self.extract_progress_value = 0
        
        def update_extract():
            self.extract_progress_value += 10
            self.ui.progressExtraccion.setValue(self.extract_progress_value)
            if self.extract_progress_value >= 100:
                self.extract_timer.stop()
                self.ui.labelEstadoExtraccion.setText("✅ Extracción completada")
                self.update_status("MP3 extraído exitosamente")
                timestamp = datetime.now().strftime("%H%M%S")
                self.ui.listExtraidos.addItem(f"🎵 audio_{timestamp}.mp3")
                QMessageBox.information(self, "Completado", "¡MP3 extraído exitosamente!")
                self.current_mp4_file = None
                self.ui.labelArchivoSeleccionado.setText("Archivo: No seleccionado")
        
        self.extract_timer.timeout.connect(update_extract)
        self.extract_timer.start(500)
    
    ###################### Pestaña 5: Audiolibro ######################
    def load_audiobook(self):
        """Cargar archivo de audiolibro"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar Audiolibro", "",
            "Archivos de Audio (*.mp3 *.wav *.m4a);;Todos los archivos (*.*)"
        )
        if file_path:
            self.current_audiobook = file_path
            self.ui.labelTituloLibro.setText(f"Título: {os.path.basename(file_path)}")
            self.ui.labelAutorLibro.setText("Autor: Desconocido")
            self.ui.progressAudiolibro.setValue(0)
            self.update_status(f"Audiolibro cargado: {file_path}")
    
    def load_selected_audiobook(self, item):
        """Cargar audiolibro seleccionado de la biblioteca"""
        book_title = item.text()
        self.ui.labelTituloLibro.setText(f"Título: {book_title}")
        self.ui.labelAutorLibro.setText("Autor: Seleccionado")
        self.ui.progressAudiolibro.setValue(0)
        self.update_status(f"Seleccionado: {book_title}")
    
    def play_audiobook(self):
        """Reproducir audiolibro"""
        if "No seleccionado" in self.ui.labelTituloLibro.text():
            QMessageBox.warning(self, "Error", "Carga o selecciona un audiolibro primero")
            return
        
        self.ui.btnPlayAudiolibro.setText("⏸ Pausa")
        self.update_status("Reproduciendo audiolibro...")
        
        # Simular reproducción
        self.audiobook_timer = QTimer()
        self.audiobook_timer.timeout.connect(self.update_audiobook_progress)
        self.audiobook_timer.start(1000)
    
    def pause_audiobook(self):
        """Pausar audiolibro"""
        self.ui.btnPlayAudiolibro.setText("▶ Play")
        self.update_status("Audiolibro en pausa")
        if hasattr(self, 'audiobook_timer'):
            self.audiobook_timer.stop()
    
    def stop_audiobook(self):
        """Detener audiolibro"""
        self.ui.btnPlayAudiolibro.setText("▶ Play")
        self.ui.progressAudiolibro.setValue(0)
        self.update_status("Audiolibro detenido")
        if hasattr(self, 'audiobook_timer'):
            self.audiobook_timer.stop()
    
    def update_audiobook_progress(self):
        """Actualizar barra de progreso del audiolibro"""
        value = self.ui.progressAudiolibro.value() + 5
        if value >= 100:
            value = 0
            self.update_status("Audiolibro completado")
            self.ui.btnPlayAudiolibro.setText("▶ Play")
            if hasattr(self, 'audiobook_timer'):
                self.audiobook_timer.stop()
        self.ui.progressAudiolibro.setValue(value)