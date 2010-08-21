<a class="${w.widget_class} ${w.overlay and 'overlay' or ''} ${w.css_class % w.data}"
   title="${w.help_text % w.data}"
   href="${w.action % w.data}"
   ${w.overlay and 'rel="#overlay"' or ''}>
    % for c in w.children:
        ${c.display() | n }
    % endfor
</a>
