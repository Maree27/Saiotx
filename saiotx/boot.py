# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

def boot_session(bootinfo):
    emp_info = frappe.db.get_list('Employee',filters={'user_id':frappe.session.user},fields=['*'])

    if emp_info:
        bootinfo.profile = emp_info[0]