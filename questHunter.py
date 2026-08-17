import sys
import os
import json
import urllib.request
from PyQt6.QtCore import QSize, Qt, QThread, pyqtSignal, QByteArray
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
    QProgressBar,
    QDialog,
    QMessageBox,
)
import shutil
import subprocess
import base64
import hashlib
import webbrowser
from datetime import datetime

CURRENT_VERSION = "1.1.0"

icon_b64 = """ 
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
"""

def get_app_icon(base64_str: str) -> QIcon:
    try:
        if "," in base64_str:
            base64_str = base64_str.split(",", 1)[1]

        img_bytes = base64.b64decode(base64_str)
        q_byte_array = QByteArray(img_bytes)

        pixmap = QPixmap()
        if pixmap.loadFromData(q_byte_array):
            return QIcon(pixmap)
    except Exception as e:
        print(f"[IconLoader] Failed to decode window icon: {e}")

    return QIcon()

if getattr(sys, "frozen", False):
    EXE_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    EXE_DIR = os.path.dirname(os.path.abspath(__file__))

CACHE_DIR = os.path.join(EXE_DIR, "icon_cache")
os.makedirs(CACHE_DIR, exist_ok=True)

JSON_FEED_URL = "https://raw.githubusercontent.com/P1sco/QuestHunter/main/Data-Feed/quests.json"
FULL_LIST_URL = "https://raw.githubusercontent.com/P1sco/QuestHunter/refs/heads/main/Data-Feed/fullList.json"
FULL_LIST_FILE = os.path.join(EXE_DIR, "fullList.json")
WEBSITE_URL = "https://www.questhunter.dev"
ERROR_LOG_FILE = os.path.join(EXE_DIR, "error_log.txt")
def log_error(error_message, context=""):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {error_message}\n"
        if context:
            log_entry += f"Context: {context}\n"
        log_entry += "-" * 60 + "\n"
        
        with open(ERROR_LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Failed to write to error log: {e}")


class FullListDownloader(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error = pyqtSignal(str)
    update_required = pyqtSignal()

    def __init__(self, force_download=False):
        super().__init__()
        self.force_download = force_download

    def run(self):
        try:
            local_exists = os.path.exists(FULL_LIST_FILE)
            local_size = os.path.getsize(FULL_LIST_FILE) if local_exists else 0
            
            try:
                req = urllib.request.Request(
                    FULL_LIST_URL,
                    headers={"User-Agent": "QuestHunter-Launcher/1.0"},
                    method="HEAD"
                )
                with urllib.request.urlopen(req, timeout=10) as response:
                    remote_size = int(response.headers.get('content-length', 0))
            except Exception as e:
                print(f"HEAD request failed: {e}")
                remote_size = -1
            
            if self.force_download or not local_exists or (remote_size != -1 and local_size != remote_size):
                if local_exists and remote_size != -1 and local_size != remote_size:
                    self.update_required.emit()
                    return
                else:
                    self.download_full_list()
            else:
                self.finished.emit()
                
        except Exception as e:
            self.error.emit(f"Failed to check fullList.json: {str(e)}")

    def download_full_list(self):
        try:
            req = urllib.request.Request(
                FULL_LIST_URL,
                headers={"User-Agent": "QuestHunter-Launcher/1.0"}
            )
            with urllib.request.urlopen(req, timeout=30) as response:
                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0
                
                with open(FULL_LIST_FILE, 'wb') as f:
                    while True:
                        chunk = response.read(8192)
                        if not chunk:
                            break
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            progress = int((downloaded / total_size) * 100)
                            self.progress.emit(progress)
                
                self.finished.emit()
        except Exception as e:
            self.error.emit(f"Failed to download fullList.json: {str(e)}")

class JSONFetcher(QThread):
    data_loaded = pyqtSignal(list)
    error_occurred = pyqtSignal(str)

    def run(self):
        try:
            req = urllib.request.Request(
                JSON_FEED_URL, 
                headers={"User-Agent": "QuestHunter-Launcher/1.0"}
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                payload = json.loads(response.read().decode("utf-8"))
                if isinstance(payload, dict):
                    games = payload.get("games", payload.get("quests", []))
                else:
                    games = payload
                self.data_loaded.emit(games)
        except Exception as e:
            self.error_occurred.emit(str(e))

class DiscordSearcher(QThread):
    data_loaded = pyqtSignal(list)
    error_occurred = pyqtSignal(str)

    def __init__(self, search_query):
        super().__init__()
        self.search_query = search_query.lower().strip()

    def run(self):
        try:
            if not os.path.exists(FULL_LIST_FILE):
                self.error_occurred.emit("fullList.json not found. Please download it first.")
                return

            with open(FULL_LIST_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)

            filtered_games = []
            for game in data:
                game_name = game.get("name", "").lower()
                aliases = [alias.lower() for alias in game.get("aliases", [])]
                
                if (self.search_query in game_name or 
                    any(self.search_query in alias for alias in aliases)):
                    
                    game_id = game.get("id", "")
                    name = game.get("name", "Unknown Game")
                    icon_hash = game.get("icon_hash", "")
                    
                    executables = game.get("executables", [])
                    exec_path = ""
                    if executables:
                        for exe in executables:
                            if exe.get("os") == "win32":
                                exec_path = exe.get("name", "")
                                break
                        if not exec_path:
                            exec_path = executables[0].get("name", "")
                    
                    icon_url = ""
                    if game_id and icon_hash:
                        icon_url = f"https://cdn.discordapp.com/app-icons/{game_id}/{icon_hash}.png"
                    
                    filtered_games.append({
                        "id": game_id,
                        "name": name,
                        "icon_url": icon_url,
                        "icon_hash": icon_hash,
                        "exec_path": exec_path,
                        "source": "discord"
                    })
            
            if filtered_games:
                self.data_loaded.emit(filtered_games)
            else:
                self.error_occurred.emit(f"Game not found: {self.search_query}")
                
        except json.JSONDecodeError:
            self.error_occurred.emit("Error: Corrupted fullList.json file")
        except Exception as e:
            self.error_occurred.emit(f"Error searching: {str(e)}")

class UpdateChecker(QThread):
    update_available = pyqtSignal(str, str)
    error_occurred = pyqtSignal(str)
    no_update = pyqtSignal()

    def run(self):
        try:
            req = urllib.request.Request(
                "https://api.github.com/repos/P1sco/QuestHunter/releases/latest",
                headers={"User-Agent": "QuestHunter-Launcher/1.0"}
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode("utf-8"))
                latest_version = data.get("tag_name", "").lstrip("v")
                
                if latest_version and self.is_newer_version(latest_version, CURRENT_VERSION):
                    self.update_available.emit(latest_version, WEBSITE_URL)
                else:
                    self.no_update.emit()
        except Exception as e:
            self.error_occurred.emit(f"Update check failed: {str(e)}")
    
    def is_newer_version(self, latest, current):
        try:
            latest_parts = [int(x) for x in latest.split('.')]
            current_parts = [int(x) for x in current.split('.')]
            
            while len(latest_parts) < len(current_parts):
                latest_parts.append(0)
            while len(current_parts) < len(latest_parts):
                current_parts.append(0)
            
            for i in range(len(latest_parts)):
                if latest_parts[i] > current_parts[i]:
                    return True
                elif latest_parts[i] < current_parts[i]:
                    return False
            return False
        except:
            return latest != current

class IconDownloader(QThread):
    icon_loaded = pyqtSignal(str, str)

    def __init__(self, game_id, icon_url):
        super().__init__()
        self.game_id = game_id
        self.icon_url = icon_url

    def run(self):
        if not self.icon_url or not self.icon_url.startswith(("http://", "https://")):
            return

        url_hash = hashlib.md5(self.icon_url.encode()).hexdigest()[:8]
        file_name = f"{self.game_id}_{url_hash}.png"
        local_path = os.path.join(CACHE_DIR, file_name)

        if os.path.exists(local_path):
            self.icon_loaded.emit(self.game_id, local_path)
            return

        try:
            req = urllib.request.Request(
                self.icon_url, 
                headers={"User-Agent": "QuestHunter-Launcher/1.0"}
            )
            with urllib.request.urlopen(req, timeout=10) as resp, open(local_path, "wb") as f:
                f.write(resp.read())
            self.icon_loaded.emit(self.game_id, local_path)
        except Exception as e:
            print(f"[IconDownloader] Failed to fetch icon for {self.game_id}: {e}")

class GameCard(QFrame):
    def __init__(self, game_id, game_name, icon_url, exec_path="", source="github", parent=None):
        super().__init__(parent)
        self.game_id = game_id
        self.game_name = game_name
        self.icon_url = icon_url
        self.exec_path = exec_path
        self.source = source
        self.is_selected = False

        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedWidth(130)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(8, 10, 8, 10)
        layout.setSpacing(6)

        self.icon_label = QLabel()
        self.icon_label.setFixedSize(64, 64)
        self.icon_label.setScaledContents(True)
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.load_icon(icon_url)

        self.title_label = QLabel(game_name)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setWordWrap(True)
        
        if source == "discord":
            self.title_label.setStyleSheet("font-weight: bold; font-size: 11px; color: #00ccff;")
        else:
            self.title_label.setStyleSheet("font-weight: bold; font-size: 11px; color: #e0e0e0;")

        layout.addWidget(self.icon_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.set_selected(False)

    def load_icon(self, icon_url):
        if icon_url and icon_url.startswith(("http://", "https://")):
            url_hash = hashlib.md5(icon_url.encode()).hexdigest()[:8]
            file_name = f"{self.game_id}_{url_hash}.png"
            local_path = os.path.join(CACHE_DIR, file_name)
            
            if os.path.exists(local_path):
                self.icon_label.setPixmap(QPixmap(local_path))
            else:
                self.icon_label.setText("🎮")
                self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.downloader = IconDownloader(self.game_id, icon_url)
                self.downloader.icon_loaded.connect(self.on_icon_downloaded)
                self.downloader.start()
        elif os.path.exists(icon_url):
            self.icon_label.setPixmap(QPixmap(icon_url))
        else:
            self.icon_label.setText("🎮")
            self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def on_icon_downloaded(self, game_id, local_path):
        if game_id == self.game_id and os.path.exists(local_path):
            self.icon_label.setPixmap(QPixmap(local_path))

    def set_selected(self, selected: bool):
        self.is_selected = selected
        if selected:
            self.setStyleSheet("""
                GameCard {
                    border: 2px solid #007acc;
                    border-radius: 8px;
                }
            """)
        else:
            self.setStyleSheet("""
                GameCard {
                    border: 1px solid #333333;
                    border-radius: 8px;
                }
                GameCard:hover {
                    border: 1px solid #555555;
                }
            """)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            main_win = self.window()
            if hasattr(main_win, "select_game"):
                main_win.select_game(self)
        super().mousePressEvent(event)

class ProgressDialog(QDialog):
    def __init__(self, title, label_text, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(400, 120)
        self.setStyleSheet("background-color: #1e1e1e; color: #ffffff;")
        
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        
        self.label = QLabel(label_text)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 13px;")
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid #333333;
                border-radius: 4px;
                text-align: center;
                height: 20px;
            }
            QProgressBar::chunk {
                background-color: #007acc;
                border-radius: 4px;
            }
        """)
        
        layout.addWidget(self.label)
        layout.addWidget(self.progress_bar)
        
        self.cancelled = False

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def set_status(self, text):
        self.label.setText(text)

    def closeEvent(self, event):
        self.cancelled = True
        event.accept()

class LauncherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quest Hunter - Discord Quests Spoofer")
        self.setFixedSize(640, 560)
        self.setStyleSheet("background-color: #121212; color: #ffffff;")
        self.setWindowIcon(get_app_icon(icon_b64))
        
        self.selected_card = None
        self.all_cards = []
        self.discord_cards = []
        self.is_discord_search = False

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(10)

        search_container = QWidget()
        search_layout = QHBoxLayout(search_container)
        search_layout.setContentsMargins(0, 0, 0, 0)
        search_layout.setSpacing(8)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search games...")
        self.search_bar.setFixedHeight(35)
        self.search_bar.setStyleSheet("""
            QLineEdit {
                background-color: #1e1e1e;
                border: 1px solid #333333;
                border-radius: 6px;
                padding: 0 10px;
                color: #ffffff;
            }
            QLineEdit:focus {
                border: 1px solid #007acc;
            }
        """)
        self.search_bar.textChanged.connect(self.filter_games)
        self.search_bar.returnPressed.connect(self.on_search_enter)
        
        self.deep_search_btn = QPushButton("🔍 Deep Search")
        self.deep_search_btn.setFixedHeight(35)
        self.deep_search_btn.setStyleSheet("""
            QPushButton {
                background-color: #2a2a2a;
                color: #00ccff;
                font-weight: bold;
                border: 1px solid #00ccff;
                border-radius: 6px;
                padding: 0 16px;
            }
            QPushButton:hover {
                background-color: #1a3a4a;
                border: 1px solid #00ddff;
            }
            QPushButton:pressed {
                background-color: #0a2a3a;
            }
        """)
        self.deep_search_btn.clicked.connect(self.on_deep_search)
        
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.deep_search_btn)
        
        main_layout.addWidget(search_container)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        grid_container = QWidget()
        self.grid_layout = QGridLayout(grid_container)
        self.grid_layout.setSpacing(12)
        self.grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        scroll_area.setWidget(grid_container)
        main_layout.addWidget(scroll_area)

        bottom_bar = QVBoxLayout()
        bottom_bar.setContentsMargins(4, 4, 4, 4)
        bottom_bar.setSpacing(6)

        controls_row = QHBoxLayout()

        self.status_label = QLabel(f"Version {CURRENT_VERSION} - Loading...")
        self.status_label.setStyleSheet("color: #888888; font-size: 12px;")

        self.launch_btn = QPushButton("Launch Replica")
        self.launch_btn.setFixedHeight(40)
        self.launch_btn.setEnabled(False)
        self.launch_btn.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                font-weight: bold;
                border-radius: 6px;
                padding: 0 24px;
            }
            QPushButton:disabled {
                background-color: #2a2a2a;
                color: #666666;
            }
            QPushButton:hover:enabled {
                background-color: #0098ff;
            }
        """)
        self.launch_btn.clicked.connect(self.on_launch_clicked)

        controls_row.addWidget(self.status_label)
        controls_row.addStretch()
        controls_row.addWidget(self.launch_btn)

        disclaimer_label = QLabel("⚠️ Quest Hunter is 100% Free & Open Source. If you paid for this software, you were scammed. Made with love by Pisco ❤️")
        disclaimer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        disclaimer_label.setStyleSheet("color: white; font-size: 10px; font-weight: 500; padding-top: 4px;")

        bottom_bar.addLayout(controls_row)
        bottom_bar.addWidget(disclaimer_label)

        main_layout.addLayout(bottom_bar)

        self.initialize_app()

    def initialize_app(self):
        self.check_full_list()
        self.check_app_updates()
        self.fetch_github_quests()

    def check_full_list(self):
        self.full_list_downloader = FullListDownloader()
        self.full_list_downloader.progress.connect(self.on_download_progress)
        self.full_list_downloader.finished.connect(self.on_full_list_ready)
        self.full_list_downloader.error.connect(self.on_full_list_error)
        self.full_list_downloader.update_required.connect(self.on_update_needed)
        self.full_list_downloader.start()

    def on_download_progress(self, value):
        self.status_label.setText(f"Downloading fullList.json: {value}%")
        self.status_label.setStyleSheet("color: #00ccff; font-size: 12px;")

    def on_full_list_ready(self):
        self.status_label.setText(f"Version {CURRENT_VERSION} ")
        self.status_label.setStyleSheet("color: #55ff55; font-size: 12px;")

    def on_full_list_error(self, error):
        self.status_label.setText(f"Error: {error}")
        self.status_label.setStyleSheet("color: #ff5555; font-size: 12px;")

    def on_update_needed(self):
        reply = QMessageBox.question(
            self,
            "Update Available",
            "A newer version of fullList.json is available.\n\nWould you like to download it now?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.progress_dialog = ProgressDialog(
                "Updating fullList.json",
                "Downloading latest version...",
                self
            )
            self.progress_dialog.show()
            
            self.full_list_downloader = FullListDownloader(force_download=True)
            self.full_list_downloader.progress.connect(self.progress_dialog.update_progress)
            self.full_list_downloader.finished.connect(self.on_update_finished)
            self.full_list_downloader.error.connect(self.on_update_error)
            self.full_list_downloader.start()
        else:
            self.status_label.setText(f"Version {CURRENT_VERSION} - Using existing fullList.json")
            self.status_label.setStyleSheet("color: #888888; font-size: 12px;")

    def on_update_finished(self):
        if hasattr(self, 'progress_dialog'):
            self.progress_dialog.close()
        self.status_label.setText(f"Version {CURRENT_VERSION} - fullList.json updated successfully")
        self.status_label.setStyleSheet("color: #55ff55; font-size: 12px;")

    def on_update_error(self, error):
        if hasattr(self, 'progress_dialog'):
            self.progress_dialog.close()
        self.status_label.setText(f"Update failed: {error}")
        self.status_label.setStyleSheet("color: #ff5555; font-size: 12px;")

    def check_app_updates(self):
        self.update_checker = UpdateChecker()
        self.update_checker.update_available.connect(self.on_update_available)
        self.update_checker.error_occurred.connect(self.on_update_check_error)
        self.update_checker.no_update.connect(self.on_no_update)
        self.update_checker.start()

    def on_update_available(self, version, url):
        reply = QMessageBox.question(
            self,
            "Update Available",
            f"A new version (v{version}) is available!\n\nCurrent version: v{CURRENT_VERSION}\n\nWould you like to visit the website to download it?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            webbrowser.open(url)

    def on_update_check_error(self, error):
        pass

    def on_no_update(self):
        pass

    def fetch_github_quests(self):
        self.json_fetcher = JSONFetcher()
        self.json_fetcher.data_loaded.connect(self.on_json_loaded)
        self.json_fetcher.error_occurred.connect(self.on_json_error)
        self.json_fetcher.start()

    def on_json_loaded(self, games_list):
        self.all_cards.clear()
        self.is_discord_search = False
        self.discord_cards.clear()

        sorted_games = sorted(
            games_list, key=lambda g: str(g.get("name", "")).lower()
        )

        for game in sorted_games:
            g_id = game.get("id", str(game.get("name", "")).lower().replace(" ", "_"))
            name = game.get("name", "Unknown Game")
            icon_url = game.get("icon_url", game.get("icon", ""))
            exec_path = game.get("exe_path") or game.get("exec", "")

            card = GameCard(g_id, name, icon_url, exec_path, source="github")
            self.all_cards.append(card)

        self.rebuild_grid(self.all_cards)
        self.status_label.setText(f"Version {CURRENT_VERSION} - Select a game to launch")
        self.status_label.setStyleSheet("color: #888888; font-size: 12px;")

    def on_json_error(self, err_msg):
        self.status_label.setText(f"Failed to fetch feed: {err_msg}")
        self.status_label.setStyleSheet("color: #ff5555; font-size: 12px;")

    def on_deep_search(self):
        query = self.search_bar.text().strip()
        if not query:
            self.status_label.setText("Please enter a search term")
            self.status_label.setStyleSheet("color: #ff5555; font-size: 12px;")
            return
        
        if not os.path.exists(FULL_LIST_FILE):
            reply = QMessageBox.question(
                self,
                "fullList.json Missing",
                "fullList.json is required for Deep Search.\n\nWould you like to download it now?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                self.progress_dialog = ProgressDialog(
                    "Downloading fullList.json",
                    "Downloading Discord game database...",
                    self
                )
                self.progress_dialog.show()
                
                self.full_list_downloader = FullListDownloader(force_download=True)
                self.full_list_downloader.progress.connect(self.progress_dialog.update_progress)
                self.full_list_downloader.finished.connect(self.on_full_list_downloaded_for_search)
                self.full_list_downloader.error.connect(self.on_full_list_download_error)
                self.full_list_downloader.start()
            return
        
        if self.selected_card:
            self.selected_card.set_selected(False)
            self.selected_card = None
            self.launch_btn.setEnabled(False)
        
        self.status_label.setText(f"Searching Discord for '{query}'...")
        self.status_label.setStyleSheet("color: #00ccff; font-size: 12px;")
        self.clear_grid()
        
        self.discord_searcher = DiscordSearcher(query)
        self.discord_searcher.data_loaded.connect(self.on_discord_search_loaded)
        self.discord_searcher.error_occurred.connect(self.on_discord_search_error)
        self.discord_searcher.start()

    def on_full_list_downloaded_for_search(self):
        if hasattr(self, 'progress_dialog'):
            self.progress_dialog.close()
        self.on_deep_search()

    def on_full_list_download_error(self, error):
        if hasattr(self, 'progress_dialog'):
            self.progress_dialog.close()
        self.status_label.setText(f"Download failed: {error}")
        self.status_label.setStyleSheet("color: #ff5555; font-size: 12px;")

    def on_discord_search_loaded(self, games_list):
        self.discord_cards.clear()
        self.is_discord_search = True
        
        for game in games_list:
            g_id = game.get("id", "")
            name = game.get("name", "Unknown Game")
            icon_url = game.get("icon_url", "")
            exec_path = game.get("exec_path", "")

            card = GameCard(g_id, name, icon_url, exec_path, source="discord")
            self.discord_cards.append(card)

        self.rebuild_grid(self.discord_cards)
        
        if self.discord_cards:
            self.status_label.setText(f"Found {len(self.discord_cards)} game(s) from Discord")
            self.status_label.setStyleSheet("color: #00ccff; font-size: 12px; font-weight: bold;")
        else:
            self.status_label.setText("Game not found")
            self.status_label.setStyleSheet("color: #ff5555; font-size: 12px; font-weight: bold;")

    def on_discord_search_error(self, err_msg):
        self.status_label.setText(err_msg)
        self.status_label.setStyleSheet("color: #ff5555; font-size: 12px; font-weight: bold;")
        self.is_discord_search = False
        
        if self.all_cards:
            self.rebuild_grid(self.all_cards)
        else:
            self.clear_grid()

    def clear_grid(self):
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    def rebuild_grid(self, card_list):
        self.clear_grid()
        COLUMNS = 4
        for index, card in enumerate(card_list):
            row = index // COLUMNS
            col = index % COLUMNS
            self.grid_layout.addWidget(card, row, col)

    def filter_games(self, query):
        query = query.strip().lower()
        if self.is_discord_search and self.discord_cards:
            filtered = [c for c in self.discord_cards if query in c.game_name.lower()]
            self.rebuild_grid(filtered)
        else:
            filtered = [c for c in self.all_cards if query in c.game_name.lower()]
            self.rebuild_grid(filtered)

    def on_search_enter(self):
        query = self.search_bar.text().strip()
        if query:
            self.on_deep_search()

    def select_game(self, card: GameCard):
        if self.selected_card:
            self.selected_card.set_selected(False)
        self.selected_card = card
        self.selected_card.set_selected(True)
        source_tag =""
        self.status_label.setText(f"Ready: {card.game_name}{source_tag}")
        self.status_label.setStyleSheet("color: #ffffff; font-weight: bold; font-size: 12px;")
        self.launch_btn.setEnabled(True)

    def on_launch_clicked(self):
        if not self.selected_card:
            return

        game_name = self.selected_card.game_name
        rel_exe_path = self.selected_card.exec_path
        source = self.selected_card.source

        if not rel_exe_path:
            error_msg = "Empty executable path"
            self.status_label.setText(f"Error: {error_msg}")
            self.status_label.setStyleSheet("color: #ff5555; font-size: 12px;")
            log_error(error_msg, f"Game: {game_name}")
            return

        source_mfs = os.path.join(EXE_DIR, "Binaries", "Win64", "main.mfs")

        if not os.path.exists(source_mfs):
            error_msg = "Missing Binaries/Win64/main.mfs template!"
            self.status_label.setText(f"Error: {error_msg}")
            self.status_label.setStyleSheet("color: #ff5555; font-size: 12px;")
            log_error(error_msg, f"Game: {game_name}, Path: {source_mfs}")
            return

        try:
            if source == "github":
                clean_rel_path = os.path.normpath(rel_exe_path).lstrip(r"\/")
                target_exe = os.path.join(EXE_DIR, clean_rel_path)
                target_dir = os.path.dirname(target_exe)
                
            else:
                clean_rel_path = os.path.normpath(rel_exe_path).lstrip(r"\/")
                exe_filename = os.path.basename(clean_rel_path)
                exe_dir_part = os.path.dirname(clean_rel_path)
                
                safe_game_name = "".join(c for c in game_name if c.isalnum() or c in " -_")
                game_folder = os.path.join(EXE_DIR, safe_game_name)
                
                if exe_dir_part:
                    target_exe = os.path.join(game_folder, exe_dir_part, exe_filename)
                    target_dir = os.path.dirname(target_exe)
                else:
                    target_exe = os.path.join(game_folder, exe_filename)
                    target_dir = game_folder

            try:
                os.makedirs(target_dir, exist_ok=True)
            except OSError as e:
                error_msg = f"Failed to create directory: {str(e)}"
                self.status_label.setText(f"Error: Directory creation failed")
                self.status_label.setStyleSheet("color: #ff5555; font-size: 12px;")
                log_error(error_msg, f"Game: {game_name}, Target: {target_dir}")
                QMessageBox.critical(
                    self,
                    "Launch Error",
                    f"Failed to create directory:\n\n{target_dir}\n\nError: {str(e)}\n\nThis has been logged to error_log.txt"
                )
                return

            shutil.copy2(source_mfs, target_exe)
            subprocess.Popen([target_exe], cwd=target_dir)
            
            source_tag =""
            self.status_label.setText(f"Running Replica: {game_name}{source_tag}")
            self.status_label.setStyleSheet("color: #55ff55; font-size: 12px; font-weight: bold;")
            
        except shutil.Error as e:
            error_msg = f"File copy failed: {str(e)}"
            self.status_label.setText("Error: File copy failed")
            self.status_label.setStyleSheet("color: #ff5555; font-size: 12px;")
            log_error(error_msg, f"Game: {game_name}, Source: {source_mfs}, Target: {target_exe}")
            QMessageBox.critical(
                self,
                "Launch Error",
                f"Failed to copy template file:\n\n{str(e)}\n\nThis has been logged to error_log.txt"
            )
            
        except PermissionError as e:
            error_msg = f"Permission denied: {str(e)}"
            self.status_label.setText("Error: Permission denied")
            self.status_label.setStyleSheet("color: #ff5555; font-size: 12px;")
            log_error(error_msg, f"Game: {game_name}, Target: {target_exe}")
            QMessageBox.critical(
                self,
                "Launch Error",
                f"Permission denied:\n\n{str(e)}\n\nTry running as administrator or check file permissions.\n\nThis has been logged to error_log.txt"
            )
            
        except Exception as e:
            error_msg = f"{type(e).__name__}: {str(e)}"
            self.status_label.setText(f"Launch failed: {str(e)[:50]}...")
            self.status_label.setStyleSheet("color: #ff5555; font-size: 12px;")
            log_error(error_msg, f"Game: {game_name}, Source: {source}, Path: {rel_exe_path}")
            QMessageBox.critical(
                self,
                "Launch Error",
                f"Launch failed:\n\n{str(e)}\n\nThis has been logged to error_log.txt"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LauncherWindow()
    window.show()
    sys.exit(app.exec())