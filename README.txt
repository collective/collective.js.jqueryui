Introduction
============

Integration of jqueryui in Plone 4.
Use 1.7 versions if you want to use this package on Plone < 4.

This version includes jqueryui 1.8rc3 without the tabs plugin. The Smoothless
theme is used.

It is different from collective.jqueryui in many ways:

* no skin dirs (js and css are in resource dirs)
* no all the bunch of files and documentations from original jqueryui
* this one is minified
* just add all jqueryui to portal_js, and default css to portal_css (if you 
  apply the profile)

Notes
=====

The package contains now only one profile. It doesn't replace
the jQuery version like the previous versions did.

Upgrade notes
=============

If you used the ``withjqtools`` or ``withjqtoolsplone3`` profile in older
version, please use now the ``default`` profile.
