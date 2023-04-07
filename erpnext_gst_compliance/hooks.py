from . import __version__ as app_version

app_name = "erpnext_gst_compliance"
app_title = "ERPNext GST Compliance"
app_publisher = "Frappe Technologied Pvt. Ltd."
app_description = "Manage GST Compliance of ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@erpnext.com"
app_license = "GNU GPL v3.0"

before_tests = [
	"erpnext.setup.utils.before_tests",
	"erpnext_gst_compliance.erpnext_gst_compliance.setup.before_test"
]
after_install = "erpnext_gst_compliance.erpnext_gst_compliance.india.setup.setup"

doctype_js = {
	"Sales Invoice": [
					"public/js/sales_invoice.js",
					"erpnext_gst_compliance/erpnext_gst_compliance/india/e_invoice/einvoice.js",
                    "public/js/india.js",
					"public/js/india_js.js",
				]}


doctype_list_js = {
    "Sales Invoice": [
      "erpnext_gst_compliance/erpnext_gst_compliance/india/e_invoice/einvoice.js"
    ]
}


doc_events = {
	"Sales Invoice": {
		"on_update": "erpnext_gst_compliance.erpnext_gst_compliance.doctype.e_invoice.e_invoice.validate_sales_invoice_change",
		"on_submit": "erpnext_gst_compliance.erpnext_gst_compliance.doctype.e_invoice.e_invoice.validate_sales_invoice_submission",
		"on_cancel": [
			"erpnext_gst_compliance.erpnext_gst_compliance.doctype.e_invoice.e_invoice.validate_sales_invoice_cancellation",
			"erpnext_gst_compliance.erpnext_gst_compliance.doctype.e_invoice.e_invoice.cancel_e_invoice"
		],
		"on_trash": [
			"erpnext_gst_compliance.erpnext_gst_compliance.doctype.e_invoice.e_invoice.validate_sales_invoice_deletion",
			"erpnext_gst_compliance.erpnext_gst_compliance.doctype.e_invoice.e_invoice.delete_e_invoice"
		],
        "validate": [
			"erpnext_gst_compliance.erpnext_gst_compliance.india.utils.validate_document_name",
			"erpnext_gst_compliance.erpnext_gst_compliance.india.utils.update_taxable_values",
            "erpnext_gst_compliance.erpnext_gst_compliance.india.utils.validate_sez_and_export_invoices",
		]
	},
	"Company": {
		# "after_insert": "erpnext_gst_compliance.erpnext_gst_compliance.setup.on_company_update",
		# "on_update": "erpnext_gst_compliance.erpnext_gst_compliance.setup.on_company_update",
		"on_trash": "erpnext_gst_compliance.erpnext_gst_compliance.india.utils.delete_gst_settings_for_company"

	},
    "Tax Category": {
		"validate": "erpnext_gst_compliance.erpnext_gst_compliance.india.utils.validate_tax_category"
	},
    'Address': {
		'validate': ['erpnext_gst_compliance.erpnext_gst_compliance.india.utils.validate_gstin_for_india', 
               'erpnext_gst_compliance.erpnext_gst_compliance.india.utils.update_gst_category',]
	},
    'Supplier': {
		'validate': 'erpnext_gst_compliance.erpnext_gst_compliance.india.utils.validate_pan_for_india'
	},
    ('Sales Invoice', 'Sales Order', 'Delivery Note', 'Purchase Invoice', 'Purchase Order', 'Purchase Receipt'): {
		'validate': ['erpnext_gst_compliance.erpnext_gst_compliance.india.utils.set_place_of_supply']
	},
	"Purchase Invoice": {
		"validate": [
			"erpnext_gst_compliance.erpnext_gst_compliance.india.utils.update_grand_total_for_rcm",
            "erpnext_gst_compliance.erpnext_gst_compliance.india.utils.validate_reverse_charge_transaction",
			"erpnext_gst_compliance.erpnext_gst_compliance.india.utils.update_itc_availed_fields",
			"erpnext_gst_compliance.erpnext_gst_compliance.india.utils.update_taxable_values"

		
			]
	},
    "Payment Entry":{
                    "validate": "erpnext_gst_compliance.erpnext_gst_compliance.india.utils.update_place_of_supply",

	}
}


regional_overrides = {
    'india': {
    	'erpnext.tests.test_regional.test_method': 'erpnext_gst_compliance.erpnext_gst_compliance.india.utils.test_method',
    	'erpnext.controllers.taxes_and_totals.get_itemised_tax_breakup_header': 'erpnext_gst_compliance.erpnext_gst_compliance.india.utils.get_itemised_tax_breakup_header',
		'erpnext.controllers.taxes_and_totals.get_itemised_tax_breakup_data': 'erpnext_gst_compliance.erpnext_gst_compliance.india.utils.get_itemised_tax_breakup_data',
		'erpnext.accounts.party.get_regional_address_details': 'erpnext_gst_compliance.erpnext_gst_compliance.india.utils.get_regional_address_details',
		'erpnext.controllers.taxes_and_totals.get_regional_round_off_accounts': 'erpnext_gst_compliance.erpnext_gst_compliance.india.utils.get_regional_round_off_accounts',
		'erpnext.hr.utils.calculate_annual_eligible_hra_exemption': 'erpnext_gst_compliance.erpnext_gst_compliance.india.utils.calculate_annual_eligible_hra_exemption',
		'erpnext.hr.utils.calculate_hra_exemption_for_period': 'erpnext_gst_compliance.erpnext_gst_compliance.india.utils.calculate_hra_exemption_for_period',
		'erpnext.accounts.doctype.purchase_invoice.purchase_invoice.make_regional_gl_entries': 'erpnext_gst_compliance.erpnext_gst_compliance.india.utils.make_regional_gl_entries',
		'erpnext.controllers.accounts_controller.validate_einvoice_fields': 'erpnext_gst_compliance.erpnext_gst_compliance.india.e_invoice.utils.validate_einvoice_fields',
		'erpnext.assets.doctype.asset.asset.get_depreciation_amount': 'erpnext_gst_compliance.erpnext_gst_compliance.india.utils.get_depreciation_amount',
		'erpnext.stock.doctype.item.item.set_item_tax_from_hsn_code': 'erpnext_gst_compliance.erpnext_gst_compliance.india.utils.set_item_tax_from_hsn_code'

	}









}

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]
