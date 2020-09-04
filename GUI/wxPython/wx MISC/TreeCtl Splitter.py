import wx


class MyTree(wx.TreeCtrl):
    '''Our customized TreeCtrl class    '''

    def __init__(self, parent, id, position, size, style):
        '''Initialize our tree '''
        wx.TreeCtrl.__init__(self, parent, id, position, size, style)
        root = self.AddRoot('Programmer')
        os = self.AppendItem(root, 'Operating Systems')
        pl = self.AppendItem(root, 'Programming Languages')
        tk = self.AppendItem(root, 'Toolkits')
        self.AppendItem(os, 'Linux')
        self.AppendItem(os, 'FreeBSD')
        self.AppendItem(os, 'OpenBSD')
        self.AppendItem(os, 'NetBSD')
        self.AppendItem(os, 'Solaris')
        cl = self.AppendItem(pl, 'Compiled languages')
        sl = self.AppendItem(pl, 'Scripting languages')
        self.AppendItem(cl, 'Java')
        self.AppendItem(cl, 'C++')
        self.AppendItem(cl, 'C')
        self.AppendItem(cl, 'Pascal')
        self.AppendItem(sl, 'Python')
        self.AppendItem(sl, 'Ruby')
        self.AppendItem(sl, 'Tcl')
        self.AppendItem(sl, 'PHP')
        self.AppendItem(tk, 'Qt')
        self.AppendItem(tk, 'MFC')
        self.AppendItem(tk, 'wxPython')
        self.AppendItem(tk, 'GTK+')
        self.AppendItem(tk, 'Swing')


class MyFrame(wx.Frame):
    ''' Our customized window class '''

    def __init__(self, parent, id, title):
        '''Initialize our window '''
        wx.Frame.__init__(self, parent, id, title,
                          wx.DefaultPosition, wx.Size(450, 350))

        # Create a splitter window
        self.splitter = wx.SplitterWindow(self, -1)

        # Create the left panel
        leftPanel = wx.Panel(self.splitter, -1)
        # Create a box sizer that will contain the left panel contents
        leftBox = wx.BoxSizer(wx.VERTICAL)

        # Create our tree and put it into the left panel
        self.tree = MyTree(leftPanel, 1, wx.DefaultPosition, (-1, -1),
                           wx.TR_HIDE_ROOT | wx.TR_HAS_BUTTONS)

        # Add the tree to the box sizer
        leftBox.Add(self.tree, 1, wx.EXPAND)

        # Bind the OnSelChanged method to the tree
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, id=1)

        # Set the size of the right panel to that required by the tree
        leftPanel.SetSizer(leftBox)

        # Create the right panel
        rightPanel = wx.Panel(self.splitter, -1)
        # Create the right box sizer that will contain the panel's contents
        rightBox = wx.BoxSizer(wx.VERTICAL)
        # Create a widget to display static text and store it in the right
        # panel
        self.display = wx.StaticText(rightPanel, -1, '', (10, 10),
                                     style=wx.ALIGN_CENTRE)
        # Add the display widget to the right panel
        rightBox.Add(self.display, -1, wx.EXPAND)
        # Set the size of the right panel to that required by the
        # display widget
        rightPanel.SetSizer(rightBox)
        # Put the left and right panes into the split window
        self.splitter.SplitVertically(leftPanel, rightPanel)
        # Create the window in the centre of the screen
        self.Centre()

    def OnSelChanged(self, event):
        '''Method called when selected item is changed '''
        # Get the selected item object
        item = event.GetItem()
        # Display the selected item text in the text widget
        self.display.SetLabel(self.tree.GetItemText(item))


class MyApp(wx.App):
    def OnInit(self):
        '''Initialize by creating the split window with the tree '''
        frame = MyFrame(None, -1, 'treectrl.py')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True


if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()
