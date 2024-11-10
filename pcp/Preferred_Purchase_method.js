async function fetchData() {
    const response = await fetch('customer_personality.csv'); 
    const dataText = await response.text();

    // Parsing csv
    const rows = dataText.trim().split('\n').slice(1); 
    const data = rows.map(row => {
        const columns = row.split(',');

        // Categorize Income 
        const incomeValue = parseFloat(columns[4]);
        let incomeCategory = "";
        if (incomeValue < 10000) incomeCategory = "0-10000";
        else if (incomeValue < 35000) incomeCategory = "10000-35000";
        else if (incomeValue < 50000) incomeCategory = "35000-50000";
        else if (incomeValue < 100000) incomeCategory = "50000-100000";
        else incomeCategory = "Above 100000";

        return {
            year_birth: parseInt(columns[1]), // Year of birth 
            marital_status: columns[3], // Marital status
            kidhome: parseInt(columns[5]), // Number of kids at home
            teenhome: parseInt(columns[6]), // Number of teenagers at home
            incomeCategory: incomeCategory, // Categorical income
            numStorePurchases: parseInt(columns[18]), // Number of store purchases
            numWebPurchases: parseInt(columns[17]), // Number of web purchases
            numCatalogPurchases: parseInt(columns[19]) // Number of catalog purchases
        };
    });
    const sampleData = data.slice(0, 50);
    createPlot(sampleData);
}

function createPlot(data) {
    const maritalStatusColors = {
        "Single": "#F0F921",    // Light Yellow
        "Married": "#9EED47",   // Light Green
        "Together": "#32B26B",  // Soft Teal
        "Divorced": "#2D7F5F",  // Soft Sea Green
        "Widow": "#4D4E98"      // Light Blue
    };

    const trace = {
        type: 'parcoords',
        line: {
            color: data.map(d => {
                switch (d.marital_status) {
                    case 'Single': return 0;
                    case 'Married': return 0.25;
                    case 'Together': return 0.5;
                    case 'Divorced': return 0.75;
                    case 'Widow': return 1;
                    default: return 0;
                }
            }),
            colorscale: [
                [0, maritalStatusColors["Single"]],
                [0.25, maritalStatusColors["Married"]],
                [0.5, maritalStatusColors["Together"]],
                [0.75, maritalStatusColors["Divorced"]],
                [1, maritalStatusColors["Widow"]]
            ],
            showscale: true,
            colorbar: {
                title: 'Marital Status',
                tickvals: [0, 0.25, 0.5, 0.75, 1],
                ticktext: ['Single', 'Married', 'Together', 'Divorced', 'Widow'],
                lenmode: "fraction",
                len: 1.0
            }
        },
        dimensions: [
            {
                range: [1930, 2020],
                label: 'Year of Birth',
                values: data.map(d => d.year_birth),
                tickvals: [1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
            },
            {
                label: 'Marital Status',
                values: data.map(d => {
                    switch (d.marital_status) {
                        case 'Single': return 1;
                        case 'Married': return 2;
                        case 'Together': return 3;
                        case 'Divorced': return 4;
                        case 'Widow': return 5;
                        default: return 0;
                    }
                }),
                tickvals: [1, 2, 3, 4, 5],
                ticktext: ['Single', 'Married', 'Together', 'Divorced', 'Widow']
            },
            {
                range: [0, Math.max(...data.map(d => d.kidhome))],
                label: 'Kids at Home',
                values: data.map(d => d.kidhome),
                tickvals: [0, 1, 2]
            },
            {
                range: [0, Math.max(...data.map(d => d.teenhome))],
                label: 'Teens at Home',
                values: data.map(d => d.teenhome),
                tickvals: [0, 1, 2]
            },
            {
                label: 'Income Category',
                values: data.map(d => {
                    switch (d.incomeCategory) {
                        case '0-10000': return 1;
                        case '10000-35000': return 2;
                        case '35000-50000': return 3;
                        case '50000-100000': return 4;
                        case 'Above 100000': return 5;
                        default: return 0;
                    }
                }),
                tickvals: [1, 2, 3, 4, 5],
                ticktext: ['0-10000', '10000-35000', '35000-50000', '50000-100000', 'Above 100000']
            },
            {
                range: [0, Math.max(...data.map(d => d.numStorePurchases))],
                label: 'Store Purchases',
                values: data.map(d => d.numStorePurchases)
            },
            {
                range: [0, Math.max(...data.map(d => d.numWebPurchases))],
                label: 'Web Purchases',
                values: data.map(d => d.numWebPurchases)
            },
            {
                range: [0, Math.max(...data.map(d => d.numCatalogPurchases))],
                label: 'Catalog Purchases',
                values: data.map(d => d.numCatalogPurchases)
            }
        ]
    };

    const layout = {
        title: 'Customer Demographics and Purchase Channels',
        width: 900,
        height: 600
    };

    Plotly.newPlot('plot', [trace], layout);
}

fetchData();
