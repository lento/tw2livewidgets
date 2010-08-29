<%namespace name="utils" file="utils.mak"/>
function(data) {
    var action = $.sprintf('${w.action | n}', data);
    var title = $.sprintf('${w.help_text | n}', data);
    var css_class = $.sprintf('${w.css_class | n}', data);
    var field = '<a class="${w.widget_class} ${w.dialog and 'dialog' or 'action'} ' + css_class + '" title="' + title + '" href="' + action + '">';
    ${utils.render_subfields(w.children) | n}
    field += '</a>';
    return field;
}

