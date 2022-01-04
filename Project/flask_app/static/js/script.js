function sortTable(tableClass, n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    // table = document.getElementById("myTable2");
    table = document.getElementsByClassName(tableClass)[0];
    switching = true;
    // Set the sorting direction to ascending:
    dir = "asc";
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
        // Start by saying: no switching is done:
        switching = false;
        rows = table.rows;
        /* Loop through all table rows (except the
        first, which contains table headers): */
        for (i = 1; i < (rows.length - 1); i++) {
            // Start by saying there should be no switching:
            shouldSwitch = false;
            /* Get the two elements you want to compare,
            one from current row and one from the next: */
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];
            /* Check if the two rows should switch place,
            based on the direction, asc or desc: */
            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    // If so, mark as a switch and break the loop:
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    // If so, mark as a switch and break the loop:
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            /* If a switch has been marked, make the switch
            and mark that a switch has been done: */
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            // Each time a switch is done, increase this count by 1:
            switchcount++;
        } else {
            /* If no switching has been done AND the direction is "asc",
            set the direction to "desc" and run the while loop again. */
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}
// ============================================
// WORKING
// ============================================
const api = {
    key: "139e606a6bb07396691fcb466ee11417",
    base: "https://api.openweathermap.org/data/2.5/",
}
const searchbox = document.querySelector(".search-box");
searchbox.addEventListener("keypress", setQuery);

const searchbutton = document.querySelector(".search_button");
searchbutton.addEventListener("click", search_bar_value);

function setQuery(evt) {
    if (evt.keyCode == 13) {
        getResults(searchbox.value);
        // console.log(searchbox.value)
    }
}
function search_bar_value() {
    getResults(document.querySelector(".search-box").value);
}
function getResults(query) {
    fetch(`${api.base}weather?q=${query}&units=imperial&APPID=${api.key}`)
        .then(weather => {
            return weather.json();
        }).then(displayResults);
}
// function getUserResults() {
//     fetch(`${api.base}weather?lat={lat}&lon={lon}&units=imperial&APPID=${api.key}`)
//         .then(weather => {
//             return weather.json();
//         }).then(displayResults);
// }

// function dateBuilder(d) {
//     let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
//     let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

//     let day = days[d.getDay()];
//     let date = d.getDate();
//     let month = months[d.getMonth()];
//     let year = d.getFullYear();

//     return `${day} ${date} ${month} ${year}`
// }

function displayResults(weather) {
    console.log(weather);
    let city = document.querySelector(".location .city");
    city.innerText = `${weather.name}, ${weather.sys.country}`;

    // let now = new Date();
    // let date = document.querySelector('.location .date');
    // date.innerText = dateBuilder(now);
    let temp = document.querySelector('.temp');
    temp.innerHTML = `${Math.round(weather.main.temp)}°F`;

    let weather_el = document.querySelector('.weather');
    weather_el.innerText = weather.weather[0].main;

    let humidity = document.querySelector('.humidity');
    humidity.innerText = `Humidity: ${weather.main.humidity}%`;

    let wind = document.querySelector('.wind');
    wind.innerHTML = `Wind Speed: ${weather.wind.speed} miles/hour`;

    let hilow = document.querySelector('.hi-low');
    hilow.innerText = `${Math.round(weather.main.temp_min)}°F /  ${Math.round(weather.main.temp_max)}°F`;
}
// default weather data on load 
getResults("Atlanta");

//====================================
// AIRPORT INFO api
// ===================================
