#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.5 on Tue Jun 18 16:55:32 2013

import string
import threading
import wx
from mega import Mega
import os

# begin wxGlade: extracode
# end wxGlade

# end of class MyMenuBar1
class MyFrame2(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame2.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.frame_2_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(2, "Quit", "", wx.ITEM_NORMAL)
        self.frame_2_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(4, "Generate tree", "", wx.ITEM_NORMAL)
        self.frame_2_menubar.Append(wxglade_tmp_menu, "Inne")
        self.SetMenuBar(self.frame_2_menubar)
        # Menu Bar end
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)
        self.button_1 = wx.Button(self.notebook_1_pane_1, -1, "Upload File")
        self.gauge_1 = wx.Gauge(self.notebook_1_pane_1, -1, 100)
        self.button_3 = wx.Button(self.notebook_1_pane_1, -1, "Upload Directory")
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)
        self.tree_ctrl_1 = wx.TreeCtrl(self.notebook_1_pane_2, -1, style=wx.TR_HAS_BUTTONS | wx.TR_NO_LINES | wx.TR_DEFAULT_STYLE | wx.SUNKEN_BORDER)
        self.button_6 = wx.Button(self.notebook_1_pane_2, -1, "Download")
        self.label_3 = wx.StaticText(self.notebook_1_pane_2, -1, "label_3")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.Click_Quit, id=2)
        self.Bind(wx.EVT_MENU, self.generate_tree, id=4)
        self.Bind(wx.EVT_BUTTON, self.upload_file, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.upload_directory, self.button_3)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.zmiana, self.tree_ctrl_1)
        self.Bind(wx.EVT_BUTTON, self.download_tree, self.button_6)
        # end wxGlade




    def __set_properties(self):
        # begin wxGlade: MyFrame2.__set_properties
        self.SetTitle(u"Główne menu")
        self.SetSize((447, 362))
        self.gauge_1.SetMinSize((200, 28))
        self.button_3.Enable(False)
        self.tree_ctrl_1.SetMinSize((325, 305))
        self.button_6.SetMinSize((119, 27))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame2.__do_layout
        grid_sizer_2 = wx.GridSizer(1, 1, 0, 0)
        grid_sizer_5 = wx.FlexGridSizer(1, 2, 0, 0)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_3 = wx.GridSizer(3, 2, 0, 0)
        grid_sizer_3.Add(self.button_1, 0, 0, 0)
        grid_sizer_3.Add(self.gauge_1, 0, 0, 0)
        grid_sizer_3.Add(self.button_3, 0, 0, 0)
        self.notebook_1_pane_1.SetSizer(grid_sizer_3)
        grid_sizer_5.Add(self.tree_ctrl_1, 1, wx.EXPAND, 0)
        sizer_4.Add(self.button_6, 0, 0, 0)
        sizer_4.Add(self.label_3, 0, 0, 0)
        grid_sizer_5.Add(sizer_4, 1, wx.EXPAND, 0)
        self.notebook_1_pane_2.SetSizer(grid_sizer_5)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "Upload")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "tab2")
        grid_sizer_2.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(grid_sizer_2)
        self.Layout()
        self.SetSize((447, 362))
        # end wxGlade


    def myupdater(self, current, total):
        m = 100 * current / total
        print(m)
        self.gauge_1.SetValue(m)
        wx.Yield()
        

    def uploading(self, path):
        mega.upload(path, callback=self.myupdater)
        self.button_1.Enable(True)

    def upload_file(self, event):  # wxGlade: MyFrame2.<event_handler>
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            mypath = os.path.basename(path)
        self.button_1.Enable(False)
        t = threading.Thread(target=self.uploading, args=(path,))
        t.start()

    def upload_directory(self, event):  # wxGlade: MyFrame2.<event_handler>
        print "Event handler `upload_directory' not implemented"
        event.Skip()

    def subtree(self, folder_id, files, root, again=None):
        if again:
            print("dasd")
        else:
            list_id=0
            nono=[]

        image_list = wx.ImageList(16, 16)
        folder_icon = image_list.Add(wx.Image("images/Folder-icon.png", wx.BITMAP_TYPE_PNG).Scale(16,16).ConvertToBitmap())
        self.tree_ctrl_1.AssignImageList(image_list)
        table = []
        table_a = []
        table_file = []
        table_id = 0
        for folder in files.items():
            if folder[1]['h'] == folder_id:
                folder_name = folder[1]['a']['n']
        print folder_name

        for folder2 in files.items():
            if folder2[1]['p'] == folder_id and folder2[1]['t'] == 1:
                table.append(folder2[1]['a']['n'])
                table_id = table_id + 1

        table.sort()

        print table

        for a in range (0,table_id):
            for folder3 in files.items():
                if folder3[1]['p'] == folder_id and folder3[1]['t'] == 1 and folder3[1]['a']['n'] == table[a]:
                    table_a.append(folder3[1]['h'])
        moje = folder_id + '_tree'
        print (moje)

        if table_id == 0:
            for folder4 in files.items():
                if folder4[1]['t'] == 0 and folder4[1]['p'] == folder_id:
                    xyz = self.tree_ctrl_1.AppendItem(root, folder4[1]['a']['n'])
                    self.tree_ctrl_1.SetPyData(xyz, folder4[1]['h'])
                    print folder4[1]['a']['n']

        for c in range (0,table_id):
            abc = self.tree_ctrl_1.AppendItem(root, table[c])
            self.tree_ctrl_1.SetPyData(abc, table_a[c] + " folder")
            self.tree_ctrl_1.SetItemImage(abc, folder_icon, wx.TreeItemIcon_Normal)
            self.subtree(table_a[c], files, abc, again="yes")
            if c == (table_id - 1):
                for folder4 in files.items():
                    if folder4[1]['t'] == 0 and folder4[1]['p'] == folder_id:

                        xyz = self.tree_ctrl_1.AppendItem(root, folder4[1]['a']['n'])
                        self.tree_ctrl_1.SetPyData(xyz, folder4[1]['h'] + " file")
                        print folder4[1]['a']['n']

            

    def generate_tree(self, event):  # wxGlade: MyFrame2.<event_handler>
        print "Event handler `generate_tree' not implemented"
        files = mega.get_files()
        for folder in files.items():
            if folder[1]['t'] == 2:
                a = folder[1]
        print (a['h'])
        moje = a['h'] + '_tree'
        print (moje)
        root = self.tree_ctrl_1.AddRoot(a['a']['n'])
        self.subtree(a['h'], files, root)


    def tree_download(self, event):  # wxGlade: MyFrame2.<event_handler>
        print "Event handler `tree_download' not implemented"
        item = self.tree_ctrl_1.GetSelection()
        print (self.tree_ctrl_1.GetItemText(item))
        event.Skip()

    def zmiana(self, event):  # wxGlade: MyFrame2.<event_handler>
        m = self.tree_ctrl_1.GetPyData(event.GetItem())
        self.label_3.SetLabel(m)

        event.Skip()

    def folder_download_id(self, folderid, download_location):
        mega.download_folder(foldernameorid=folderid, download_location=download_location, using="id", files=None)
        self.button_6.Enable(True)

    def file_download_id(self, fileid, download_location):
        files = mega.get_files()
        for file in files.items():
            if file[1]['a'] and file[1]['h'] == fileid:
                mega.download(file, download_location)
        self.button_6.Enable(True)

    def Click_Quit(self, event):  # wxGlade: MyFrame2.<event_handler>
        self.Close(1)

    def download_tree(self, event):  # wxGlade: MyFrame2.<event_handler>
        
        dialog = wx.DirDialog(None, "Choose a directory:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.button_6.Enable(False)
            print dialog.GetPath()
            path = dialog.GetPath()
            print self.label_3.GetLabel()
            i_d = self.label_3.GetLabel()
            i_d = i_d.split()
            print i_d[1]
            if i_d[1] == "folder":
                t = threading.Thread(target=self.folder_download_id, args=(i_d[0], path))
            if i_d[1] == "file":
                t = threading.Thread(target=self.file_download_id, args=(i_d[0], path))
            t.start()

  #      mega.download_folder(foldernameorid=self.label_3.GetLabel(), download_location=path, using="id", files=None)
        dialog.Destroy()
        event.Skip()


# end of class MyFrame2
class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, -1, "Login")
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "")
        self.label_2 = wx.StaticText(self, -1, "Password")
        self.text_ctrl_2 = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
        self.panel_1 = wx.Panel(self, -1)
        self.button_2 = wx.Button(self, -1, "Login")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.Login, self.button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Logowanie")
        self.SetSize((401, 140))
        self.text_ctrl_1.SetMinSize((200, 26))
        self.text_ctrl_2.SetMinSize((200, 26))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        grid_sizer_4 = wx.FlexGridSizer(2, 2, 0, 0)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.label_1, 0, 0, 0)
        sizer_2.Add(self.text_ctrl_1, 0, 0, 0)
        grid_sizer_4.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_3.Add(self.label_2, 0, 0, 0)
        sizer_3.Add(self.text_ctrl_2, 0, 0, 0)
        grid_sizer_4.Add(sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.panel_1, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.button_2, 0, wx.ALIGN_RIGHT, 0)
        self.SetSizer(grid_sizer_4)
        self.Layout()
        self.SetSize((401, 140))
        # end wxGlade

    def Quit(self, event):  # wxGlade: MyFrame.<event_handler>
            dlg = wx.MessageDialog(self,"Do you really want to close this application?","Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_OK:
                self.Destroy()

    def Login(self, event):  # wxGlade: MyFrame.<event_handler>
        udalosie=0
        m = mega.login(self.text_ctrl_1.GetValue(), self.text_ctrl_2.GetValue())
        if(m):
            print("Zalogowany")
            self.button_2.Disable()
            
            frame_1.Close(1)
            frame_2.Show()

# end of class MyFrame
if __name__ == "__main__":
    mega = Mega({'verbose': True})
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    frame_2 = MyFrame2(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()