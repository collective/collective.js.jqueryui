VERSION = '1.9.1'

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

DEPS['ui.effects.core'] = tuple()
DEPS['ui.effects.blind'] = ('ui.effects.core',)
DEPS['ui.effects.bounce'] = ('ui.effects.core',)
DEPS['ui.effects.clip'] = ('ui.effects.core',)
DEPS['ui.effects.drop'] = ('ui.effects.core',)
DEPS['ui.effects.explode'] = ('ui.effects.core',)
DEPS['ui.effects.fade'] = ('ui.effects.core',)
DEPS['ui.effects.fold'] = ('ui.effects.core',)
DEPS['ui.effects.highlight'] = ('ui.effects.core',)
DEPS['ui.effects.pulsate'] = ('ui.effects.core',)
DEPS['ui.effects.scale'] = ('ui.effects.core',)
DEPS['ui.effects.shake'] = ('ui.effects.core',)
DEPS['ui.effects.slide'] = ('ui.effects.core',)
DEPS['ui.effects.transfer'] = ('ui.effects.core',)

JQUERYUI_DEPENDENCIES = DEPS

CSS_RESOURCE_ID = '++resource++jquery-ui-themes/sunburst/jqueryui.css'
PATCH_RESOURCE_ID = '++resource++jquery-ui-themes/sunburst-patch.css'

ORDERED_PLUGINS = ['ui.core', 'ui.widget', 'ui.mouse', 'ui.position',
                   'ui.draggable', 'ui.droppable', 'ui.resizable',
                   'ui.selectable', 'ui.sortable', 'ui.accordion',
                   'ui.autocomplete', 'ui.button',
                   'ui.datepicker', 'ui.dialog', 'ui.menu', 'ui.progressbar',
                   'ui.slider', 'ui.spinner', 'ui.tabs', 'ui.tooltip',
                   'ui.effects.core', 'ui.effects.blind',
                   'ui.effects.bounce', 'ui.effects.clip', 'ui.effects.drop',
                   'ui.effects.explode', 'ui.effects.fade', 'ui.effects.fold',
                   'ui.effects.highlight', 'ui.effects.pulsate', 'ui.effects.scale',
                   'ui.effects.shake', 'ui.effects.slide', 'ui.effects.transfer']
