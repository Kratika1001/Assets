# Copyright (c) 2025, kratika and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CodeRequestForm(Document):
	pass

class CodeRequestForm(Document):
    def before_insert(self):
        # Set the 'created_by' field to the logged-in user if not already set
        if not self.created_by:
            self.created_by = frappe.session.user
   
