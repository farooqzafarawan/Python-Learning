import wx


class TreePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # initialize Tree Control
        self.tree = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, (200, 170),
                                wx.TR_HAS_BUTTONS)

        # create Tree Control using Create() method
        self.tree.Create
        # Add root to Tree Control
        self.root = self.tree.AddRoot('Root')

        # Add item to root
        itm = self.tree.AppendItem(self.root, 'Item')

        # Add item to 'itm'
        self.tree.AppendItem(itm, "Sub Item")

        # Expand whole tree
        self.tree.Expand(self.root)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        self.SetSizer(sizer)

    # Add another item to root
        itm = self.tree.AppendItem(self.root, 'Item 2')
        # Add item to 'itm'
        self.tree.AppendItem(itm, "Sub Item 2")


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='TreeCtrl Demo')
        panel = TreePanel(self)
        self.Show()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()
