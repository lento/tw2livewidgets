<%namespace name="utils" file="utils.mak"/>
function(data) {
    var action = $.sprintf("${w.action | n}", data);
    var title = $.sprintf('${w.label | n}', data);
    var css_class = $.sprintf('${w.css_class | n}', data);
    var field = '<a class="' + css_class + ' overlay" title="' + title + '" ';
    field += 'href="' + action + '" rel="#overlay">';
    ${utils.render_subfields(w.children) | n}
    field += '</a>';
    return field;
}

