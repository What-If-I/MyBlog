(function () {

    var deleteBtn = jQuery('#delete-post'),
        editBtn = jQuery('#edit-post');

    editBtn.click(function () {
        $.ajax({
            url: '/article/' + editBtn.data('article-id'),
            type: 'DELETE',
            headers: {'X-CSRFToken': editBtn.data('token')},
            success: function (result) {
                window.location.href = '/'
            },
            error: function (result) {
                alert(result)
            }
        });
    });


    deleteBtn.click(function () {
        $.ajax({
            url: '/article/' + deleteBtn.data('article-id'),
            type: 'DELETE',
            headers: {'X-CSRFToken': deleteBtn.data('token')},
            success: function (result) {
                window.location.href = '/'
            },
            error: function (result) {
                // todo: display message in a better way
                alert(result.status + ": " + result.result.statusText)
            }
        });
    });

})();