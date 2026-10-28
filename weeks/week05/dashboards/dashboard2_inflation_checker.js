
// RICHARD DAVIES & JOSH HELLINGS

// AUTOMATED DATA VISUALISATION FOR POLICYMAKERS

// PURPOSE: JS CHART BUILDER THAT ALLOWS COUNTRY SELECTION AND RUNS FROM ECO-API TO BUILD CHARTS AND MAKES DIVS TO ACCOMODATE CHARTS.

// KEY FEATURES:
// - FUNCTION TO ADD COUNTRY INPUT BOXES
// - FUNCTION TO COLLECT COUNTRY CODES FROM INPUT BOXES, RETURNS ARRAY OF COUNTRY CODES
// - TEMPLATE VEGA-LITE CHART SPEC
// - FUNCTION TO LOOP THROUGH COUNTRY CODES AND BUILD CHARTS


// 1. FUNCTION TO ADD COUNTRY INPUT BOX

function addInputBox() {
    const countryInputContainer = document.getElementById('countryInputs');
    const inputBox = document.createElement('input');
    inputBox.type = 'text';
    inputBox.placeholder = 'iso3';
    inputBox.classList.add('countryInput');
    inputBox.maxLength = 3;     // Limit entry to 3 characters
    countryInputContainer.appendChild(inputBox);

}

// 2. FUNCTION TO COLLECT COUNTRY CODES FROM INPUT BOXES, RETURNS ARRAY OF COUNTRY CODES
function collectCountries() {
    // On click, get the country codes from the input boxes
    const countryInputs = document.querySelectorAll('.countryInput');
    const countryCodes = [];
    countryInputs.forEach(input => {
        // Check if the input is not empty
        if (input.value.trim() !== '') {
            countryCodes.push(input.value.trim().toLowerCase());
        }
    });
    return countryCodes;
}


// 3. DEFINE TEMPLATE SPEC
let baseSpec = {
    "$schema": "https://vega.github.io/schema/vega-lite/v6.json",
    "title": {
        "text": "", // This is injected via code, added from the csv that we load above.
        "subtitle": ["",""], // Added from csv
        "subtitleFontStyle":"italic",
        "subtitleFontSize":10,
        "anchor": "start",
        "color": "black"},
    "view": {"stroke": "transparent"}, // Make box around chart clear
    "data":{
        "url": "", // Added from loop
        "format":{
            "type": "json",
            "property": "data"}},

    "transform": [
        {"calculate":"year(datum.date)", "as": "year"},
        {"filter": "datum.year >= 2000"}
    ],
        
    "height": 200,
    "width": 200,
    "mark": {"type": "line", "color": "#58b3c7"},
    "encoding": {
        "x":{"field": "date", "type": "temporal", "title": null, "axis": {"grid": false,}},
        "y":{"field": "value", "type": "quantitative", "title": null, "axis": {"grid": false}}
    }
}


// 4. FUNCTION TO BUILD CHARTS (PASSES IN ARRAY OF COUNTRY CODES AND SELECTED SERIES)
async function buildCharts(selectCountries, selectedSeries) {
    // 1. Select our container div (where we will put the charts)
    const chartsContainer = document.getElementById('charts');
    // Clear previous charts to avoid duplicates/id collisions across runs
    chartsContainer.innerHTML = '';


    // 2. Loop across series
    for(let i=0; i<selectCountries.length; i++){
        // Make the URL:

        let urlUse = `https://api.economicsobservatory.com/${selectCountries[i]}/${selectedSeries}`;

        const spec = JSON.parse(JSON.stringify(baseSpec)); // Deep clone the base spec

        // Set the data URL:
        spec.data.url = urlUse;
        console.log(`Data URL: ${urlUse}`);

        // Set the title:
        spec.title.text = `${selectedSeries} - ${selectCountries[i]}`;

        // EXTRA CUSTOMISATION FOR INFLATION-ONLY EXAMPLE
        if (selectedSeries === 'infl') {
            spec.mark.type = 'bar';
            spec.encoding.y.axis.labelExpr = 'datum.label + "%"';
        }

        // Add the chart to the container:
        let chartDiv = document.createElement('div');
        chartDiv.id = "c"+i; // Give it a unique id
        chartDiv.classList.add('chart');
        chartsContainer.appendChild(chartDiv);
        await vegaEmbed(chartDiv, spec);

        console.log(spec);
    }
}


// 5. FUNCTION TO RUN THE WHOLE THING (WHEN USER CLICKS RUN BUTTON)
function run() {

    // 1. Get the selected series from the dropdown
    let selectedSeries = '';
    // try and get the selected series from the dropdown (doesn't exist in inflation-only example)
    try {
        selectedSeries = document.getElementById('seriesSelect').value;
    } catch (error) {
        selectedSeries = 'infl'; // Default to inflation if no series is selected (i.e. inflation-only example)
    }
    console.log(`Selected series: ${selectedSeries}`);

    // 2. Collect list of inputted country codes
    const selectCountries = collectCountries();
    console.log(`Selected country codes: ${selectCountries}`);

    // 3. Build the charts
    buildCharts(selectCountries, selectedSeries);
}