from django.template.loader import render_to_string

from plugins.archive_plugin import plugin_settings
from utils import models, setting_handler

def inject_edit_article(context):
    """
    Inject a form to be injected at the beginning of the submission process
    Prompts user to specify whether submission is new or update to existing article
    If update, asks whether major (substantive content updates) or minor (typos)
    """
    request = context.get('request')
    plugin = models.Plugin.objects.get(name=plugin_settings.SHORT_NAME)

    edit_article_enabled = setting_handler.get_plugin_setting(plugin, 'edit_article_enabled', request.journal)

    if not edit_article_enabled.value:
        return ''

    return render_to_string('archive_plugin/inject_edit_article.html', request=request)


def inject_article_archive(context):
    """
    Injects a link for the user to browse previous version of an article
    """ 
    request = context.get('request')
    plugin = models.Plugin.objects.get(name=plugin_settings.SHORT_NAME)

    article_archive_enabled = setting_handler.get_plugin_setting(plugin, 'article_archive_enabled', request.journal)

    if not article_archive_enabled.value:
        return ''

    return render_to_string('archive_plugin/inject_article_arhive.html', context={'article': context.get('article')}, request=request)


def inject_journal_archive(context):
    """
    Injects a link for the user to browse a list of previous archives of the encyclopedia
    """
    request = context.get('request')
    plugin = models.Plugin.objects.get(name=plugin_settings.SHORT_NAME)

    journal_archive_enabled = setting_handler.get_plugin_setting(plugin, 'article_archive_enabled', request.journal)

    if not journal_archive_enabled.value:
        return ''

    return render_to_string('archive_plugin/inject_journal_archive.html', request=request)