document.addEventListener('DOMContentLoaded', function () {
    const dropdownToggles = document.querySelectorAll('.dropdown-item.dropdown-toggle');
  
    dropdownToggles.forEach(function (toggle) {
      toggle.addEventListener('click', function (e) {
        e.preventDefault();
  
        const submenu = toggle.nextElementSibling;
  
        if (submenu) {
          submenu.classList.toggle('show');
        }
      });
    });
  });
  