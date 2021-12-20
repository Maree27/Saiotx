# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "saiotx"
app_title = "Saiotx"
app_publisher = "ammarhararah"
app_description = "Saiotx Theme"
app_icon = "octicon octicon-briefcase-16"
app_color = "grey"
app_email = "ammarhararah@gmail.com"
app_license = "MIT"
app_logo_url = '/assets/saiotx/images/saiotx_logo_trans.png'


website_context = {
    "favicon": "/assets/saiotx/images/favicon.png",
    "splash_image": "/assets/saiotx/images/bg2.png"
}
homepage = "login"
home_page = "login"
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/saiotx/css/saiotx.css"
fixtures = ["Custom Script"]
# app_include_js = "/assets/saiotx/js/saiotx.js"

# include js, css files in header of web template
# web_include_css = "/assets/saiotx/css/saiotx.css"
# web_include_js = "/assets/saiotx/js/saiotx.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "saiotx.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "saiotx.install.before_install"
after_install = "saiotx.install.after_install"
extend_bootinfo = "saiotx.boot.boot_session"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "saiotx.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"saiotx.tasks.all"
# 	],
# 	"daily": [
# 		"saiotx.tasks.daily"
# 	],
# 	"hourly": [
# 		"saiotx.tasks.hourly"
# 	],
# 	"weekly": [
# 		"saiotx.tasks.weekly"
# 	]
# 	"monthly": [
# 		"saiotx.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "saiotx.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "saiotx.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "saiotx.task.get_dashboard_data"
# }

