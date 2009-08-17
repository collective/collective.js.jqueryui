Introduction
============

Simple integration of jqueryui in Plone, like collective.js.jquery.

It is different from collective.jqueryui in many ways:

* no skin dirs (js and css are in resource dirs)
* no all the bunch of files and documentations from original jqueryui
* this one is minified
* just add all jqueryui to portal_js, and default css to portal_css (if you apply the profile)

Notes
=====

Plone3.3 include the last JQuery (1.3.2). So please update your products to use the JQuery included in Plone, or you will include it twice.

