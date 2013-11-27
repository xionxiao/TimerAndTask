# -*- coding: utf-8 -*-
import wx

class TaskBarIcon(wx.TaskBarIcon):
    def __init__(self, frame=None):
        wx.TaskBarIcon.__init__(self)
        icon = wx.Icon('favicon.ico', wx.BITMAP_TYPE_ICO)
        self.__frame = frame
        self.SetIcon(icon, u"番茄时钟")
        self.__menu = self.CreatePopupMenu()
        # Popup menu when right click
        self.Bind(wx.EVT_TASKBAR_RIGHT_UP, self.__OnTaskBarRight)
        # Open mainframe when double click
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.__OnTaskBarLeftDClick)

    # override function
    def CreatePopupMenu(self):
        menu = wx.Menu()
        item = menu.Append(wx.ID_ANY, u"打开")
        self.Bind(wx.EVT_MENU, self.__OnTaskBarLeftDClick, item)
        item = menu.Append(wx.ID_ANY, u"开始计时")
        self.Bind(wx.EVT_MENU, wx.GetApp().StartTask, item)
        item = menu.Append(wx.ID_ANY, u"停止计时")
        item.Enable(False)
        self.Bind(wx.EVT_MENU, wx.GetApp().StopTask, item)
        menu.AppendSeparator()
        item = menu.Append(wx.ID_ANY, u"退出")
        self.Bind(wx.EVT_MENU, self.__OnClose, item)
        return menu

    def OnStartTask(self, evt):
        self.ShowBalloon("", u"番茄钟开始计时")
        self.__menu.FindItemByPosition(1).Enable(False)
        self.__menu.FindItemByPosition(2).Enable(True)

    def OnStopTask(self, evt):
        self.ShowBalloon("", u"番茄钟停止")
        self.__menu.FindItemByPosition(1).Enable(True)
        self.__menu.FindItemByPosition(2).Enable(False)
        
    def __OnTaskBarRight(self, evt):
        self.PopupMenu(self.__menu)

    def __OnTaskBarLeftDClick(self, evt):
        if self.__frame.IsIconized():
            self.__frame.Iconize(False)
        if not self.__frame.IsShown():
            self.__frame.Show()
        else:
            self.__frame.Hide()
        self.__frame.Raise()

    def __OnClose(self, evt):
        self.__frame.Destroy()
        self.RemoveIcon()
        self.Destroy()
        
