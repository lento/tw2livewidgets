<li class="item-${w.item_id}">
    % for c in w.children:
        ${c.display() | n}
    % endfor
</li>
