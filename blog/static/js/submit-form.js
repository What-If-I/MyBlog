(function setup_submit_form() {

    const content = document.getElementById("id_content");
    const markdownEditor = new SimpleMDE({
        element: content,
        indentWithTabs: false,
        spellChecker: false
    });

    const form = document.getElementById("submit");
    form.addEventListener('click', function (ev) {
        content.value = markdownEditor.value();
    });

})();
