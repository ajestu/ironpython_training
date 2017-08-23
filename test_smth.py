

def test(app):
   old_list=app.group.get_group_list(app.main_window)
   app.group.add_new_group(app.main_window,"test group")
   new_list=app.group.get_group_list(app.main_window)
   old_list.append("test group")
   assert sorted(old_list)==sorted(new_list)






