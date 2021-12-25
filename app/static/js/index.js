// Apply the prefered theme [light, dark]
function set_theme(theme) {
    const logo_class = document.getElementById('theme-btn').classList;
    const set_root = (root, color) =>  document.documentElement.style.setProperty(root, color);

    if (theme == "dark") {
        set_root('--color-purple', 'rgb(99 102 241)');
        set_root('--color-light', 'rgb(30 41 59)');
        set_root('--color-dark', 'rgb(15 23 42)');
        set_root('--color-white', 'white');
        set_root('--color-cyan', '#17a2b8');
        set_root('--color-blue', '#1976d2');
        logo_class.remove("fa-moon");
        logo_class.add("fa-sun");
        localStorage.setItem("theme", "dark");
    } else {
        set_root('--color-purple', 'rgb(99 102 241)');
        set_root('--color-light', 'white');
        set_root('--color-white', 'rgb(15 23 42)');
        set_root('--color-dark', '#e3ebff');
        set_root('--color-cyan', '#17a2b8');
        set_root('--color-blue', '#1976d2');
        logo_class.remove("fa-sun");
        logo_class.add("fa-moon");
        localStorage.setItem("theme", "light");
    };
};

// Sets the sidenav visiblity [off when false]
function set_sidenav(value) {
    const app = document.getElementById("app");
    const sidenav = document.getElementById("sidenav");
    const footer =document.getElementById("footer");

    if(value == true) {
        sidenav.style.display  = 'flex';
        app.style.paddingLeft = '3.5rem';
        app.style.width = '80vw';
        footer.style.marginLeft = '3.5rem';
    } else {
        sidenav.style.display = 'none';
        app.style.paddingLeft = '0';
        app.style.width = '90vw';
        footer.style.marginLeft = '0';
    };
};

// Toggle theme on btn click 
function toggle_theme() {
    const theme = localStorage.getItem("theme");
    theme == "dark" ? set_theme("light") : set_theme("dark");
};

// Toggle sidenav on burger click
function toggle_burger() {
    const sidenav = document.getElementById("sidenav");
    if (sidenav.style.display == 'none') {
        set_sidenav(true);
    } else {
        set_sidenav(false);
    };
};

//STARTUP FUNCTION
function main() {
    //To Apply the user selected theme
    const theme = localStorage.getItem("theme");
    theme == "light" ? set_theme("light") : set_theme("dark");

    // Toggle sidenav when less screen size [off when < 600]
    ['resize', 'reload', 'load'].forEach(event =>
        window.addEventListener(event, () => {
            if (window.innerWidth < 600) {
                set_sidenav(false);
            } else {
                set_sidenav(true);
            };
        })
    );
};



main();
