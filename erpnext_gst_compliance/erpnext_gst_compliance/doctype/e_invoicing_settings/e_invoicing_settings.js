frappe.ui.form.on('E Invoice Settings', {
	refresh(frm) {
		const docs_link = 'https://docs.erpnext.com/docs/v13/user/manual/en/regional/india/setup-e-invoicing';
		frm.dashboard.set_headline(
			__("Read {0} for more information on E Invoicing features.", [`<a href='${docs_link}'>documentation</a>`])
		);
	}
});