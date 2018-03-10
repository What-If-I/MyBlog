(function () {

    var deleteBtn = jQuery('#delete-post');


    deleteBtn.click(function () {
        if (confirm("Are you sure you want to delete this post? You can't undo this action.")) {
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
        }
    });

})();