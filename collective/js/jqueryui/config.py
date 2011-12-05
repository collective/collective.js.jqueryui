VERSION = '1.8.16'

DEPS = {}

DEPS['core']     =tuple()
DEPS['widget']   =tuple()
DEPS['mouse']    =('core',)
DEPS['position'] =tuple()

DEPS['draggable'] =('core','widget','mouse')
DEPS['droppable'] =('draggable','core','widget','mouse')
DEPS['resizable'] =('core','widget','mouse')
DEPS['selectable']=('core','widget','mouse')
DEPS['sortable']  =('core','widget','mouse')

DEPS['accordion']   =('core','widget')
DEPS['autocomplete']=('core','widget','position')
DEPS['buttom']      =('core','widget')
DEPS['dialog']      =('core','widget','position')
DEPS['slider']      =('core','widget','mouse')
DEPS['tabs']        =('core','widget')
DEPS['datepicker']  =('core',)
DEPS['progressbar'] =('core','widget')

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
DEPS['effects.scale']=('effects.core',)
DEPS['effects.shake']=('effects.core',)
DEPS['effects.slide']=('effects.core',)
DEPS['effects.transfer']=('effects.core',)

JQUERYUI_DEPENDENCIES = DEPS
