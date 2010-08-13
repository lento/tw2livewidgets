<%namespace name="utils" file="utils.mak"/>
function(data) {
    ## use widget value if "dest" was not given, this is the mako + javascript
    ## counterpart to what is done in python in the widget's "prepare()"
    % if w.dest:
        dest = $.sprintf("${w.dest | n}", data);
    % else:
        dest = data["${w.id}"] ? data["${w.id}"] : '';
    % endif
    var title = $.sprintf("${w.label | n}", data);
    var css_class = $.sprintf("${w.css_class | n}', data);
    var field = '<div class="' + field_class + '" title="' + title + '">';
    field += '<a href="' + dest + '">';
    ${utils.render_subfields(w.children) | n}
    field += '</a></div>';
    return field;
}
