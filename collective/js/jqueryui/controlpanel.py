import logging
from zope import component
from zope import interface
from zope import schema
try:
    from zope.component.hooks import getSite
except ImportError:
    #BBB
    from zope.site.hooks import getSite

from plone.registry.interfaces import IRecordModifiedEvent

from plone.app.registry.browser import controlpanel as basepanel

from Products.Five import BrowserView

from collective.js.jqueryui.config import JQUERYUI_DEPENDENCIES
from collective.js.jqueryui.config import PATCH_RESOURCE_ID
from collective.js.jqueryui.config import CSS_RESOURCE_ID
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
RESOURCE_ID = '++resource++jquery-ui/jquery.%s.min.js'


logger = logging.getLogger('collective.js.jqueryui')

ui_core_desc = u"The core of jQuery UI, required for all interactions \
  and widgets."


class IJQueryUIPlugins(interface.Interface):

    ui_core = schema.Bool(title=u"Core",
                       description=ui_core_desc,
                       required=False, default=False)

    ui_widget = schema.Bool(title=u"Widget",
                         description=u"", required=False, default=False)

    ui_mouse = schema.Bool(title=u"Mouse",
                         description=u"", required=False, default=False)

    ui_position = schema.Bool(title=u"Position",
                         description=u"", required=False, default=False)

    ui_draggable = schema.Bool(title=u"Draggable",
                         description=u"", required=False, default=False)

    ui_droppable = schema.Bool(title=u"Droppable",
                         description=u"", required=False, default=False)

    ui_resizable = schema.Bool(title=u"Resizable",
                         description=u"", required=False, default=False)

    ui_selectable = schema.Bool(title=u"Selectable",
                         description=u"", required=False, default=False)

    ui_sortable = schema.Bool(title=u"Sortable",
                         description=u"", required=False, default=False)

    ui_accordion = schema.Bool(title=u"Accordion",
                         description=u"", required=False, default=False)

    ui_autocomplete = schema.Bool(title=u"Autocomplete",
                         description=u"", required=False, default=False)

    ui_button = schema.Bool(title=u"Button",
                         description=u"", required=False, default=False)

    ui_datepicker = schema.Bool(title=u"Date picker",
                         description=u"", required=False, default=False)

    ui_dialog = schema.Bool(title=u"Dialog",
                         description=u"", required=False, default=False)

    ui_menu = schema.Bool(title=u"Menu",
                         description=u"", required=False, default=False)

    ui_progressbar = schema.Bool(title=u"Progress bar",
                         description=u"", required=False, default=False)

    ui_slider = schema.Bool(title=u"Slider",
                         description=u"", required=False, default=False)

    ui_spinner = schema.Bool(title=u"Spinner",
                         description=u"", required=False, default=False)

    ui_tabs = schema.Bool(title=u"Tabs",
                         description=u"", required=False, default=False)

    ui_tooltip = schema.Bool(title=u"Tooltip",
                         description=u"", required=False, default=False)

    ui_effect = schema.Bool(title=u"Effects 'core'",
                         description=u"", required=False, default=False)

    ui_effect_blind = schema.Bool(title=u"Effects 'blind'",
                         description=u"", required=False, default=False)

    ui_effect_bounce = schema.Bool(title=u"Effects 'bounce'",
                         description=u"", required=False, default=False)

    ui_effect_clip = schema.Bool(title=u"Effects 'clip'",
                         description=u"", required=False, default=False)

    ui_effect_drop = schema.Bool(title=u"Effects 'drop'",
                         description=u"", required=False, default=False)

    ui_effect_explode = schema.Bool(title=u"Effects 'explode'",
                         description=u"", required=False, default=False)

    ui_effect_fade = schema.Bool(title=u"Effects 'fade'",
                         description=u"", required=False, default=False)

    ui_effect_fold = schema.Bool(title=u"Effects 'fold",
                         description=u"", required=False, default=False)

    ui_effect_highlight = schema.Bool(title=u"Effects 'highlight'",
                         description=u"", required=False, default=False)

    ui_effect_pulsate = schema.Bool(title=u"Effects 'pulsate'",
                         description=u"", required=False, default=False)

    ui_effect_scale = schema.Bool(title=u"Effects 'scale'",
                         description=u"", required=False, default=False)

    ui_effect_shake = schema.Bool(title=u"Effects 'shake'",
                         description=u"", required=False, default=False)

    ui_effect_slide = schema.Bool(title=u"Effects 'slide'",
                         description=u"", required=False, default=False)

    ui_effect_transfer = schema.Bool(title=u"Effects 'transfer'",
                         description=u"", required=False, default=False)


class ControlPanelForm(basepanel.RegistryEditForm):
    schema = IJQueryUIPlugins
    control_panel_view = "@@jqueryui-plugins-controlpanel"


