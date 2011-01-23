from zope import component
from plone.memoize.view import memoize
import logging
logger = logging.getLogger('collective.js.jqueryui')
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView

class IncludeJQueryUI(BrowserView):
    """Used to know if jqueryui resources must be included"""
    @memoize
    def __call__(self):
        pp = getToolByName(self.context, 'portal_properties').jqueryui_properties
        if pp.global_include:
            return True

        include_ids = pp.views_and_templates
        context_state = component.getMultiAdapter((self.context, self.request),
                                                  name='plone_context_state')
        if context_state.is_view_template():
            template_id = context_state.view_template_id()
            logger.info(template_id)
            return template_id in include_ids

        current_url = context_state.current_page_url()
        view_id = current_url.split('/')[-1].replace('@@','')
        logger.info(view_id)
        return view_id in include_ids
