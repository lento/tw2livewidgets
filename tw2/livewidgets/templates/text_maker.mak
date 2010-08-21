function(data) {
    ## use widget value if "text" was not given, this is the mako + javascript
    ## counterpart to what is done in python in the widget's "prepare()"
    % if w.text:
        var text = $.sprintf('${w.text | n}', data);
    % else:
        var text = data['${w.id}'] ? data['${w.id}'] : '';
    % endif
    var css_class = $.sprintf('${w.css_class | n}', data);
    var title = $.sprintf('${w.help_text | n}', data);
    var field = '<div class="${w.widget_class} ' + css_class + '" title="' + title + '">' + text + '</div>';
    return field;
}
