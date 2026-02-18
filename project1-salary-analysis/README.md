# Salary Management Tool (_Palgakorraldus_)

The objective of this project is to create a **user-friendly analytical tool for HR professionals**.  
All data used in this project is synthetic and generated for demonstration purposes.

## 📘 Project Overview

This project demonstrates how data analysis can support **pay transparency** and **equitable compensation** within an organization.

The Power BI report focuses on:
- gender pay gaps,
- workforce composition,
- and structural factors influencing salary differences.

It enables users to explore salaries by **category, level, and gender**, and to identify key drivers behind observed pay disparities.

## 📸 Key Visualizations

Selected views illustrating the main analytical perspectives:

### Salary Ranges

Visual overview of salary dispersion across job categories and levels. Wide ranges and outliers highlight potential inconsistencies in role grading and compensation practices. Used to quickly identify areas requiring deeper investigation.

![Salary Ranges](/project1-salary-analysis/images/salary-ranges.png)

### Salary Range Cross Table

Compact tabular view of salary ranges by category and level. Provides precise numerical comparison where visual overview is not sufficient.

![Salary Range Cross Table](/project1-salary-analysis/images/cross-table.png)

### Gender Pay Gap by Category

Bar chart showing gender pay gap across job families and levels. Categories are sorted by decreasing pay gap to highlight the most critical areas. 

Pay gaps above 5% are flagged as potential risk indicators. Supporting lines show average male and female salaries for context.

![Gender Pay Gap By Category](/project1-salary-analysis/images/salary-gap.png)

### Male vs Female Salaries by Position

Scatter plot comparing average male and female salaries per job position. Point size reflects the number of employees. Positions above the diagonal indicate higher male salaries, positions below indicate higher female salaries. Used to detect structural imbalance at role level.

The Scatter Plot is connected to an interactive table showing employee-level salary details. Clicking any chart filters the table accordingly. Supports root-cause analysis behind observed pay gaps and anomalies.

   ![Male vs Female Salaries by Position](/project1-salary-analysis/images/scatter-plot.png)

## 📊 Power BI Files and documentation

- _Palgauuring.pbx_ – Complete Power BI report  
- _Andmelugu.md_ – Data story and analytical background 

## 🧩 Data Model Overview

The data model consists of two core tables — **Contract_table** and **Salary_table** 
.  
These tables contain information about:
- Employment contracts and job dimensions (category, level, workload, gender)  
- Monthly salary, benefits, working days  

The structure enables **drill-down analysis** across different organizational groups.  
Data definitions and calculated fields are described in detail in [_Andmelugu.md_](https://github.com/amullari/portfolio/blob/main/project1-salary-analysis/Andmelugu.md)

---

## ⚙️ Usage Instructions

1. Open `.pbix` files with **Power BI Desktop (version 2024 or newer)**.  
2. The report file can be explored safely without privacy concerns.  


## 🪪 License / Credits

This project was created as a group assignment during the *“Vali Andmetarkus”* data analysis training program.

Special thanks to:
- _Kelli Tursk_ (project team member)  
- _Virve Räni_ (Lecturer, BCS Koolitus)  
- _Birgit Aljaste_ (HR Manager, BCS Koolitus – project sponsor)

All data used in this project is synthetic and generated solely for demonstration purposes.  
It does not represent any real organization or individuals.
