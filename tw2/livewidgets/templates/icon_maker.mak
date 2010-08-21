function(data) {
    var icon_class = '${w.icon_class}';
    var title = $.sprintf('${w.help_text | n}', data);
    var css_class = $.sprintf('${w.css_class or '' | n}', data);
    var field = '<div class="${w.widget_class} ' + css_class + ' ' + icon_class +'" title="' + title + '"></div>';
    return field;
}

