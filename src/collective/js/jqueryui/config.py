VERSION = '1.10.4'

DEPS = {}

DEPS['ui.core'] = tuple()
DEPS['ui.widget'] = tuple()
DEPS['ui.mouse'] = ('ui.core',)
DEPS['ui.position'] = tuple()

DEPS['ui.draggable'] = ('ui.core', 'ui.widget', 'ui.mouse')
DEPS['ui.droppable'] = ('ui.draggable', 'ui.core', 'ui.widget', 'ui.mouse')
DEPS['ui.resizable'] = ('ui.core', 'ui.widget', 'ui.mouse')
DEPS['ui.selectable'] = ('ui.core', 'ui.widget', 'ui.mouse')
DEPS['ui.sortable'] = ('ui.core', 'ui.widget', 'ui.mouse')

DEPS['ui.accordion'] = ('ui.core', 'ui.widget')
DEPS['ui.autocomplete'] = ('ui.core', 'ui.widget', 'ui.position', 'ui.menu')
DEPS['ui.button'] = ('ui.core', 'ui.widget')
DEPS['ui.datepicker'] = ('ui.core',)
DEPS['ui.dialog'] = ('ui.core', 'ui.widget', 'ui.position')
DEPS['ui.menu'] = ('ui.core', 'ui.widget', 'ui.position')
DEPS['ui.progressbar'] = ('ui.core', 'ui.widget')
DEPS['ui.slider'] = ('ui.core', 'ui.widget', 'ui.mouse')
DEPS['ui.spinner'] = ('ui.core', 'ui.widget', 'ui.button')
DEPS['ui.tabs'] = ('ui.core', 'ui.widget')
DEPS['ui.tooltip'] = ('ui.core', 'ui.widget', 'ui.position')

DEPS['ui.effect'] = tuple()
DEPS['ui.effect-blind'] = ('ui.effect',)
DEPS['ui.effect-bounce'] = ('ui.effect',)
DEPS['ui.effect-clip'] = ('ui.effect',)
DEPS['ui.effect-drop'] = ('ui.effect',)
DEPS['ui.effect-explode'] = ('ui.effect',)
DEPS['ui.effect-fade'] = ('ui.effect',)
DEPS['ui.effect-fold'] = ('ui.effect',)
DEPS['ui.effect-highlight'] = ('ui.effect',)
DEPS['ui.effect-pulsate'] = ('ui.effect',)
DEPS['ui.effect-scale'] = ('ui.effect',)
DEPS['ui.effect-shake'] = ('ui.effect',)
DEPS['ui.effect-slide'] = ('ui.effect',)
DEPS['ui.effect-transfer'] = ('ui.effect',)

JQUERYUI_DEPENDENCIES = DEPS

CSS_RESOURCE_ID = '++resource++jquery-ui-themes/sunburst/jqueryui.css'
PATCH_RESOURCE_ID = '++resource++jquery-ui-themes/sunburst-patch.css'

ORDERED_PLUGINS = ['ui.core', 'ui.widget', 'ui.mouse', 'ui.position',
                   'ui.draggable', 'ui.droppable', 'ui.resizable',
                   'ui.selectable', 'ui.sortable', 'ui.accordion',
                   'ui.autocomplete', 'ui.button',
                   'ui.datepicker', 'ui.dialog', 'ui.menu', 'ui.progressbar',
                   'ui.slider', 'ui.spinner', 'ui.tabs', 'ui.tooltip',
                   'ui.effect', 'ui.effect-blind',
                   'ui.effect-bounce', 'ui.effect-clip', 'ui.effect-drop',
                   'ui.effect-explode', 'ui.effect-fade', 'ui.effect-fold',
                   'ui.effect-highlight', 'ui.effect-pulsate',
                   'ui.effect-scale', 'ui.effect-shake', 'ui.effect-slide',
                   'ui.effect-transfer']
