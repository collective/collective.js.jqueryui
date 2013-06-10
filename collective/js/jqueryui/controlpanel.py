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

from collective.js.jqueryui import jQueryUIMF as _
from collective.js.jqueryui.config import JQUERYUI_DEPENDENCIES
from collective.js.jqueryui.config import PATCH_RESOURCE_ID
from collective.js.jqueryui.config import CSS_RESOURCE_ID
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
RESOURCE_ID = '++resource++jquery-ui/jquery.%s.min.js'


logger = logging.getLogger('collective.js.jqueryui')

ui_core_desc = _(u"The core of jQuery UI, required for all interactions \
  and widgets.")

ui_widget_desc = _(u"Widgets are feature-rich, stateful plugins that have \
  a full life-cycle, along with methods and events.")

ui_mouse_desc = _(u"The mouse interaction is not intended to be used directly. \
  It is purely a base layer for other widgets to inherit from.")

ui_position_desc = _(u"Position an element relative to another.")

ui_draggable_desc = _(u"Allow elements to be moved using the mouse.")

ui_droppable_desc = _(u"Create targets for draggable elements.")

ui_resizable_desc = _(u"Change the size of an element using the mouse.")

ui_selectable_desc = _(u"Use the mouse to select elements, individually or in a group.")

ui_sortable_desc = _(u"Reorder elements in a list or grid using the mouse.")

ui_accordion_desc = _(u"Convert a pair of headers and content panels into an accordion.")

ui_autocomplete_desc = _(u"Autocomplete enables users to quickly find and select from  \
  a pre-populated list of values as they type, leveraging searching and filtering.")

ui_button_desc = _(u"Themeable buttons and button sets.")

ui_datepicker_desc = _(u"Select a date from a popup or inline calendar")

ui_dialog_desc = _(u"Open content in an interactive overlay.")

ui_menu_desc = _(u"Themeable menu with mouse and keyboard interactions for navigation.")

ui_progressbar_desc = _(u"Display status of a determinate or indeterminate process.")

ui_slider_desc = _(u"Drag a handle to select a numeric value.")

ui_spinner_desc = _(u"Enhance a text input for entering numeric values, with up/down \
  buttons and arrow key handling.")

ui_tabs_desc = _(u"A single content area with multiple panels, each associated with \
  a header in a list.")

ui_tooltip_desc = _(u"Customizable, themeable tooltips, replacing native tooltips.")

ui_effect_desc = _(u"Apply an animation effect to an element.")

ui_effect_blind_desc = _(u"The blind effect hides or shows an element by wrapping \
  the element in a container, and 'pulling the blinds'")

ui_effect_bounce_desc = _(u"The bounce effect bounces an element. When used with  \
  hide or show, the last or first bounce will also fade in/out.")

ui_effect_clip_desc = _(u"The clip effect will hide or show an element by clipping \
  the element vertically or horizontally.")

ui_effect_drop_desc = _(u"The drop effect hides or shows an element fading in/out \
  and sliding in a direction.")

ui_effect_explode_desc = _(u"The explode effect hides or shows an element by \
  splitting it into pieces.")

ui_effect_fade_desc = _(u"The fade effect hides or shows an element by fading it.")

ui_effect_fold_desc = _(u"The fold effect hides or shows an element by folding it.")

ui_effect_highlight_desc = _(u"The highlight effect hides or shows an element by \
  animating its background color first.")

ui_effect_pulsate_desc = _(u"The pulsate effect hides or shows an element by \
  pulsing it in or out.")

ui_effect_scale_desc = _(u"Shrink or grow an element by a percentage factor.")

ui_effect_shake_desc = _(u"Shakes the element multiple times, vertically or horizontally.")

ui_effect_slide_desc = _(u"Slides the element out of the viewport.")

ui_effect_transfer_desc = _(u"Transfers the outline of an element to another element.")


