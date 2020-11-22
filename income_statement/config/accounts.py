from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
            "label": _("Profitability"),
			"items": [
				{
					"type": "report",
					"name": "Net Profit Report",
					"doctype": "GL Entry",
					"is_query_report": True
				},
				
            ]
		}
	] 