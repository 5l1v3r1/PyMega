#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.5 on Tue Jun 18 16:55:32 2013

import threading
import wx
from mega import Mega
import os
from decimal import Decimal
# begin wxGlade: extracode
# end wxGlade

class MyFrame2(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame2.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)
        self.button_1 = wx.Button(self.notebook_1_pane_1, -1, "Upload File")
        self.gauge_1 = wx.Gauge(self.notebook_1_pane_1, -1, 100)
        self.button_3 = wx.Button(self.notebook_1_pane_1, -1, "Upload Directory")
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.upload_file, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.upload_directory, self.button_3)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame2.__set_properties
        self.SetTitle(u"Główne menu")
        self.SetSize((447, 362))
        self.gauge_1.SetMinSize((200, 28))
        self.button_3.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame2.__do_layout
        grid_sizer_2 = wx.GridSizer(1, 1, 0, 0)
        grid_sizer_3 = wx.GridSizer(3, 2, 0, 0)
        grid_sizer_3.Add(self.button_1, 0, 0, 0)
        grid_sizer_3.Add(self.gauge_1, 0, 0, 0)
        grid_sizer_3.Add(self.button_3, 0, 0, 0)
        self.notebook_1_pane_1.SetSizer(grid_sizer_3)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "tab1")
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



# end of class MyFrame2
class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, -1, "Login", style=wx.ALIGN_CENTRE)
        self.label_2 = wx.StaticText(self, -1, u"Hasło\n", style=wx.ALIGN_CENTRE)
        self.panel_1 = wx.Panel(self, -1)
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "")
        self.text_ctrl_2 = wx.TextCtrl(self, -1, "", style=wx.TE_PASSWORD)
        self.panel_2 = wx.Panel(self, -1)
        self.panel_3 = wx.Panel(self, -1)
        self.panel_4 = wx.Panel(self, -1)
        self.button_2 = wx.Button(self, -1, "Logowanie")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.Login, self.button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Logowanie")
        self.label_1.SetBackgroundColour(wx.Colour(242, 241, 240))
        self.label_2.SetBackgroundColour(wx.Colour(242, 241, 240))
        self.panel_1.SetBackgroundColour(wx.Colour(242, 241, 240))
        self.panel_2.SetBackgroundColour(wx.Colour(242, 241, 240))
        self.panel_3.SetBackgroundColour(wx.Colour(242, 241, 240))
        self.panel_4.SetBackgroundColour(wx.Colour(242, 241, 240))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        grid_sizer_1 = wx.GridSizer(3, 3, 0, 0)
        grid_sizer_1.Add(self.label_1, 0, 0, 0)
        grid_sizer_1.Add(self.label_2, 0, 0, 0)
        grid_sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.text_ctrl_1, 0, 0, 0)
        grid_sizer_1.Add(self.text_ctrl_2, 0, 0, 0)
        grid_sizer_1.Add(self.panel_2, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.panel_3, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.panel_4, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.button_2, 0, 0, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self)
        self.Layout()
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
