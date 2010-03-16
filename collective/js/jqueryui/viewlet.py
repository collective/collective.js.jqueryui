from plone.app.layout.viewlets.common import ViewletBase
from zope.i18n import translate


class L10nDatepicker(ViewletBase):

    def language(self):
        language = self.request.LANGUAGE
        if '-' in language:
            # strip combined language code
            language = language.split('-')[0]
        return language

    def update(self):
        date_format = translate("date_format_short",
                                domain="plonelocales",
                                context=self.request)
        self.jq_date_format = date_format.replace(
            "${d}", "dd").replace(
            "${m}", "mm").replace(
            "${Y}", "yy")

    def render(self):
        print "rendering viewlet"
        return u"""<script type="text/javascript">
        jQuery(function($){
            $.datepicker.setDefaults(
                jQuery.extend($.datepicker.regional['%s'],
                {dateFormat: '%s'}));
        });
        </script>""" % (self.language(), self.jq_date_format)
    

