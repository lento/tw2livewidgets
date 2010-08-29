<a class="${w.widget_class} ${w.dialog and 'dialog' or 'action'} ${w.css_class % w.data}"
   title="${w.help_text % w.data}"
   href="${w.action % w.data}">
    % for c in w.children:
        ${c.display() | n }
    % endfor
</a>
