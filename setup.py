from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpnext_gst_compliance/__init__.py
from erpnext_gst_compliance import __version__ as version

setup(
	name='erpnext_gst_compliance',
	version=version,
	description='Manage GST Compliance of ERPNext',
	author='Frappe Technologies Pvt. Ltd.',
	author_email='developers@frappe.io',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
