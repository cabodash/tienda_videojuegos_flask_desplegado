let inputContainers = document.querySelectorAll('.input-box');
inputContainers.forEach(element => {
    let input = element.querySelector("input");

    isFilled(input, element);
    input.addEventListener('focusout', function () {
        isFilled(input, element);
    });

});

let textareaContainers = document.querySelectorAll('.textarea-box');
textareaContainers.forEach(element => {
    let textarea = element.querySelector("textarea");
    isFilled(textarea, element);
    textarea.addEventListener('focusout', function () {
        isFilled(textarea, element);
    });
});


function isFilled(field, element) {
    if (field.value.trim() === '') {
        element.classList.remove('is-filled');
    } else {
        element.classList.add('is-filled');
    }
}


