from fixture.group import Group_helper
import clr
import os.path
project_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append(os.path.join(project_dir,"TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir,"Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName('TestStack.White')
from TestStack.White import Application
from TestStack.White.UIItems.Finders import *
clr.AddReferenceByName("UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35")
from System.Windows.Automation import *


class Opplication:

    def __init__(self,link):
        self.group = Group_helper(self)
        self.tw=Application.Launch(link)


    def open_main_window(self):
        return self.tw.GetWindow("Free Address Book")


    def destroy(self):
        main_w=self.open_main_window()
        main_w.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()