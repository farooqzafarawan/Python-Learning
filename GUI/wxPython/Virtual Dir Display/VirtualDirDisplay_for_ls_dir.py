import wx
#import images  # from wxPython.py-at-2004
import string
import ls_file_parser


class MyTreeCtrl(wx.TreeCtrl):
	def __init__(self, parent, id, pos, size, style):
		wx.TreeCtrl.__init__(self, parent, id, pos, size, style)

	def OnCompareItems(self, item1, item2):
		t1 = self.GetItemText(item1)
		t2 = self.GetItemText(item2)
		#self.log.WriteText('compare: ' + t1 + ' <> ' + t2 + '\n')
		if t1 < t2:
			return -1
		if t1 == t2:
			return 0
		return 1


class TreeCtrlPanel(wx.Panel):

	def __init__(self, parent, filename):
	  # Use the WANTS_CHARS style so the panel doesn't eat the Return key.
	  wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)
	  wx.EVT_SIZE(self, self.OnSize)

	  tID = wx.NewId()

	  self.tree = MyTreeCtrl(self, tID, wx.DefaultPosition, wx.DefaultSize,
                          wx.TR_HAS_BUTTONS | wx.TR_EDIT_LABELS,  # | wx.TR_MULTIPLE
                          #| wx.TR_HIDE_ROOT
                          )

	  isz = (16, 16)
	  il = wx.ImageList(isz[0], isz[1])
	  # wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, isz) -> wx.ArtProvider.GetBitmap()/3
	  self.folderIdx = il.Add(wx.ArtProvider.GetBitmap(
              wx.ART_FOLDER,      wx.ART_OTHER, isz))
	  self.folderOpenIdx = il.Add(wx.ArtProvider.GetBitmap(
              wx.ART_FILE_OPEN,   wx.ART_OTHER, isz))
	  self.fileIdx = il.Add(wx.ArtProvider.GetBitmap(
              wx.ART_REPORT_VIEW, wx.ART_OTHER, isz))
	  #self.fileIdx  = self.il.Add(images.getFile1Bitmap())
	  #self.smileidx = self.il.Add(images.getSmilesBitmap())

	  self.tree.SetImageList(il)
	  self.il = il

	  # NOTE: 1 tree items have to have a data object in order to be sorted.
	  #       2 Since our compare just uses the labels we don't need real data, so we'll just
	  # use None below for the item data.

	  wx.EVT_TREE_ITEM_EXPANDED(self, tID, self.OnItemExpanded)
	  wx.EVT_TREE_ITEM_COLLAPSED(self, tID, self.OnItemCollapsed)
	  wx.EVT_TREE_SEL_CHANGED(self, tID, self.OnSelChanged)
	  wx.EVT_TREE_BEGIN_LABEL_EDIT(self, tID, self.OnBeginEdit)
	  wx.EVT_TREE_END_LABEL_EDIT(self, tID, self.OnEndEdit)
	  wx.EVT_TREE_ITEM_ACTIVATED(self, tID, self.OnActivate)

	  wx.EVT_LEFT_DCLICK(self.tree, self.OnLeftDClick)
	  wx.EVT_RIGHT_DOWN(self.tree, self.OnRightClick)
	  wx.EVT_RIGHT_UP(self.tree, self.OnRightUp)

	  #?? wx.EVT_COMMAND(self, 103,103, self.OnFileOpened) # Newer wxWidgets has no EVT_COMMAND
	  # load default tree
	  if filename != "":
	    self.reload_tree(filename)

	def OnFileOpened(self, evt):
	  print( "FileOpened [pressed]" )
	  self.reload_tree(self.path)

	def reload_tree(self, lar_file):
	  self.lar_file = lar_file  # file to browse
	  #self.load_tree_test_data()
	  self.load_tree_laRfile()
	  self.tree.Expand(self.root)

	def load_tree_laRfile(self):
	  self.tree.DeleteAllItems()
	  self.lar = ls_file_parser.lslaRfile(self.lar_file)
	  # Set root item
	  self.root = self.tree.AddRoot(self.lar.root_dir)
	  self.tree.SetPyData(self.root, self.lar.root_dir)
	  self.tree.SetItemImage(self.root, self.folderIdx, wx.TreeItemIcon_Normal)
	  self.tree.SetItemImage(self.root, self.folderOpenIdx,
	                         wx.TreeItemIcon_Expanded)
	  curdir = self.lar.root_dir
	  print(" root dir=", curdir)
	  self.loadsubitems2(self.root, curdir)

	def loadsubitems2(self, rt_item, dir):
	  ls = self.lar.lso(dir)
	  for f in ls:
	      name = f[-1]
	      if name == '.' or name == '..':
	          continue
	      child = self.tree.AppendItem(rt_item, name)
	      path = self.lar.join_path(dir, name)
	      self.tree.SetPyData(child, path)
	      if self.lar.is_dir2(dir, name):
	      	self.tree.SetItemImage(child, self.folderIdx, wx.TreeItemIcon_Normal)
	      	self.tree.SetItemImage(child, self.folderOpenIdx,
	      	                       wx.TreeItemIcon_Expanded)
	      else:
	      	self.tree.SetItemImage(child, self.fileIdx, wx.TreeItemIcon_Normal)
	      	self.tree.SetItemImage(child, self.fileIdx, wx.TreeItemIcon_Expanded)

	      if not self.lar.is_dir2(dir, name):
	          continue
	      ls2 = self.lar.lso(path)
	      for f2 in ls2:
	        name2 = f2[-1]
	        if name2 == '.' or name2 == '..':
	            continue
	        item = self.tree.AppendItem(child, name2)
	        path2 = self.lar.join_path(path, name2)
	        self.tree.SetPyData(item, path2)
	        self.tree.SetItemImage(item, self.folderIdx, wx.TreeItemIcon_Normal)
	        self.tree.SetItemImage(item, self.folderOpenIdx,
	                               wx.TreeItemIcon_Expanded)

	def OnRightClick(self, event):
	  pt = event.GetPosition()
	  item, flags = self.tree.HitTest(pt)
	  #self.log.WriteText("OnRightClick: %s, %s, %s\n" % (self.tree.GetItemText(item), type(item), item.__class__))
	  self.tree.SelectItem(item)

	def OnRightUp(self, event):
	  pt = event.GetPosition()
	  item, flags = self.tree.HitTest(pt)
	  #self.log.WriteText("OnRightUp: %s (manually starting label edit)\n"  % self.tree.GetItemText(item))
	  self.tree.EditLabel(item)

	def OnBeginEdit(self, event):
	  # show how to prevent edit...
	  if self.tree.GetItemText(event.GetItem()) == "The Root Item":
	    wx.Bell()
	    #self.log.WriteText("You can't edit this one...\n")

	    # Lets just see what's visible of its children
	    cookie = 0
	    root = event.GetItem()
	    (child, cookie) = self.tree.GetFirstChild(root, cookie)
	    while child.IsOk():
	      #self.log.WriteText("Child [%s] visible = %d" %
	      #                     (self.tree.GetItemText(child),
	      #                      self.tree.IsVisible(child)))
	      (child, cookie) = self.tree.GetNextChild(root, cookie)

	    event.Veto()

	def OnEndEdit(self, event):
	  #self.log.WriteText("OnEndEdit\n")
	  # show how to reject edit, we'll not allow any digits
	  for x in event.GetLabel():
	    if x in string.digits:
	      #self.log.WriteText("You can't enter digits...\n")
	      event.Veto()
	      return

	def OnLeftDClick(self, event):
	  pt = event.GetPosition()
	  item, flags = self.tree.HitTest(pt)
	  #self.log.WriteText("OnLeftDClick: %s\n" % self.tree.GetItemText(item))
	  parent = self.tree.GetItemParent(item)
	  self.tree.SortChildren(parent)
	  event.Skip()

	def OnSize(self, event):
	  w, h = self.GetClientSize()
	  self.tree.SetDimensions(0, 0, w, h)

	def OnItemExpanded(self, event):
	  item = event.GetItem()
	  #self.log.WriteText("OnItemExpanded: %s\n" % self.tree.GetItemText(item))
	  self.tree.DeleteChildren(item)
	  dir = self.tree.GetPyData(item)
	  assert(dir)
	  self.loadsubitems2(item, dir)

	def OnItemCollapsed(self, event):
	  item = event.GetItem()
	  #self.log.WriteText("OnItemCollapsed: %s\n" % self.tree.GetItemText(item))

	def OnSelChanged(self, event):
	  self.item = event.GetItem()
	  #-self.log.WriteText("OnSelChanged: %s\n" % self.tree.GetItemText(self.item))
	  #items = self.tree.GetSelections()
	  #print map(self.tree.GetItemText, items)
	  #
	  self.listpanel = self.GetParent().GetWindow2()

	  path = self.tree.GetPyData(self.item)
	  #self.log.WriteText("pwd: '%s'\n" % path)
	  self.RePopulateList(path)

	  event.Skip()

	def RePopulateList(self, dirpath):
	  self.listpanel.GetListCtrl().DeleteAllItems()
	  if not self.lar.is_dir(dirpath):
	    print(" //path: "+dirpath+" is not dir\n")
	    return
	  ls = self.lar.lso(dirpath)
	  for f in ls:
	    name = f[-1]
	    if name == '.' or name == '..':
	        continue
	    self.listpanel.AppendItem(name)

	def OnActivate(self, event):
	    pass
            #self.log.WriteText("OnActivate: %s\n" % self.tree.GetItemText(self.item))


def create_treectl_panel(parent, fname):
	return TreeCtrlPanel(parent, fname)


class tApp(wx.App):
    Win_title = "TreePanel"

    def __init__(self, create_win, fname):
        self.create_window = create_win
        self.fname = fname
        wx.App.__init__(self, 0)

    def OnInit(self):
        frame = wx.Frame(None, -1, tApp.Win_title, pos=(50, 50), size=(0, 0),
                         style=wx.NO_FULL_REPAINT_ON_RESIZE | wx.DEFAULT_FRAME_STYLE)
        frame.CreateStatusBar()
        #frame.SetMenuBar(menuBar)
        #win = create_window(frame, frame, None, fname)
        win = self.create_window(frame, self.fname)
        frame.Show(True)

        # so set the frame to a good size for showing stuff
        frame.SetSize((640, 480))
        win.SetFocus()

        self.SetTopWindow(frame)
        self.frame = frame
        return True


if __name__ == '__main__':
	import sys
	import os
	fname = r'D:\Wikipedia\markdown'
	app = tApp(create_treectl_panel, fname)
	app.MainLoop()
