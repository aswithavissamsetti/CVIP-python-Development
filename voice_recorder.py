import sys
import os
import datetime
import threading
import pyaudio
import wave
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QListWidget

class VoiceRecorderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Voice Recorder")
        self.setGeometry(100, 100, 400, 400)

        self.record_button = QPushButton("Record")
        self.stop_button = QPushButton("Stop")
        self.list_widget = QListWidget()

        self.recording = False
        self.audio = pyaudio.PyAudio()
        self.stream = None

        layout = QVBoxLayout()
        layout.addWidget(self.record_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.list_widget)

        self.record_button.clicked.connect(self.start_recording)
        self.stop_button.clicked.connect(self.stop_recording)

        self.recording_thread = None
        self.recording_file = None

        self.setLayout(layout)

    def start_recording(self):
        self.recording = True
        self.record_button.setEnabled(False)
        self.stop_button.setEnabled(True)

        self.recording_file = self.create_audio_file()
        self.stream = self.audio.open(format=pyaudio.paInt16,
                                     channels=1,
                                     rate=44100,
                                     input=True,
                                     frames_per_buffer=1024,
                                     stream_callback=self.record_callback)

        self.recording_thread = threading.Thread(target=self.record_audio)
        self.recording_thread.start()

    def stop_recording(self):
        self.recording = False
        self.record_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def create_audio_file(self):
        current_time = datetime.datetime.now()
        file_name = current_time.strftime("%Y%m%d_%H%M%S") + ".wav"
        return wave.open(file_name, 'wb')

    def record_callback(self, in_data, frame_count, time_info, status):
        self.recording_file.writeframes(in_data)
        return in_data, pyaudio.paContinue

    def record_audio(self):
        while self.recording:
            pass
        self.stream.stop_stream()
        self.stream.close()
        self.recording_file.close()

        self.list_widget.addItem(self.recording_file.name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VoiceRecorderApp()
    window.show()
    sys.exit(app.exec_())
