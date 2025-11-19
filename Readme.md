![Quests Hunter Advertisement Poster - Skip the Downloads](https://raw.githubusercontent.com/P1sco/QuestHunter/refs/heads/main/Assets/QuestHunter.png)

### 🎮 Quests Hunter: Lightweight Launcher for Discord Quests

A simple, open-source **Python GUI application** that fetches and launches virtual game profiles, allowing users to complete Discord Quests without downloading full games. It works by emulating the required local file structure and launching a placeholder executable with the correct Discord Application ID.

---

### Repository & Downloads

| Button | Link | Purpose |
| :--- | :--- | :--- |
| [🚀 **Download Latest Release (ZIP)**](https://github.com/P1sco/QuestHunter/releases/download/1.2.1.0/QuestHunter-v1.2.1.zip) | `https://github.com/P1sco/QuestHunter/releases/latest/download/QuestHunter-v1.2.1.zip` | Direct link to the latest packaged release. |
| [⭐ **Star QuestHunter on GitHub**](https://github.com/P1sco/QuestHunter) | `https://github.com/P1sco/QuestHunter` | Encourages support and helps project visibility. |
| [💖 **Donate via PayPal**](https://paypal.me/Oelbahy) | `https://paypal.me/Oelbahy` | Direct link for financial support. |

---


### ✨ Features

* **⚡ Lightweight & Fast:** Minimal footprint, no large game downloads required.
* **🖼️ Dynamic Launcher:** Fetches the latest quest data (images and links) from a remote HTML source (`www.questhunter.dev/Data-Feed/index.html`).
* **🛠️ Emulated Launch:** Automatically creates the necessary folder structure (`Binaries/Win64/...`) and copies placeholder files (`main.mfs`, `source.mui`) to successfully spoof game presence to Discord.
* **🛡️ Open Source:** Fully transparent and auditable code base.

---

### ⚠️ Disclaimer & Important Notice

> This software is intended for educational and convenience purposes only. Use it responsibly and understand that using any software to bypass intended game requirements may violate Discord's Terms of Service. **Use at your own risk.** The authors are not responsible for any actions taken against your Discord account.

---

### ⬇️ Installation

You can run this utility either by downloading the compiled executable (Recommended for ease of use) or by running it directly from the Python source code.

#### 1. Pre-compiled Executable (Recommended for Windows)

1.  Go to the [**Releases Page**](https://github.com/P1sco/QuestHunter/releases/tag/1.2.1.0).
2.  Download the latest executable file (e.g., `QuestHunter.exe` or the corresponding ZIP file).
3.  Extract the contents to a location of your choice.
4.  Proceed to **Usage** step 2.

#### 2. From Source

*This method requires [Python 3](https://www.python.org/downloads/) and the necessary libraries.*

1.  **Install Required Libraries:** Open your terminal or command prompt and run:
    ```bash
    pip install requests beautifulsoup4 Pillow
    ```
2.  Clone the repository:
    ```bash
    git clone [https://github.com/P1sco/QuestHunter](https://github.com/P1sco/QuestHunter)
    cd QuestHunter
    ```
3.  **Critical Step: Create Template Files**
    The launcher requires two placeholder files in a specific directory to perform the necessary file copying for emulation:
    * Create a directory structure: `Binaries/Win64/en-US`
    * Place your placeholder files here:
        * `Binaries/Win64/en-US/source.mui`
    * Compile and Executable of Gif.py to main.exe and rename it to main.mfs and plac it here:
        * `Binaries/Win64/main.mfs`
    > **Note:** These files should be the lightweight stub files you intend to use for the emulation process.

---

### 🚀 Usage

#### 1. Launch the Application

* **If using the executable:** Double-click the downloaded `QuestHunter.exe` file.
* **If running from source:**
    ```bash
    python questHunter.py
    ```

#### 2. Using the GUI

1.  The **Quests Hunter** window will appear. It will attempt to connect to the remote server to fetch the latest quest banners and game links.
2.  **Click on Run Replica** corresponding to the game you need to emulate.
3.  The application will automatically handle file creation, copying, and launching the placeholder executable to successfully spoof your game presence to Discord.
4.  **Keep the console window and the launched process running** until your Discord Quest progress updates (typically 15-30 minutes of "playtime").
5.  Once the quest is complete, you can safely close the launched process and the **Quests Hunter** application.

---

### 💖 Support the Developer

If you find Quests Hunter useful and would like to support its continued development and maintenance, any tips or donations are greatly appreciated!

* **PayPal:** [paypal.me/Oelbahy](https://paypal.me/Oelbahy)

---

### 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---

### 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

### ✉️ Contact

Pisco - [https://github.com/P1sco/](https://github.com/P1sco/)
Project Link: [https://github.com/P1sco/QuestHunter](https://github.com/P1sco/QuestHunter)

---
