"""This extension's custom config settings.

This is the One Place where all this extension's config settings and their
default values should be defined.

We keep them in this config.py file so that they can be accessed by all this
extension's modules without any circular import problems.

If there are non-default settings for any of these variables in the config file
CKAN will pass them to the plugin object at CKAN startup and the plugin will
assign them to the variables in this module.
Other than that these variables shouldn't be assigned to - read-only!

"""
recheck_resources_after = 24
resend_pending_resources_after = 1
broken_resource_min_fails = 1
broken_resource_min_hours = 0
authorized_users = []
#This filter is not used rigth now, it is just added for a future use
organization_to_filter = ["cmems","plan4all","gdacs","esa-scihub", "ebas", "scent", "vito", "nasa-cmr"] # Orgs: "cmems","plan4all","gdacs","esa-scihub", "ebas", "scent", "vito" and "nasa-cmr"
