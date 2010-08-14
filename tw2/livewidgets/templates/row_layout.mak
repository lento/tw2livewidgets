<tr id="${w.item_id}">
    % for c in w.children:
        <td>
            ${c.display() | n}
        </td>
    % endfor
</tr>
