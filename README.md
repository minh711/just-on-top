# Just on Top

Open-source Python application for display a text always on top

![image](https://github.com/user-attachments/assets/f03032ef-8f94-4060-b910-241e1dfde547)

## Development

### 1. Virtual environment

Create a virtual environment in project folder:

```bash
python3 -m venv venv
```

Activate the virtual environment

```bash
source venv/bin/activate
```

or for Windows

```bash
.\venv\Scripts\Activate.ps1
```

Check if it activated

```bash
which python3
```

or for Windows

```bash
python -c "import sys; print(sys.executable)"
```

If the directory shows the current project folder, it means it activated.

### 2. Install packages

Run this to install packages needed

```bash
pip install -r requirements.txt
```

## Notes

### Change icon

Go to where the package placed:

```bash
customtkinter\assets\icons
```

Then replace the default `.ico` file with a different one with the same name.

## Deployment

Script:

```bash
pyinstaller --noconsole --onefile main.py --icon=assets/jot_icon.ico --add-data "themes/dark_theme.json;themes" --add-data "themes/light_theme.json;themes"
```
