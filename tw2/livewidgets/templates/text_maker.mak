function(data) {
    ## use widget value if "text" was not given, this is the mako + javascript
    ## counterpart to what is done in python in the widget's "prepare()"
    % if w.text:
        text = $.sprintf("${w.text | n}", data);
    % else:
        text = data["${w.id}"] ? data["${w.id}"] : '';
    % endif
    var css_class = $.sprintf("${w.css_class | n}", data);
    var title = $.sprintf("${w.label | n}", data);
    field = '<div class="' + css_class + '" title="' + title + '">' + text + '</div>';
    return field;
}
