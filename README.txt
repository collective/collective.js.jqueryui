Introduction
============

Integration of jqueryui in Plone, like collective.js.jquery.

It is different from collective.jqueryui in many ways:

* no skin dirs (js and css are in resource dirs)
* no all the bunch of files and documentations from original jqueryui
* this one is minified
* just add all jqueryui to portal_js, and default css to portal_css (if you 
  apply the profile)

Notes
=====

There are three profiles in this package:

- ``default``: use this one with Plone 3.2/3.3 if you don't use
  plone.app.jquerytools. It will replace the jQuery version in Plone by
  the one included in collective.js.jquery because Plone <= 3.3rc2 include
  an old version of jQuery (1.2) and jqueryui 1.7 requires jQuery 1.3+.

- ``withjqtoolsplone3``: use this one if you include plone.app.jquerytools
  yourself in a Plone 3.2, this profile installs a jqueryui library
  without the tabs plugin which conflicts with plone.app.jquerytools.
  It will replace the jQuery version in Plone by the one included in
  collective.js.jquery.

- ``withjqtools``: use this one if you use Plone 3.3/4. It will keep the
  jQuery version included in Plone and is compatible with
  plone.app.jquerytools. You need to include plone.app.jquerytools yourself
  on Plone 3.3.
