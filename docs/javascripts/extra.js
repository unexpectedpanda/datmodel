function filterList(element) {
    /**
    * Filter out list elements based on user input.
    *
    * You don't call this function directly. Instead, it's called automatically by an
    * event listener that's placed on input elements with the appropriate class.
    *
    * To create a filterable list in your HTML, an `input` element must be present with
    * the class `filter`. It must be followed by a `ul` with the class `filter`, which
    * contains the list items to filter. For example:
    *
    * <input type="text" class="filter" placeholder="Filter the list">
    * <ul class="filter">
    *   <li>List item</li>
    *   <li>List item</li>
    * </ul>
    *
    * @param {string} element - The `input` element used to filter the list content.
    */
    let inputElement, inputContent, listItemsToFilter, items, i, j, txtValue;

    inputElement = document.querySelector('#' + element.id);
    inputContent = inputElement.value.toLowerCase();

    listItemsToFilter = document.querySelectorAll('ul.filter');

    for (i = 0; i < listItemsToFilter.length; i++) {
        items = listItemsToFilter[i].querySelectorAll('li');

        for (j = 0; j < items.length; j++) {
            txtValue = items[j].innerText;

            if (txtValue.toLowerCase().indexOf(inputContent) > -1) {
                items[j].style.display = '';
            } else {
                items[j].style.display ='none';
            }
        }

    }
}

(function () {
    // Wait for the DOM content to load
    document.addEventListener('DOMContentLoaded', function(){
        // Turn autocomplete off for filter input elements, and set an event listener on
        // those inputs. The `input` event is used instead of `keyup` to properly capture
        // Input Method Editor (IME) content.
        let filterFields;

        filterFields = document.querySelectorAll('input.filter')

        for (i = 0; i < filterFields.length; i++) {
            filterFields[i].setAttribute('autocomplete', 'off');
            filterFields[i].addEventListener('input', function(){
                filterList(this);
            });
        }
    });
})();
