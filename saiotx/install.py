# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version


def after_install():
    import frappe
    welcome_page_exists =frappe.db.exists("Page","welcome-to-erpnext")

    if welcome_page_exists:
        frappe.db.delete("Page","welcome-to-erpnext")

    
    frappe.db.commit()