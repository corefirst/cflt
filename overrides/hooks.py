import os
import shutil

def on_post_build(config, **kwargs):
    site_dir = config['site_dir']
    sitemap_src = os.path.join(site_dir, 'sitemap.xml')
    sitemap_gz_src = os.path.join(site_dir, 'sitemap.xml.gz')
    
    if os.path.exists(sitemap_src):
        # Find i18n plugin to get configured languages
        i18n_plugin = config['plugins'].get('i18n')
        
        if i18n_plugin:
            i18n_config = i18n_plugin.config
            for lang_config in i18n_config['languages']:
                lang = lang_config['locale']
                # Skip the default language if it's at the root
                if lang_config.get('default', False) and i18n_config.get('docs_structure') == 'folder':
                    continue
                
                lang_dir = os.path.join(site_dir, lang)
                if os.path.isdir(lang_dir):
                    shutil.copyfile(sitemap_src, os.path.join(lang_dir, 'sitemap.xml'))
                    if os.path.exists(sitemap_gz_src):
                        shutil.copyfile(sitemap_gz_src, os.path.join(lang_dir, 'sitemap.xml.gz'))
                    print(f"INFO    -  Copied sitemap.xml to {lang_dir}")
