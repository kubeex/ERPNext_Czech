app_name = "czech_localization"
app_title = "Czech Localization"
app_publisher = "Kuban"
app_description = "Czech language, terminology and localization layer for ERPNext and HRMS"
app_email = "kuban.sir@gmail.com"
app_license = "mit"

# Installed after erpnext and hrms so its translations/customizations
# act as the final, company-controlled layer.
required_apps = ["frappe", "erpnext", "hrms"]

# Fixtures / custom fields / workflows exported from this app go here as
# they are added, e.g.:
# fixtures = [
#     {"dt": "Custom Field", "filters": [["module", "=", "Czech Localization"]]},
#     {"dt": "Workflow", "filters": [["module", "=", "Czech Localization"]]},
# ]
