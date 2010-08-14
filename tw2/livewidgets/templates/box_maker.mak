<%namespace name="utils" file="utils.mak"/>
function(data) {
    var title = $.sprintf('${w.label | n}', data);
    var css_class = $.sprintf('${w.css_class | n}', data);
    var field = '<div class="' + css_class + '" title="' + title + '">';
    ${utils.render_subitems(w.children) | n}
    field += '</div>';
    return field;
}

