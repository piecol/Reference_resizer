<img width="64" height="64" alt="resize_silk_text" src="https://github.com/user-attachments/assets/056d83e3-8ee5-46fe-9741-2336cf1fbf9b" />

# Reference resizer (KiCad 9 Plugin)
This KiCad 9 plugin resizes all **reference designators** on the **silkscreen layers (F.SilkS / B.SilkS)** to a consistent size.  
It helps enforce readability and board design rules without manually editing each footprint.

---

## ✨ Features
- Resizes **all reference texts** on the silkscreen layers.
- Allows you to set a consistent **text height** and **thickness**.
- Works only on external layers (F.SilkS and B.SilkS).
- Easy to run via **External Plugins** menu or a toolbar icon in KiCad PCB Editor.


https://github.com/user-attachments/assets/ac3c7b87-9c3b-4907-8248-4fca15c36ec1


---

## 📂 Installation

1. Locate your KiCad 9 plugin folder. Typical locations:
   - **Linux:** `~/.local/share/kicad/9.0/plugins/`
   - **Windows:** `%APPDATA%\kicad\9.0\plugins\`
     (usually `C:\Users\<YourName>\AppData\Roaming\kicad\9.0\plugins\`)
   - **macOS:** `~/Library/Preferences/kicad/9.0/scripting/plugins/`

2. Copy the files into that folder:

resize_silk_text.py

resize_silk_text.png

resize_silk_text.pyplugin

```swift
~/Library/Preferences/kicad/9.0/scripting/plugins/
 └── resize_silk_refs/
     ├── resize_silk_text.py
     ├── resize_silk_text.pyplugin
     └── resize_silk_text.png
```


4. Restart **KiCad PCB Editor**.

---

## ▶️ Usage

1. Open your board in **KiCad PCB Editor**.
2. Go to:
- **Tools → External Plugins → Resize Silk References**
- or click the <img width="32" height="32" alt="resize_silk_text" src="https://github.com/user-attachments/assets/056d83e3-8ee5-46fe-9741-2336cf1fbf9b" />
 toolbar button.
3. The plugin will:
- Scan all footprints
- Resize their reference designator text on **F.SilkS** and **B.SilkS**

---

## ⚙️ Configuration
Inside the script you can adjust:
```python
NEW_HEIGHT = pcbnew.FromMM(1.0)     # Reference height
NEW_WIDTH  = pcbnew.FromMM(0.15)    # Reference line thickness
