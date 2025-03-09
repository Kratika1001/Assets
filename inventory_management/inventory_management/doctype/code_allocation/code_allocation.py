# Copyright (c) 2025, kratika and contributors
# For license information, please see license.txt

#import frappe
from frappe.model.document import Document
from datetime import datetime


class CodeAllocation(Document):
	pass


class CodeAllocation(Document):
    def before_insert(self):
        # Automatically set the created_on field to today's date
        if not self.created_on:
            self.created_on = datetime.today().strftime('%Y-%m-%d')  # Format the date as 'YYYY-MM-DD'
