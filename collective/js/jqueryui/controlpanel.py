import logging
from zope import component
from zope import interface
from zope import schema
from zope.component.hooks import getSite

from plone.registry.interfaces import IRecordModifiedEvent
from plone.z3cform import layout

from plone.app.registry.browser import controlpanel as basepanel

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from collective.js.jqueryui.config import JQUERYUI_DEPENDENCIES
from collective.js.jqueryui.config import PATCH_RESOURCE_ID
from collective.js.jqueryui.config import CSS_RESOURCE_ID


logger = logging.getLogger('collective.js.jqueryui')

class IJQueryUIPlugins(interface.Interface):
    
    ui_core = schema.Bool(title=u"Core",
                       description=u"The core of jQuery UI, required for all interactions and widgets.",
                       required=False,default=False)
    
    ui_widget = schema.Bool(title=u"Widget",
                         description=u"",required=False,default=False)

    ui_mouse = schema.Bool(title=u"Mouse",
                         description=u"",required=False,default=False)

    ui_position = schema.Bool(title=u"Position",
                         description=u"",required=False,default=False)

    ui_draggable = schema.Bool(title=u"Draggable",
                         description=u"",required=False,default=False)

    ui_droppable = schema.Bool(title=u"Droppable",
                         description=u"",required=False,default=False)

    ui_resizable = schema.Bool(title=u"Resizable",
                         description=u"",required=False,default=False)

    ui_selectable = schema.Bool(title=u"Selectable",
                         description=u"",required=False,default=False)

    ui_sortable = schema.Bool(title=u"Sortable",
                         description=u"",required=False,default=False)

    ui_accordion = schema.Bool(title=u"Accordion",
                         description=u"",required=False,default=False)

    ui_autocomplete = schema.Bool(title=u"Autocomplete",
                         description=u"",required=False,default=False)

    ui_button = schema.Bool(title=u"Button",
                         description=u"",required=False,default=False)

    ui_dialog = schema.Bool(title=u"Dialog",
                         description=u"",required=False,default=False)

    ui_slider = schema.Bool(title=u"Slider",
                         description=u"",required=False,default=False)

    ui_tabs = schema.Bool(title=u"Tabs",
                         description=u"",required=False,default=False)

    ui_datepicker = schema.Bool(title=u"Date picker",
                         description=u"",required=False,default=False)

    ui_progressbar = schema.Bool(title=u"Progress bar",
                         description=u"",required=False,default=False)

    effects_core = schema.Bool(title=u"Effects 'core'",
                         description=u"",required=False,default=False)

    effects_blind = schema.Bool(title=u"Effects 'blind'",
                         description=u"",required=False,default=False)

    effects_bounce = schema.Bool(title=u"Effects 'bounce'",
                         description=u"",required=False,default=False)

    effects_clip = schema.Bool(title=u"Effects 'clip'",
                         description=u"",required=False,default=False)

    effects_drop = schema.Bool(title=u"Effects 'drop'",
                         description=u"",required=False,default=False)

    effects_explode = schema.Bool(title=u"Effects 'explode'",
                         description=u"",required=False,default=False)

    effects_fade = schema.Bool(title=u"Effects 'fade'",
                         description=u"",required=False,default=False)

    effects_fold = schema.Bool(title=u"Effects 'fold",
                         description=u"",required=False,default=False)

    effects_highlight = schema.Bool(title=u"Effects 'highlight'",
                         description=u"",required=False,default=False)

    effects_pulsate = schema.Bool(title=u"Effects 'pulsate'",
                         description=u"",required=False,default=False)

    effects_scale = schema.Bool(title=u"Effects 'scale'",
                         description=u"",required=False,default=False)

    effects_shake = schema.Bool(title=u"Effects 'shake'",
                         description=u"",required=False,default=False)

    effects_slide = schema.Bool(title=u"Effects 'slide'",
                         description=u"",required=False,default=False)

    effects_transfer = schema.Bool(title=u"Effects 'transfer'",
                         description=u"",required=False,default=False)
    

class ControlPanelForm(basepanel.RegistryEditForm):
    schema = IJQueryUIPlugins

PluginsControlPanelView = layout.wrap_form(ControlPanelForm,
                                    basepanel.ControlPanelFormWrapper)
PluginsControlPanelView.label = u"JQueryUI plugins settings"

RESOURCE_ID='++resource++jquery-ui/jquery.%s.min.js'

@component.adapter(IJQueryUIPlugins, IRecordModifiedEvent)
def update_dependencies(record, event):

    key = event.record.fieldName
    rkey = key.replace('_','.')
    to_enable =set()
    to_disable=set()

    if event.oldValue and not event.newValue:
        #means it has been deactivated
        to_disable.add(RESOURCE_ID%rkey)
    elif not event.oldValue and event.newValue:
        to_enable.add(RESOURCE_ID%rkey)
        deps = JQUERYUI_DEPENDENCIES[rkey]
        for dep in deps:
            to_enable.add(RESOURCE_ID%(dep))

    logger.info("enable %s"%to_enable)
    logger.info("disable %s"%to_disable)
    update_registry(to_enable, to_disable)

def update_registry(to_enable=[], to_disable=[]):
    site=getSite()
    jsregistry = site.portal_javascripts
    
    for js in to_disable:
        resource = jsregistry.getResource(js)
        if resource:
            resource.setEnabled(False)
        else:
            logger.error('no resource %s'%js)

    for js in to_enable:
        resource = jsregistry.getResource(js)
        if resource:
            resource.setEnabled(True)
        else:
            logger.error('no resource %s'%js)

    jsregistry.cookResources()

class IJQueryUICSS(interface.Interface):
    """JQueryUI CSS"""
    
    css = schema.Bool(title=u"Sunburst CSS for jqueryui",
                      description=u"Activate the JQueryUI theme 'sunburst'",
                      default=False)
    
    patch = schema.Bool(title=u"Sunburst CSS Integration",
                        description=u"Activate the integration between JQueryUI\
                               'sunburst' theme and the Plone 'Sunburst' theme",
                       default=False)

class SunburstControlPanelForm(basepanel.RegistryEditForm):
    schema = IJQueryUICSS

SunburstControlPanelView = layout.wrap_form(SunburstControlPanelForm,
                                       basepanel.ControlPanelFormWrapper)

SunburstControlPanelView.label = u"JQueryUI Sunburst CSS settings"


@component.adapter(IJQueryUICSS, IRecordModifiedEvent)
def update_css(record, event):
    site = getSite()
    cssregistry = site.portal_css

    key = event.record.fieldName
    stylesheet = None
    if key=='css':
        stylesheet = cssregistry.getResource(CSS_RESOURCE_ID)
    elif key=='patch':
        stylesheet = cssregistry.getResource(PATCH_RESOURCE_ID)
    status = event.newValue
    if stylesheet is not None:
        stylesheet.setEnabled(status)
        cssregistry.cookResources()


class MainControlPanelView(BrowserView):
    label = u"JQueryUI control panel"
    description = u""

    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def actions(self):
        cstate = self.context.restrictedTraverse('plone_context_state')
        actions = cstate.actions('jqueryui_panels')
        return actions
    
        