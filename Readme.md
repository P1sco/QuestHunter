# QuestHunter

A tool that lets you complete Discord Quests without downloading entire games. It fakes the game files Discord looks for, so you can get your rewards without wasting storage space.

## Real Talk

**This is a proof-of-concept tool.** It emulates game presence by creating the folder structure Discord expects and running a placeholder executable.

**Use it at your own risk.** I'm not responsible if Discord decides to take action against your account. That said, I've been using it myself for a while without issues—just don't be stupid about it.

## Downloads

| What | Link |
|------|------|
| Latest Release | [Download Here](https://github.com/P1sco/QuestHunter/releases/download/v2.1.0/QuestHunter.v2.1.0.zip) |
| Star the Repo | [GitHub](https://github.com/P1sco/QuestHunter) |
| Buy me a coffee | [PayPal](https://paypal.me/Oelbahy) |

## What It Does

- **Lightweight** – No 100GB downloads. Just a tiny executable.
- **Emulates game presence** – Creates the exact folder structure for the games Discord checks for.
- **Open source** – You can read every line of code yourself.

## How to Use

### Option 1: Download the EXE (Easiest)

1. Go to the [Releases Page](https://github.com/P1sco/QuestHunter/releases)
2. Download `QuestHunter.exe` (or the latest ZIP)
3. Extract it somewhere you'll remember
4. Run `QuestHunter.exe`

### Option 2: Run from Source

If you prefer running Python directly:

```bash
# Install dependencies
pip install PyQt6

# Clone the repo
git clone https://github.com/P1sco/QuestHunter
cd QuestHunter

# Run it
python questHunter.py
```

** One extra step for source users:** You need to create the `main.mfs` file that the launcher copies and rename it to main.mfs and move it to /Binaries/Win64/.

1. Package `gif.py` into an executable:
   ```bash
   pyinstaller --onefile --noconsole gif.py
   ```

### Actually Using the Tool

1. Open QuestHunter
2. It'll fetch the latest quests from the feed
3. Pick the game you want, click "Launch Replica"
4. The tool creates all the fake files Discord looks for
5. Keep it running for 15 minutes
6. Check your Discord quest progress—it should count up
7. Close everything when you're done

## FAQ

**Q: Will I get banned?**
A: Most likely not, but it's technically against Discord's ToS.

**Q: Why not just download the actual game?**
A: Some of these games are 100GB+. Not everyone has that kind of storage or bandwidth.

**Q: Is this a virus?**
A: It's open source—check the code yourself. No weird network activity, no data collection. Just Python.

**Q: What's the "Deep Search" feature?**
A: If a game isn't in the main feed, click "Deep Search" and it'll pull data straight from Discord's own database. Works for pretty much any detectable game.

## Building Your Own Version

If you want to modify it:

```bash
git clone https://github.com/P1sco/QuestHunter
cd QuestHunter
# Make your changes
python questHunter.py
```

To build the EXE:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed questHunter.py
```

## Support

If this saved you from downloading 200GB of games, feel free to [buy me a coffee](https://paypal.me/Oelbahy). Or just star the repo—that helps too.

## 📄 License

MIT License—use it, modify it, do whatever.

---
