<%namespace name="utils" file="utils.mak"/>
function(data) {
    var dest = $.sprintf('${w.dest | n}', data);
    var title = $.sprintf('${w.help_text | n}', data);
    var css_class = $.sprintf('${w.css_class | n}', data);
    var field = '<div class="${w.widget_class} ' + css_class + '" title="' + title + '">';
    field += '<a href="' + dest + '">';
    ${utils.render_subfields(w.children) | n}
    field += '</a></div>';
    return field;
}
