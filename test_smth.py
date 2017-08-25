

def test(app):
    main_w=app.open_main_window()
    old_list=app.group.get_group_list(main_w)
    app.group.add_new_group("test group",main_w)
    new_list=app.group.get_group_list(main_w)
    old_list.append("test group")
    assert sorted(old_list)==sorted(new_list)






