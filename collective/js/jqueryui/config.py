VERSION = '1.8.16'

DEPS = {}

DEPS['ui.core']     =tuple()
DEPS['ui.widget']   =tuple()
DEPS['ui.mouse']    =('ui.core',)
DEPS['ui.position'] =tuple()

DEPS['ui.draggable'] =('ui.core','ui.widget','ui.mouse')
DEPS['ui.droppable'] =('ui.draggable','ui.core','ui.widget','ui.mouse')
DEPS['ui.resizable'] =('ui.core','ui.widget','ui.mouse')
DEPS['ui.selectable']=('ui.core','ui.widget','ui.mouse')
DEPS['ui.sortable']  =('ui.core','ui.widget','ui.mouse')

DEPS['ui.accordion']   =('ui.core','ui.widget')
DEPS['ui.autocomplete']=('ui.core','ui.widget','ui.position')
DEPS['ui.button']      =('ui.core','ui.widget')
DEPS['ui.dialog']      =('ui.core','ui.widget','ui.position')
DEPS['ui.slider']      =('ui.core','ui.widget','ui.mouse')
DEPS['ui.tabs']        =('ui.core','ui.widget')
DEPS['ui.datepicker']  =('ui.core',)
DEPS['ui.progressbar'] =('ui.core','ui.widget')

DEPS['effects.core']     =tuple()
DEPS['effects.blind']    =('effects.core',)
DEPS['effects.bounce']   =('effects.core',)
DEPS['effects.clip']     =('effects.core',)
DEPS['effects.drop']     =('effects.core',)
DEPS['effects.explode']  =('effects.core',)
DEPS['effects.fade']     =('effects.core',)
DEPS['effects.fold']     =('effects.core',)
DEPS['effects.highlight']=('effects.core',)
DEPS['effects.pulsate']  =('effects.core',)
DEPS['effects.scale']    =('effects.core',)
DEPS['effects.shake']    =('effects.core',)
DEPS['effects.slide']    =('effects.core',)
DEPS['effects.transfer'] =('effects.core',)

JQUERYUI_DEPENDENCIES = DEPS

CSS_RESOURCE_ID='++resource++jquery-ui-themes/sunburst/jqueryui.css'
PATCH_RESOURCE_ID='++resource++jquery-ui-themes/sunburst-patch.css'

ORDERED_PLUGINS = ['ui.core','ui.widget','ui.mouse','ui.position',
                   'ui.draggable','ui.droppable','ui.resizable','ui.selectable',
                   'ui.sortable','ui.accordion','ui.autocomplete','ui.button',
                   'ui.dialog','ui.slider','ui.tabs','ui.datepicker',
                   'ui.progressbar','effects.core','effects.blind',
                   'effects.bounce','effects.clip','effects.drop',
                   'effects.explode','effects.fade','effects.fold',
                   'effects.highlight','effects.pulsate','effects.scale',
                   'effects.shake','effects.slide','effects.transfer']
