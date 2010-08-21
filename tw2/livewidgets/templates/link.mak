<div class="${w.widget_class} ${w.css_class % w.data}" title="${w.help_text % w.data}">
<a href="${w.dest % w.data}">
    % for c in w.children:
        ${c.display() | n }
    % endfor
</a>
</div>
