from plone.app.layout.viewlets.common import ViewletBase
from zope.i18n import translate

# this list was generated from jqueryui 1.8rc3
JQUERYUI_LANGUAGES = (
    'af', 'ar', 'az', 'bg', 'bs', 'ca', 'cs', 'da', 'de', 'el', 'en-GB', 'eo',
    'es', 'et', 'eu', 'fa', 'fi', 'fr-CH', 'fr', 'he', 'hr', 'hu', 'hy', 'id',
    'is', 'it', 'ja', 'ko', 'lt', 'lv', 'ms', 'nl', 'no', 'pl', 'pt-BR', 'ro',
    'ru', 'sk', 'sl', 'sq', 'sr', 'sr-SR', 'sv', 'th', 'tr', 'uk', 'vi',
    'zh-CN', 'zh-HK', 'zh-TW',
)

class L10nDatepicker(ViewletBase):

    def jq_language(self):
        language = self.request.LANGUAGE
        if '-' in language:
            # normalize combined language code
            parts = language.split('-')
            language = "%s-%s" % (parts[0], parts[1].upper())
            if language in JQUERYUI_LANGUAGES:
                return language
            else:
                # If the combined language doesn't exist in jqueryui
                # check only the first part.
                language = language.split('-')[0]
        if language in JQUERYUI_LANGUAGES:
            return language
        # Return empty string if the language is not supported
        # by jqueryui so the default this.regional[''] of the datepicker
        # plugin is used.
        return ''

    def update(self):
        date_format = translate(u"date_format_short_datepicker",
                                domain="plonelocales",
                                context=self.request)
        if date_format == u"date_format_short_datepicker":
            self.jq_date_format = 'mm/dd/yy'
        else:
            self.jq_date_format = date_format

    def render(self):
        return u"""<script type="text/javascript">
        jQuery(function($){
            $.datepicker.setDefaults(
                jQuery.extend($.datepicker.regional['%s'],
                {dateFormat: '%s'}));
        });
        </script>""" % (self.jq_language(), self.jq_date_format)
    

