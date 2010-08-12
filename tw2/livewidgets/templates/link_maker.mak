<%namespace name="utils" file="utils.mak"/>
function(data, id) {
    var title = $.sprintf('${w.parent.label | n}', data);
    var dest = $.sprintf('${w.parent.dest | n}', data);
    var css_class = $.sprintf('${w.parent.css_class | n}', data);
    var field = '<div class="' + field_class + '" title="' + title + '">';
    field += '<a href="' + dest + '">';
    ${utils.render_subfields(w.parent.children) | n}
    field += '</a></div>';
    return field;
}
