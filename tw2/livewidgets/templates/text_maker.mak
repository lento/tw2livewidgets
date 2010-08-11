function(data, id) {
    var css_class = $.sprintf('${w.parent.css_class or '' | n}', data);
    var title = $.sprintf('${w.parent.label or '' | n}', data);
    % if w.parent.text:
        var text = $.sprintf('${w.parent.text | n}', data);
    % else:
        var text = data[id] ? data[id] : '';
    % endif
    field = '<div class="' + css_class + '" title="' + title + '">' + text + '</div>';
    return field;
}
