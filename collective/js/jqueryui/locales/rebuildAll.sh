#!/bin/bash
# ensure that when something is wrong, nothing is broken more than it should...
set -e

PRODUCTNAME='collective.js.jqueryui'
I18NDOMAIN=$PRODUCTNAME

i18ndude rebuild-pot --pot ${PRODUCTNAME}.pot --create ${I18NDOMAIN} ../
i18ndude sync --pot ${PRODUCTNAME}.pot ./*/LC_MESSAGES/${PRODUCTNAME}.po

i18ndude merge --pot ./plone.pot --merge ./plone-manual.pot
i18ndude sync --pot ./plone.pot ./*/LC_MESSAGES/plone.po

WARNINGS=`find . -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-WARN' | wc -l`
ERRORS=`find . -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-ERROR' | wc -l`
FATAL=`find . -name "*pt"  | xargs i18ndude find-untranslated | grep -e '^-FATAL' | wc -l`

echo
echo "There are $WARNINGS warnings \(possibly missing i18n markup\)"
echo "There are $ERRORS errors \(almost definitely missing i18n markup\)"
echo "There are $FATAL fatal errors \(template could not be parsed, eg. if it\'s not html\)"
echo "For more details, run \'find . -name \"\*pt\" \| xargs i18ndude find-untranslated\' or"
echo "Look the rebuild i18n log generate for this script called \'rebuild_i18n.log\' on locales dir"

rm ./rebuild_i18n.log

touch ./rebuild_i18n.log

find ../ -name "*pt" | xargs i18ndude find-untranslated > rebuild_i18n.log
