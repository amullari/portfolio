# Human Genome RNA Analysis: Structural Patterns and Genomic Distribution

## 📊 Project Overview
Human Genome RNA Analysis dashboard built with Power BI & Python. Featuring PostgreSQL data integration from RNAcentral, structural classification of 20+ RNA types, and genomic distribution mapping.

This data analysis project investigates the relationship between different RNA types, their physical lengths, and their spatial distribution within the human genome. By transforming complex genomic data into an interactive Power BI dashboard, the analysis reveals how biological classification dictates physical characteristics.

## 🧬 Data Source
The dataset is derived from **[RNAcentral](https://rnacentral.org/)**, the non-coding RNA sequence database. RNAcentral is a free, public resource that aggregates data from specialized ncRNA databases to provide a single entry point for accessing a wide range of non-coding RNA sequences.

## 💡 Key Analytical Insights
Based on the visualized data:
* **Structural Dominance:** **lncRNAs** act as "genomic architects," dominating long-sequence categories and making up **97.07%** of the long-class loci.
* **The Short Messenger Class:** **piRNAs** are the dominant type among short sequences, accounting for **70.53%** of the short-class loci.
* **Scale Variance:** There is a drastic difference in average length; **lncRNAs** average **10,852.2 bp**, while **piRNAs** average **45.2 bp**.
* **Spatial Organization:** Scatter plot analysis confirms that genomic location (start/stop positions) is highly ordered and strongly correlated with the specific length group of the RNA.

![Average Locus Size by RNA Type](image.png)

![Genomic Distribution Scatter Plot](image-1.png)

## 🛠️ Tech Stack & Methodology
* **Tools:** PostgreSQL, Python (Pandas, psycopg2), Power BI.
* **Agile Problem Solving:** When faced with initial connectivity hurdles between the database and Power BI, I implemented a **Python-based data bridge**. This ensured the project stayed on schedule and allowed for flexible data transformation before visualization.
* **Visualization Best Practices:** * Implemented **"Top N + Other"** grouping to improve readability by consolidating 20+ RNA types.
    * Used **logarithmic scaling ($log_{10}$)** to effectively visualize data spanning several orders of magnitude.
    * Applied a strategic color hierarchy to highlight key biological markers while neutralizing noise.

## 🤝 Credits & Acknowledgments
* **Project Concept:** This analysis was developed as part of a technical assessment task provided by Sergei Zubkov from Keskkonnateenused AS.
* **Subject Matter Expertise:** Special thanks to the biochemist specializing in RNA research who provided invaluable insights into the biological context and significance of the dataset.

## 📝 Conclusion
This project demonstrates the ability to deliver clear, actionable insights from complex datasets while maintaining technical flexibility to overcome infrastructure challenges.