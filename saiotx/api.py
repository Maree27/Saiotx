# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def get_employee_info():
	employee_doc = frappe.db.get_list("Employee",filters={"user_id":frappe.session.user},fields=["name"])

	if employee_doc:
		checks = frappe.db.sql("""
			SELECT time,log_type,name 
			FROM `tabEmployee Checkin`
			WHERE employee = '{employee}'
				AND time like "{date}%"
		""".format(employee=employee_doc[0].get('name'),
					date=frappe.utils.today()),as_dict=1)

		if checks:
			return checks

	return None


def get_profit_loss_info():
	company = frappe.defaults.get_user_default("company")
	fiscal_year = frappe.defaults.get_user_default("fiscal_year")
	filters_dict_yearly = frappe._dict({
		'company': company,
		'from_fiscal_year': fiscal_year,
		'to_fiscal_year': fiscal_year,
		'periodicity': 'Yearly',
		'cost_center': [],
		'project': [],
		'include_default_book_entries': 1
		})
	filters_dict_monthly = filters_dict_yearly.copy()
	filters_dict_monthly.periodicity = 'Monthly'
	
	from erpnext.accounts.report.profit_and_loss_statement.profit_and_loss_statement import execute
	
	yearly_statement_result = execute(filters_dict_yearly)
	monthly_statement_result = execute(filters_dict_monthly)

	if yearly_statement_result and yearly_statement_result[1]:
		full_profit = yearly_statement_result[1]
	
	if monthly_statement_result and monthly_statement_result[1]:
		full_profit = monthly_statement_result[1]
	
		
@frappe.whitelist()
def get_total_purchase_info():
	if "System Manager" not in frappe.get_roles(frappe.session.user):
		return
	total_purchase_invoices = frappe.db.sql("""
		SELECT SUM(grand_total) as total
		FROM `tabPurchase Invoice`
	""",as_dict=1)
	if total_purchase_invoices:
		return total_purchase_invoices[0]
	
	return {}

@frappe.whitelist()
def get_total_purchase_order_info():
	if "System Manager" not in frappe.get_roles(frappe.session.user):
		return
		
	total_purchase_invoices = frappe.db.sql("""
		SELECT SUM(grand_total) as total
		FROM `tabPurchase Order`
	""",as_dict=1)
	if total_purchase_invoices:
		return total_purchase_invoices[0]
	
	return {}

@frappe.whitelist()
def get_total_sales_order_info():
	if "System Manager" not in frappe.get_roles(frappe.session.user):
		return

	total_sales_invoices = frappe.db.sql("""
		SELECT SUM(grand_total) as total
		FROM `tabSales Order`
	""",as_dict=1)

	if total_sales_invoices:
		return total_sales_invoices[0]
	
	return {}

@frappe.whitelist()
def get_total_sales_info():
	if "System Manager" not in frappe.get_roles(frappe.session.user):
		return

	total_sales_invoices = frappe.db.sql("""
		SELECT SUM(grand_total) as total
		FROM `tabSales Invoice`
	""",as_dict=1)

	if total_sales_invoices:
		return total_sales_invoices[0]
	
	return {}

@frappe.whitelist()
def get_daily_sales():
	if "System Manager" not in frappe.get_roles(frappe.session.user):
		return

	import datetime

	today = datetime.date.today()
	daily_sales = frappe.db.sql("""
		SELECT SUM(grand_total) as total, COUNT(name) as no_of_docs
		FROM `tabSales Invoice`
		WHERE posting_date = "{today}"
	""".format(today=today),as_dict=1)

	if daily_sales:
		return daily_sales[0]

	return {}


@frappe.whitelist()
def get_daily_purchases():
	if "System Manager" not in frappe.get_roles(frappe.session.user):
		return

	import datetime

	today = datetime.date.today()
	daily_purchases = frappe.db.sql("""
		SELECT SUM(grand_total) as total,count(name) as no_of_docs
		FROM `tabPurchase Invoice`
		WHERE posting_date = "{today}"
	""".format(today=today),as_dict=1)

	if daily_purchases:
		return daily_purchases[0]

	return {}

@frappe.whitelist()
def get_statistics_cards():
	if "System Manager" not in frappe.get_roles(frappe.session.user):
		return

	user = frappe.session.user
	lang = frappe.db.get_value("User", user,"language")
	from erpnext.accounts.utils import get_balance_on

	cards = frappe.db.get_all("Statistic Card",fields=["*"])
	result = []
	for card in cards:
		row = frappe._dict()
		row.title = card.title
		if lang == "ar":
			row.title = card.arabic_title
		row.icon = card.icon
		if card.choose_type == "DocType":
			row.total = frappe.db.count(card.document_type)
			result.append(row)
		elif card.choose_type == "Account":
			row.total = frappe.utils.fmt_money(get_balance_on(card.account))
			result.append(row)

	return result