class PluginsControlPanelView(basepanel.ControlPanelFormWrapper):
    form = ControlPanelForm

    index = ViewPageTemplateFile('controlpanel_layout.pt')

    label = u"JQueryUI plugins settings"

    def parent_panel_url(self):
        return '%s/@@jqueryui-controlpanel' % (self.context.absolute_url())

#
#@component.adapter(IJQueryUIPlugins, IRecordModifiedEvent)
#def update_dependencies(record, event):
#
#    key = event.record.fieldName
#    rkey = key.replace('_','.')
#    to_enable =set()
#    to_disable=set()
#
#    if event.oldValue and not event.newValue:
#        #means it has been deactivated
#        to_disable.add(RESOURCE_ID%rkey)
#        if rkey == 'ui.datepicker':
#            to_disable.add('++resource++jquery-ui-i18n.js')
#
#    elif not event.oldValue and event.newValue:
#        to_enable.add(RESOURCE_ID%rkey)
#        if rkey == 'ui.datepicker':
#            to_enable.add('++resource++jquery-ui-i18n.js')
#        deps = JQUERYUI_DEPENDENCIES[rkey]
#        for dep in deps:
#            to_enable.add(RESOURCE_ID%(dep))
#
#    update_registry(to_enable, to_disable)
#    verify_jsregistry(record)


def update_registry(to_enable=[], to_disable=[]):
    site = getSite()
    jsregistry = site.portal_javascripts

    for js in to_disable:
        resource = jsregistry.getResource(js)
        if resource:
            resource.setEnabled(False)

    for js in to_enable:
        resource = jsregistry.getResource(js)
        if resource:
            resource.setEnabled(True)

    jsregistry.cookResources()


def verify_jsregistry(record):
    """This function check the jsregistry configuration against the jsregistry
    """
    site = getSite()
    jsregistry = site.portal_javascripts

    keys = JQUERYUI_DEPENDENCIES.keys()
    for key in keys:
        rkey = key.replace('.', '_')
        resource_id = RESOURCE_ID % key
        setting = getattr(record, rkey, None)
        if setting is None:
            continue
        js = jsregistry.getResource(resource_id)
        #at install time resources are not load ...
        if not js:
            continue
        enabled = js.getEnabled()
        if enabled == setting:
            continue
        if not setting:
            #we don't want it explicitly but it can be a dependency
            continue
        #we have a not syncrhonized configuration
        msg = '%s issue. auto enable it' % resource_id
        logger.info(msg)
        js.setEnabled(True)
        if key == 'ui.datepicker':
            js = jsregistry.getResource('++resource++jquery-ui-i18n.js')
            js.setEnabled(True)


class IJQueryUICSS(interface.Interface):
    """JQueryUI CSS"""

    css = schema.Bool(title=u"Sunburst CSS for jqueryui",
                      description=u"Activate the JQueryUI theme 'Sunburst'",
                      default=False)

    patch = schema.Bool(title=u"Sunburst CSS Integration",
                        description=u"Activate the integration between \
                                JQueryUI 'Sunburst' theme and the Plone \
                                'Sunburst' theme",
                       default=False)


class SunburstControlPanelForm(basepanel.RegistryEditForm):
    schema = IJQueryUICSS
    control_panel_view = "@@jqueryui-sunburst-controlpanel"


class SunburstControlPanelView(basepanel.ControlPanelFormWrapper):
    form = SunburstControlPanelForm

    index = ViewPageTemplateFile('controlpanel_layout.pt')

    label = u"JQueryUI Sunburst CSS settings"

    def parent_panel_url(self):
        return '%s/@@jqueryui-controlpanel' % (self.context.absolute_url())


@component.adapter(IJQueryUICSS, IRecordModifiedEvent)
def cook_css_resources(record, event):
    site = getSite()
    cssregistry = site.portal_css

    key = event.record.fieldName
    stylesheet = None
    if key == 'css':
        stylesheet = cssregistry.getResource(CSS_RESOURCE_ID)
    elif key == 'patch':
        stylesheet = cssregistry.getResource(PATCH_RESOURCE_ID)
    status = event.newValue
    if stylesheet is not None:
        stylesheet.setEnabled(status)
        cssregistry.cookResources()


class MainControlPanelView(BrowserView):
    label = u"JQueryUI control panel"

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def actions(self):
        cstate = self.context.restrictedTraverse('plone_context_state')
        actions = cstate.actions('jqueryui_panels')
        return actions


@component.adapter(IJQueryUIPlugins, IRecordModifiedEvent)
def cook_js_resources(record, event):
    site = getSite()
    jsregistry = site.portal_javascripts
    jsregistry.cookResources()
