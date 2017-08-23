from model.group import Group


class Group_helper:

     def __init__(self, app):
        self.app = app



     def get_group_list(self):
        mw=self.app.opp
        modal= self.open_group_editor()
        tree= modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
        root=tree.Nodes[0]
        l=[node.Text for node in root.Nodes]
        self.close_group_editor(modal)
        return l


     def add_new_group(self,name):
        mw = self.app.opp
        modal = self.open_group_editor()
        modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
        modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter(name)
        Keyboard.Instance.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN)
        #  time.sleep(10)
        self.close_group_editor(modal)


     def close_group_editor(self,modal):
        mw = self.app.opp
        modal.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()


     def open_group_editor(self):
        mw = self.app.opp
        mw.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
        modal = mw.ModalWindow("Group editor")
        return modal
