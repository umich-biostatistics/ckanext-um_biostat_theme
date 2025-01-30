# # encoding: utf-8

# '''plugin.py

# '''
# from ckan.common import CKANConfig
# import ckan.plugins as plugins
# import ckan.plugins.toolkit as toolkit


# class ExampleThemePlugin(plugins.SingletonPlugin):
#     '''An example theme plugin.

#     '''
#     # Declare that this class implements IConfigurer.
#     plugins.implements(plugins.IConfigurer)

#     def update_config(self, config: CKANConfig):

#         # Add this plugin's templates dir to CKAN's extra_template_paths, so
#         # that CKAN will use this plugin's custom templates.
#         # 'templates' is the path to the templates dir, relative to this
#         # plugin.py file.
#         toolkit.add_template_directory(config, 'templates')

#         # Add this plugin's public dir to CKAN's extra_public_paths, so
#         # that CKAN will use this plugin's custom static files.
#         toolkit.add_public_directory(config, 'public')

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class UmBiostatThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "um_biostat_theme")

    
