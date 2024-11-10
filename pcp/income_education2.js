async function fetchData() {
    try {
        const response = await fetch('customer_personality.csv'); 
        const dataText = await response.text();
        //Parsing CSV 
        const rows = dataText.trim().split('\n').slice(1); 
        const data = rows.map(row => {
            const columns = row.split(',');

            // Map income values to categorical ranges
            const incomeValue = parseFloat(columns[4]);
            let incomeCategory = "";
            if (incomeValue < 10000) incomeCategory = "0-10000";
            else if (incomeValue < 35000) incomeCategory = "10000-35000";
            else if (incomeValue < 50000) incomeCategory = "35000-50000";
            else if (incomeValue < 100000) incomeCategory = "50000-100000";
            else incomeCategory = "Above 100000";

            // Map mntWines values to 5 categorical ranges
            const mntWinesValue = parseFloat(columns[9]);
            let mntWinesCategory = "";
            if (mntWinesValue < 200) mntWinesCategory = "0-200";
            else if (mntWinesValue < 400) mntWinesCategory = "200-400";
            else if (mntWinesValue < 600) mntWinesCategory = "400-600";
            else if (mntWinesValue < 800) mntWinesCategory = "600-800";
            else mntWinesCategory = "800 and above";

            // Map mntFruits values to 5 categorical ranges
            const mntFruitsValue = parseFloat(columns[10]);
            let mntFruitsCategory = "";
            if (mntFruitsValue < 40) mntFruitsCategory = "0-40";
            else if (mntFruitsValue < 80) mntFruitsCategory = "40-80";
            else if (mntFruitsValue < 120) mntFruitsCategory = "80-120";
            else if (mntFruitsValue < 160) mntFruitsCategory = "120-160";
            else mntFruitsCategory = "160 and above";

            // Map mntMeatProducts values to 5 categorical ranges
            const mntMeatProductsValue = parseFloat(columns[11]);
            let mntMeatProductsCategory = "";
            if (mntMeatProductsValue < 400) mntMeatProductsCategory = "0-400";
            else if (mntMeatProductsValue < 800) mntMeatProductsCategory = "400-800";
            else if (mntMeatProductsValue < 1200) mntMeatProductsCategory = "800-1200";
            else if (mntMeatProductsValue < 1600) mntMeatProductsCategory = "1200-1600";
            else mntMeatProductsCategory = "1600 and above";

            // Map mntFishProducts values to 5 categorical ranges
            const mntFishProductsValue = parseFloat(columns[12]);
            let mntFishProductsCategory = "";
            if (mntFishProductsValue < 50) mntFishProductsCategory = "0-50";
            else if (mntFishProductsValue < 100) mntFishProductsCategory = "50-100";
            else if (mntFishProductsValue < 150) mntFishProductsCategory = "100-150";
            else if (mntFishProductsValue < 200) mntFishProductsCategory = "150-200";
            else mntFishProductsCategory = "200 and above";

            // Map mntSweetProducts values to 5 categorical ranges
            const mntSweetProductsValue = parseFloat(columns[13]);
            let mntSweetProductsCategory = "";
            if (mntSweetProductsValue < 50) mntSweetProductsCategory = "0-50";
            else if (mntSweetProductsValue < 100) mntSweetProductsCategory = "50-100";
            else if (mntSweetProductsValue < 150) mntSweetProductsCategory = "100-150";
            else if (mntSweetProductsValue < 200) mntSweetProductsCategory = "150-200";
            else mntSweetProductsCategory = "200 and above";

            // Map mntGoldProds values to 5 categorical ranges
            const mntGoldProdsValue = parseFloat(columns[14]);
            let mntGoldProdsCategory = "";
            if (mntGoldProdsValue < 50) mntGoldProdsCategory = "0-50";
            else if (mntGoldProdsValue < 100) mntGoldProdsCategory = "50-100";
            else if (mntGoldProdsValue < 150) mntGoldProdsCategory = "100-150";
            else if (mntGoldProdsValue < 200) mntGoldProdsCategory = "150-200";
            else mntGoldProdsCategory = "200 and above";

            return {
                income: incomeCategory,
                education: columns[2],
                mntWines: mntWinesCategory,
                mntFruits: mntFruitsCategory,
                mntMeatProducts: mntMeatProductsCategory,
                mntFishProducts: mntFishProductsCategory,
                mntSweetProducts: mntSweetProductsCategory,
                mntGoldProds: mntGoldProdsCategory
            };
        });

        // Grouping data by education level and taking samples from each level
        const educationLevels = ['Basic', 'Graduation', '2n Cycle', 'Master', 'PhD'];
        const sampleData = [];
        educationLevels.forEach(level => {
            const group = data.filter(d => d.education === level).slice(0, 20); 
            sampleData.push(...group);
        });

        createPlot(sampleData);
    } catch (error) {
        console.error("Error loading or processing data:", error);
    }
}


