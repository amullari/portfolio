# Salary Management Report - Data Story

## Table of Contents
- [Purpose of the Data Analysis](#purpose-of-the-data-analysis)
- [Key Findings and Usage Note](#key-findings-and-usage-note)
- [Description of output](#description-of-output)
- [Glossary of Terms](#glossary-of-terms)
- [Data Protection](#data-protection)
- [Data Model](#data-model)
  - [Contract Table](#contract-table)
  - [Salary Table](#salary-table)
  - [Monthly Workdays Table](#monthly-workdays-table)
- [Measures](#measures)
- [Generation of Dummy data](#generation-of-dummy-data)

## Purpose of the Data Analysis

The objective of this data analysis is to create a **user-friendly analytical tool for HR professionals**. The tool supports understanding of salary and benefits structures and enables comparison across categories, levels, and gender. The overall goal is to support a fair and transparent salary policy.

Improving pay transparency helps build **trust**, supports **equitable pay practices**, and enables informed decision-making for both employees and management.

## Key Findings and Usage Note

This report demonstrates how salary and benefits data can be analyzed to identify pay gaps, ranges, and structural differences across job categories, levels, and gender.

> **Important:** All results shown in this report are based on **synthetic data generated for demonstration purposes**. 
> The reported figures, such as gender pay gaps or salary ranges, do **not represent any real organization or employees**.  

When applied to your own organizational data, this analytical framework and the included Power BI reports will provide **actionable insights** specific to your workforce, enabling HR professionals and management to:

- Detect potential pay disparities and outliers within categories and levels  
- Analyze gender pay gaps and distribution patterns  
- Drill down into detailed employee-level data to understand root causes  
- Support fair and transparent salary decisions

The charts and tables included in this report illustrate **the types of analysis and visualizations available**, not actual organizational results.

HR can use **department/group filters** along with the **VisibilityDeterminer** measure to create outputs suitable for external sharing, ensuring anonymity for small groups.

## Results

**Note on Average Salary:** All salary figures are presented as **full-time equivalent (FTE) monthly salaries**, meaning that salaries of employees with different workloads are adjusted to a standard full-time basis. This allows meaningful comparison across positions, levels, and genders, regardless of part-time or variable contracts.

### Salary Ranges

This chart visualizes salary ranges across job categories and levels.  
Wide ranges and outliers indicate potential inconsistencies in employee evaluation and pay structure.

From this view, users can drill down into more detailed data to identify the underlying causes of anomalies and determine possible corrective actions.

For example, the salary range of Finance Managers (2145 – 13020) suggests that job levels and grading criteria should be standardized across categories and levels, either by adjusting role definitions or aligning salaries.

![Salary Ranges](/project1-salary-analysis/images/salary-ranges.png)

## Salary Range Cross Table

This table presents the same information in a more compact form, but with less visual clarity.

![Salary Range Cross Table](/project1-salary-analysis/images/cross-table.png)

### Gender Pay Gap by Category

To analyze the gender pay gap by job families and levels, we use a bar chart showing job categories ordered by decreasing pay gap.

The gender pay gap is calculated as the difference between average male and female salaries relative to male salaries.

- A positive value indicates higher average salaries for men.  
- A negative value indicates higher average salaries for women.

A pay gap above 5% is considered critical and is highlighted in red.  
For comparison, line charts display the average salaries of men and women within each job family.

For a more detailed view by job level, a table is provided showing:

- job family  
- level  
- gender pay gap  
- average male salary  
- average female salary  
- number of employees in the group  

The overall company-level gender pay gap is 10%, indicating that the issue requires further investigation at organizational level.

Finally, the dashboard also includes a comparison of average male and female salaries across the entire company.

![Gender Pay Gap By Category](/project1-salary-analysis/images/salary-gap.png)

### Scatter Plot: Male vs Female Salaries by Position

This scatter plot shows average male and female salaries by job position.

- The Y-axis represents average male salary.  
- The X-axis represents average female salary.  
- Point size reflects the number of employees in the position.

Points above the diagonal line indicate positions where male salaries are higher.  
Points below the diagonal indicate positions where female salaries are higher.

Alongside the scatter plot, a detailed salary table is provided.  
Clicking on a point applies a position filter to the table.

The table shows:

- average base salary  
- bonuses  
- total salary  
- number of worked days  
- number of absent days  
- contract start and end dates  
- total annual salary  

![Male vs Female Salaries by Position](/project1-salary-analysis/images/scatter-plot.png)

## Glossary of Terms

**Base Salary** – the employee’s monthly base salary (excluding allowances or bonuses).  

**Benefit** or **Variable pay** – variable salary elements such as bonuses or overtime allowance.  

**Monthly Salary** – the employee’s total monthly pay including base salary and benefits.  

**Full-Time Monthly Salary** or **Monthly salary**  – monthly salary of a full-time employee.  

**Average Salary** – the average monthly salary of a full-time equivalent (FTE) employee over the selected period. This measure adjusts for part-time or variable workload, so that salaries of employees with different workloads are comparable on a full-time basis. It is not a simple mean of actual payments, but a normalized value reflecting what the salary would be for a full-time employee.  

**Group Average Salary** – average salary within a department, job category, or other group. 

**Group Median** – median monthly salary, representing a typical pay level within a group.  

**Salary Range** – minimum and maximum salaries within a group.  

**Gender Pay Gap** – difference between men’s and women’s average salaries, expressed as a % of men’s salary.

**Category** – group of job positions with similar functions within a job family; may include multiple levels.

**Level** – seniority or experience level within a category.

## Data Protection

This report is intended for use by HR professionals. There are no inherent restrictions on output visibility within HR. For outputs shared outside HR, a **department/group size filter** has been implemented to ensure anonymity where needed. A dedicated **VisibilityDeterminer measure** can be applied when filtering, to suppress values for groups below the chosen threshold.

## Data Model
![Data Model](/project1-salary-analysis/images/andmemudel.png)
### Contract Table

Contains employment contract data including gender, category, level, workload, contract dates, and employee identifiers.
Workload values are used to normalize salaries for fair comparison across full- and part-time employees.

#### Fields

| Field Name | Data Type | Key / Relation | Description |
|-------------|------------|----------------|--------------|
| **ContractID** | Long Integer | **PK** | Primary key of the contract record. Unique contract number. |
| **EmployeeID** | Long Integer | **FK → Employee.EmployeeID** | Unique identifier of the employee. Links to the Employee table. |
| **FullName** | Text |  | Employee’s full name (first name and surname). |
| **Gender** | Text |  | Gender of the employee: “Male” or “Female”. |
| **StartDate** | Date |  | Contract start date. |
| **EndDate** | Date |  | Contract end date (can be empty/null if the contract is active). |
| **Position** | Text |  | Specific job role or title in the organization. |
| **Category** | Text |  | Group of job positions sharing similar functions or belonging to the same job family. Each category may include multiple job titles at different seniority levels. |
| **CategoryCode** | Text |  | ISCO-08 four-digit job classification code for the position category. |
| **Level** | Text |  | Indicates the seniority or experience level of the position within a category. |
| **Workload** | Number (Real) |  | Workload as a fraction of a full-time position (0.0–1.0). |

---

#### Calculated Columns

| Field Name | Calculation Type | Description |
|-------------|------------------|--------------|
| **No of Levels by Category** | Derived | counts distinct levels in each category |
| **Category and Level** | Derived | combines category and level for multi-level categories |
| **LevelText** | Derived | textual level label without numeric prefix |

---

### Salary Table

Contains monthly payroll data: base salary, benefits, working days, missed days. Used for salary analysis and comparisons.

#### Fields

| Field Name         | Data Type      | Key / Relation                  | Description                                                                 |
|--------------------|---------------|---------------------------------|-----------------------------------------------------------------------------|
| ContractID         | Long Integer  | FK → Contract.ContractID        | Foreign key to Contract table.                                              |
| PeriodStart        | Date          |                                 | First day of the month.                                                     |
| PeriodEnd          | Date          | FK → Monthly Workdays.Month     | Last day of the month.                                                      |
| ActualWorkingDays  | Integer       |                                 | Number of days worked in the month.                                         |
| Salary             | Decimal       |                                 | Base salary amount for the month.                                           |
| Benefit            | Decimal       |                                 | Benefits/bonuses paid in the month.                                         |
| MissedDays         | Integer       |                                 | Number of missed workdays (vacation, sick leave, etc.).                     |
---
#### Calculated Columns

| Field Name   | Description                            |
|--------------|----------------------------------------|
| FullSalary   | Calculated as `[Salary] + [Benefit]`.  |
| Hourly Salary | Average hourly salary for a full-time employee over the selected period.       |
---

### Monthly Workdays Table 
Tracks number of working days and hours per month for full-time employees.

#### Fields

| Field Name         | Data Type        | Key / Relation                 | Description                                                                 |
|--------------------|-----------------|--------------------------------|-----------------------------------------------------------------------------|
| Month              | Date    | PK       | Last day of the month                                              |
| Working days        | integer       |                      | Number of working days per month for a full time employee                |
| Hours          | integer       |                           | Number of working hours per month for a full time employee                                                      |
---
### Measures

#### General Measures
Headcount and contract activity metrics. Includes VisibilityDeterminer to enforce privacy for small groups.

| Measure Name        | Description                                                                                                   |
|----------------------|---------------------------------------------------------------------------------------------------------------|
| **ActiveEmployees**      | Employees with active contracts. Evaluates whether the current date is between contract start and end dates. |
| **No of Employees**      | Total number of employees in the company (based on unique Employee IDs).                                   |
| **Ended Contracts**      | Contracts that have an end date within the selected month and year.                                       |
| **StartedContracts**     | Contracts that have a start date within the selected month and year.                                      |
| **No of Males**          | Number of male employees based on Employee ID.                                                            |
| **No of Females**        | Number of female employees based on Employee ID.                                                          |
| **No of Contracts**      | Number of contracts based on Contract ID.                                                                 |
| **VisibilityDeterminer** | Calculates the smaller of the counts of males and females; if the smaller count is less than 3, the measure returns blank to protect confidentiality. |

---

#### Analytical Measures

Salary and gap metrics. All averages are FTE-adjusted and account for workload. SalaryGap can be filtered by category, level, or other dimensions.

| Measure Name           | Description                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------|
| **AVG BaseSalary**          | Average monthly base salary of full-time employees over the selected period.                               |
| **AVG Benefits**            | Average monthly variable salary elements such as bonuses or allowances.                                    |
| **AVG Salary**              | Average total monthly salary (base salary + benefits) of full-time employees.                              |
| **AVG Salary Female**       | Average total monthly salary for female employees.                                                        |
| **AVG Salary Male**         | Average total monthly salary for male employees.                                                          |
| **AVG HourlySalary**        | Average hourly salary of a full-time employee based on monthly working days.                              |
| **AVG CalculatedSalary**    | Average salary adjusted for actual working and missed days (includes workload correction).                 |
| **MAX Salary**              | Maximum value of average full-time monthly salaries within the selected period.                            |
| **MedianSalary**            | Median monthly salary value of full-time employees over the selected period.                              |
| **MIN Salary**              | Minimum value of average full-time monthly salaries within the selected period.                            |
| **SalaryGap**               | Difference between men’s and women’s average salaries, expressed as a percentage of men’s average salary. |
| **Salary Range**            | The minimum and maximum values of average monthly salaries within a group.                                |
| **SalaryDifference**        | Salary range calculated as (MAX Salary – MIN Salary).                                                     |

---

##### Calculation Notes

- All average and median salary measures are based on **full-time equivalent (FTE)** values and take **workload** into account.  
- The time filters (month, year, or period) are applied consistently across all measures to ensure comparability.  
- **SalaryGap** is calculated dynamically per filter context, allowing analysis by category, level, or other dimensions.  
- **VisibilityDeterminer** supports privacy compliance by suppressing values in groups with fewer than 3 employees of either gender.  

## Generation of Dummy Data
- Generated AI-based synthetic data for 400 employees in an IT company for 2024.
- Workload: mainly 1.0, sometimes 0.5, rarely 0.75.
- Includes employees who joined or left in 2024, or had contractual changes.
- Missed days reflect Estonian seasonality; salaries adjusted proportionally.
- One row per contract per month with actual working days.
- Note: Synthetic data is for demonstration only; using your own data will produce meaningful organizational insights.

![Employee statistics](/project1-salary-analysis/images/Employee_statistics.png)
