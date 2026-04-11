// Basic form validation
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const required = form.querySelectorAll('[required]');
            let valid = true;
            required.forEach(field => {
                if (!field.value.trim()) {
                    valid = false;
                    field.style.borderColor = 'red';
                } else {
                    field.style.borderColor = '';
                }
            });
            if (!valid) {
                e.preventDefault();
                alert('Please fill all required fields');
            }
        });
    });

    // Client-side search (if needed)
    const searchForm = document.querySelector('#searchForm');
    if (searchForm) {
        searchForm.addEventListener('input', function(e) {
            // Can add live filter here if products shown
        });
    }
});
