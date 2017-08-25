from model.group import Group


class Group_helper:

     def __init__(self, app):
        self.app = app

     def open_group_editor(self,main_window):
         main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
         modal = main_window.ModalWindow("Group editor")
         return modal

     def get_group_list(self,main_window):
        modal= self.open_group_editor(main_window)
        tree= modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
        root=tree.Nodes[0]
        l=[node.Text for node in root.Nodes]
        self.close_group_editor(modal)
        return l


     def add_new_group(self,name,modal):
        modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
        modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter(name)
        Keyboard.Instance.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN)
        self.close_group_editor(modal)


     def close_group_editor(self,modal):
        modal.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()