function createPlot(data) {
    const educationLevels = Array.from(new Set(data.map(d => d.education)));
    const educationColorMap = {};
    educationLevels.forEach((level, index) => {
        educationColorMap[level] = index / (educationLevels.length - 1);
    });

    const incomeGroups = ["0-10000", "10000-35000", "35000-50000", "50000-100000", "Above 100000"];
    const productCategories = {
        mntWines: ["0-200", "200-400", "400-600", "600-800", "800 and above"],
        mntFruits: ["0-40", "40-80", "80-120", "120-160", "160 and above"],
        mntMeatProducts: ["0-400", "400-800", "800-1200", "1200-1600", "1600 and above"],
        mntFishProducts: ["0-50", "50-100", "100-150", "150-200", "200 and above"],
        mntSweetProducts: ["0-50", "50-100", "100-150", "150-200", "200 and above"],
        mntGoldProds: ["0-50", "50-100", "100-150", "150-200", "200 and above"]
    };

    const trace = {
        type: "parcoords",
        line: {
            color: data.map(d => educationColorMap[d.education]),
            colorscale: 'Viridis'
        },
        dimensions: [
            {
                label: 'Education',
                tickvals: educationLevels.map((_, i) => i),
                ticktext: educationLevels,
                values: data.map(d => educationLevels.indexOf(d.education))
            },
            {
                label: 'Income',
                tickvals: incomeGroups.map((_, i) => i),
                ticktext: incomeGroups,
                values: data.map(d => incomeGroups.indexOf(d.income))
            },
            {
                label: 'Wine Spending',
                tickvals: productCategories.mntWines.map((_, i) => i),
                ticktext: productCategories.mntWines,
                values: data.map(d => productCategories.mntWines.indexOf(d.mntWines))
            },
            {
                label: 'Fruit Spending',
                tickvals: productCategories.mntFruits.map((_, i) => i),
                ticktext: productCategories.mntFruits,
                values: data.map(d => productCategories.mntFruits.indexOf(d.mntFruits))
            },
            {
                label: 'Meat Spending',
                tickvals: productCategories.mntMeatProducts.map((_, i) => i),
                ticktext: productCategories.mntMeatProducts,
                values: data.map(d => productCategories.mntMeatProducts.indexOf(d.mntMeatProducts))
            },
            {
                label: 'Fish Spending',
                tickvals: productCategories.mntFishProducts.map((_, i) => i),
                ticktext: productCategories.mntFishProducts,
                values: data.map(d => productCategories.mntFishProducts.indexOf(d.mntFishProducts))
            },
            {
                label: 'Sweet Spending',
                tickvals: productCategories.mntSweetProducts.map((_, i) => i),
                ticktext: productCategories.mntSweetProducts,
                values: data.map(d => productCategories.mntSweetProducts.indexOf(d.mntSweetProducts))
            },
            {
                label: 'Gold Spending',
                tickvals: productCategories.mntGoldProds.map((_, i) => i),
                ticktext: productCategories.mntGoldProds,
                values: data.map(d => productCategories.mntGoldProds.indexOf(d.mntGoldProds))
            }
        ]
    };

    const layout = {
        title: 'Customers Product preference based on Income,Spending and Education',
        width :900,
        height :600
    };

    Plotly.newPlot('plot', [trace], layout);
}

fetchData();


