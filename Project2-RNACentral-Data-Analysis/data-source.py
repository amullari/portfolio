import pandas as pd
import psycopg2

# Database connection details
conn = psycopg2.connect(
    host="hh-pgsql-public.ebi.ac.uk",
    database="pfmegrnargs",
    user="reader",
    password="NWDMCE5xdipIjRrp"
)

# Fetching Ensembl assembly data (excluding legacy versions)
ensembl_assembly = pd.read_sql("SELECT * FROM ensembl_assembly WHERE assembly_id != 'v1.0';", conn)

# Fetching full RNC Locus table
rnc_locus = pd.read_sql("SELECT * FROM rnc_locus", conn)

# Query for active human (Taxid: 9606) RNA locus members
query_members = """
SELECT
    rm.id,
    rm.locus_id,
    rm.urs_taxid
    FROM rnc_locus_members rm
    JOIN rnc_rna_precomputed rp ON rm.urs_taxid = rp.id
    WHERE rp.taxid = '9606'
      AND rp.is_active = true;
"""
rnc_locus_members = pd.read_sql(query_members, conn)

# Fetching RNA types for active human sequences
rnc_rna_precomputed = pd.read_sql(
    "SELECT id, rna_type FROM rnc_rna_precomputed WHERE taxid = '9606' AND is_active = TRUE;", 
    conn
)

# Connection is kept open for Power BI data refresh

