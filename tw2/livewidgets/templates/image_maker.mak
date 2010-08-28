function(data) {
    ## use widget value if "src" was not given, this is the mako + javascript
    ## counterpart to what is done in python in the widget's "prepare()"
    % if w.src:
        src = $.sprintf('${w.src | n}', data);
    % else:
        src = data['${w.id}'] ? data['${w.id}'] : '';
    % endif
    title = $.sprintf('${w.help_text | n}', data);
    var css_class = $.sprintf('${w.css_class | n}', data);
    var field = '<img src="' + src + '" class="${w.widget_class} ' + css_class + '"  title="' + title + '"></img>';
    return field;
}

