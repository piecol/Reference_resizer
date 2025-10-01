import pcbnew
import wx
import os


class ResizeDialog(wx.Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, title="Resize Silk Text", size=(300, 200))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Reference field
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        lbl1 = wx.StaticText(panel, label="Reference height (mm):")
        self.ref_height = wx.TextCtrl(panel, value="1.2")
        hbox1.Add(lbl1, flag=wx.RIGHT, border=8)
        hbox1.Add(self.ref_height, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.ALL, border=8)

        # Value field
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        lbl2 = wx.StaticText(panel, label="Value height (mm):")
        self.val_height = wx.TextCtrl(panel, value="1.0")
        hbox2.Add(lbl2, flag=wx.RIGHT, border=8)
        hbox2.Add(self.val_height, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.ALL, border=8)

        # Checkbox
        self.include_values = wx.CheckBox(panel, label="Resize value fields too")
        vbox.Add(self.include_values, flag=wx.LEFT | wx.TOP, border=10)

        # Buttons
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(panel, wx.ID_OK, label="Apply")
        closeButton = wx.Button(panel, wx.ID_CANCEL, label="Cancel")
        hbox3.Add(okButton)
        hbox3.Add(closeButton, flag=wx.LEFT, border=5)
        vbox.Add(hbox3, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        panel.SetSizer(vbox)


class ResizeSilkReferences(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Resize Silk Text"
        self.category = "Modify PCB"
        self.description = "Resize reference (and optionally value) text on F.SilkS / B.SilkS"
        self.show_toolbar_button = True   # ✅ Show in toolbar

        # Path to icon (must be PNG, 32x32 works best)
        self.icon_file_name = os.path.join(
            os.path.dirname(__file__), "resize_silk_text.png"
        )

    def Run(self):
        dlg = ResizeDialog(None)
        if dlg.ShowModal() != wx.ID_OK:
            dlg.Destroy()
            return

        try:
            ref_height_mm = float(dlg.ref_height.GetValue())
            val_height_mm = float(dlg.val_height.GetValue())
            include_values = dlg.include_values.GetValue()
        except Exception as e:
            wx.MessageBox(f"Invalid input: {e}", "Error")
            dlg.Destroy()
            return

        dlg.Destroy()

        ref_height = pcbnew.FromMM(ref_height_mm)
        val_height = pcbnew.FromMM(val_height_mm)

        board = pcbnew.GetBoard()
        ref_count = 0
        val_count = 0

        for footprint in board.GetFootprints():
            # Reference field
            ref = footprint.Reference()
            if ref.IsVisible() and ref.GetLayer() in (pcbnew.F_SilkS, pcbnew.B_SilkS):
                ref.SetTextHeight(ref_height)
                ref.SetTextWidth(ref_height)
                ref_count += 1

            # Optional: Value field
            if include_values:
                val = footprint.Value()
                if val.IsVisible() and val.GetLayer() in (pcbnew.F_SilkS, pcbnew.B_SilkS):
                    val.SetTextHeight(val_height)
                    val.SetTextWidth(val_height)
                    val_count += 1

        pcbnew.Refresh()
        wx.MessageBox(
            f"Resized {ref_count} reference(s) and {val_count} value(s) on silkscreen.",
            "Done"
        )


ResizeSilkReferences().register()
