# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="updSvetlana", middlename="updBorisovna", lastname="updKovaleva",
                       nickname="updBelaya",
                       title="updTester", company="updThe Best",
                       address="updLenina, 8", mobile="upd89001001213", home="upd555555", work="upd121212",
                       fax="upd111111", email="updstbelaya@gmail.com", email2="updstbelaya2@gmail.com",
                       email3="updstbelaya3@gmail.com", homepage="updgoogle.com", bday="1",
                       bmonth="January", byear="1999", aday="30", amonth="November",
                       ayear="2020", address2="updSokolovka, 22", phone2="upd89002222222",
                       notes="updзаметка")
    app.contact.edit_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_first_contact_firstname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="test"))
#     app.contact.edit_first(Contact(firstname="Anakin"))
