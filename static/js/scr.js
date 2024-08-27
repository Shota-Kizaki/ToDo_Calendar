document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('myModal');
    const closeButton = document.querySelector('.close');

    document.querySelectorAll('.details-button').forEach(button => {
        button.addEventListener('click', function() {
            modal.style.display = 'block';
        });
    });

    closeButton.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});