class IJQueryUIPlugins(interface.Interface):

    ui_core = schema.Bool(title=_(u"Core"),
                       description=ui_core_desc,
                       required=False, default=False)

    ui_widget = schema.Bool(title=_(u"Widget"),
                         description=ui_widget_desc, required=False, default=False)

    ui_mouse = schema.Bool(title=_(u"Mouse"),
                         description=ui_mouse_desc, required=False, default=False)

    ui_position = schema.Bool(title=_(u"Position"),
                         description=ui_position_desc, required=False, default=False)

    ui_draggable = schema.Bool(title=_(u"Draggable"),
                         description=ui_draggable_desc, required=False, default=False)

    ui_droppable = schema.Bool(title=_(u"Droppable"),
                         description=ui_droppable_desc, required=False, default=False)

    ui_resizable = schema.Bool(title=_(u"Resizable"),
                         description=ui_resizable_desc, required=False, default=False)

    ui_selectable = schema.Bool(title=_(u"Selectable"),
                         description=ui_selectable_desc, required=False, default=False)

    ui_sortable = schema.Bool(title=_(u"Sortable"),
                         description=ui_sortable_desc, required=False, default=False)

    ui_accordion = schema.Bool(title=_(u"Accordion"),
                         description=ui_accordion_desc, required=False, default=False)

    ui_autocomplete = schema.Bool(title=_(u"Autocomplete"),
                         description=ui_autocomplete_desc, required=False, default=False)

    ui_button = schema.Bool(title=_(u"Button"),
                         description=ui_button_desc, required=False, default=False)

    ui_datepicker = schema.Bool(title=_(u"Date picker"),
                         description=ui_datepicker_desc, required=False, default=False)

    ui_dialog = schema.Bool(title=_(u"Dialog"),
                         description=ui_dialog_desc, required=False, default=False)

    ui_menu = schema.Bool(title=_(u"Menu"),
                         description=ui_menu_desc, required=False, default=False)

    ui_progressbar = schema.Bool(title=_(u"Progress bar"),
                         description=ui_progressbar_desc, required=False, default=False)

    ui_slider = schema.Bool(title=_(u"Slider"),
                         description=ui_slider_desc, required=False, default=False)

    ui_spinner = schema.Bool(title=_(u"Spinner"),
                         description=ui_spinner_desc, required=False, default=False)

    ui_tabs = schema.Bool(title=_(u"Tabs"),
                         description=ui_tabs_desc, required=False, default=False)

    ui_tooltip = schema.Bool(title=_(u"Tooltip"),
                         description=ui_tooltip_desc, required=False, default=False)

    ui_effect = schema.Bool(title=_(u"Effects 'core'"),
                         description=ui_effect_desc, required=False, default=False)

    ui_effect_blind = schema.Bool(title=_(u"Effects 'blind'"),
                         description=ui_effect_blind_desc, required=False, default=False)

    ui_effect_bounce = schema.Bool(title=_(u"Effects 'bounce'"),
                         description=ui_effect_bounce_desc, required=False, default=False)

    ui_effect_clip = schema.Bool(title=_(u"Effects 'clip'"),
                         description=ui_effect_clip_desc, required=False, default=False)

    ui_effect_drop = schema.Bool(title=_(u"Effects 'drop'"),
                         description=ui_effect_drop_desc, required=False, default=False)

    ui_effect_explode = schema.Bool(title=_(u"Effects 'explode'"),
                         description=ui_effect_explode_desc, required=False, default=False)

    ui_effect_fade = schema.Bool(title=_(u"Effects 'fade'"),
                         description=ui_effect_fade_desc, required=False, default=False)

    ui_effect_fold = schema.Bool(title=_(u"Effects 'fold'"),
                         description=ui_effect_fold_desc, required=False, default=False)

    ui_effect_highlight = schema.Bool(title=_(u"Effects 'highlight'"),
                         description=ui_effect_highlight_desc, required=False, default=False)

    ui_effect_pulsate = schema.Bool(title=_(u"Effects 'pulsate'"),
                         description=ui_effect_pulsate_desc, required=False, default=False)

    ui_effect_scale = schema.Bool(title=_(u"Effects 'scale'"),
                         description=ui_effect_scale_desc, required=False, default=False)

    ui_effect_shake = schema.Bool(title=_(u"Effects 'shake'"),
                         description=ui_effect_shake_desc, required=False, default=False)

    ui_effect_slide = schema.Bool(title=_(u"Effects 'slide'"),
                         description=ui_effect_slide_desc, required=False, default=False)

    ui_effect_transfer = schema.Bool(title=_(u"Effects 'transfer'"),
                         description=ui_effect_transfer_desc, required=False, default=False)


class ControlPanelForm(basepanel.RegistryEditForm):
    schema = IJQueryUIPlugins
    control_panel_view = "@@jqueryui-plugins-controlpanel"


class PluginsControlPanelView(basepanel.ControlPanelFormWrapper):
    form = ControlPanelForm

    index = ViewPageTemplateFile('controlpanel_layout.pt')

    label = _(u"JQueryUI plugins settings")

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

    css = schema.Bool(title=_(u"Sunburst CSS for jqueryui"),
                      description=_(u"Activate the JQueryUI theme 'Sunburst'"),
                      default=False)

    patch = schema.Bool(title=_(u"Sunburst CSS Integration"),
                        description=_(u"Activate the integration between \
                                JQueryUI 'Sunburst' theme and the Plone \
                                'Sunburst' theme"),
                       default=False)


class SunburstControlPanelForm(basepanel.RegistryEditForm):
    schema = IJQueryUICSS
    control_panel_view = "@@jqueryui-sunburst-controlpanel"


class SunburstControlPanelView(basepanel.ControlPanelFormWrapper):
    form = SunburstControlPanelForm

    index = ViewPageTemplateFile('controlpanel_layout.pt')

    label = _(u"JQueryUI Sunburst CSS settings")

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
    label = _(u"JQueryUI control panel")

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
