//Loading data
async function fetchData() {
    const response = await fetch('customer_personality.csv'); 
    const dataText = await response.text();

    // Parsing csv file
    const rows = dataText.trim().split('\n').slice(1); 
    const data = rows.map(row => {
        const columns = row.split(',');
        return {
            recency: parseFloat(columns[8]), // Recency
            numDealsPurchases: parseInt(columns[15]), // Deals purchases
            acceptedCmp1: parseInt(columns[20]), // Campaign 1
            acceptedCmp2: parseInt(columns[21]), // Campaign 2
            acceptedCmp3: parseInt(columns[22]), // Campaign 3
            acceptedCmp4: parseInt(columns[23]), // Campaign 4
            acceptedCmp5: parseInt(columns[24]), // Campaign 5
            totalAcceptedCmp: parseInt(columns[20]) + parseInt(columns[21]) + parseInt(columns[22]) + parseInt(columns[23]) + parseInt(columns[24]) // Sum of accepted campaigns
        };
    });

    const sampleData = data.slice(0, 40);

    createPlot(sampleData);
}

//plot
function createPlot(data) {
    const trace = {
        type: 'parcoords',
        line: {
            color: data.map(d => d.totalAcceptedCmp), // Color by total accepted campaigns
            colorscale: 'Viridis',
            showscale: true,
            colorbar: {
                title: 'Total Accepted Campaigns'
            }
        },
        dimensions: [
            {
                range: [0, Math.max(...data.map(d => d.recency))],
                label: 'Recency',
                values: data.map(d => d.recency),
                
            },
            {
                range: [0, Math.max(...data.map(d => d.numDealsPurchases))],
                label: 'Num_Deal_Pur',
                values: data.map(d => d.numDealsPurchases),
                
            },
            {
                range: [0, Math.max(...data.map(d => d.totalAcceptedCmp))],
                label: 'Total Accepted',
                values: data.map(d => d.totalAcceptedCmp),
                
            },
            {
                range: [0, 1],
                label: 'AcceptedCmp1',
                values: data.map(d => d.acceptedCmp1),
                
            },
            {
                range: [0, 1],
                label: 'AcceptedCmp2',
                values: data.map(d => d.acceptedCmp2),
                
            },
            {
                range: [0, 1],
                label: 'AcceptedCmp3',
                values: data.map(d => d.acceptedCmp3),
                
            },
            {
                range: [0, 1],
                label: 'AcceptedCmp4',
                values: data.map(d => d.acceptedCmp4),
                
            },
            {
                range: [0, 1],
                label: 'AcceptedCmp5',
                values: data.map(d => d.acceptedCmp5),
                
            }
        ]
    };

    const layout = {
        title: 'Customer Loyalty and Recency of Purchases',
        width: 900,
        height: 600
    };

    Plotly.newPlot('plot', [trace], layout);
}

fetchData();
