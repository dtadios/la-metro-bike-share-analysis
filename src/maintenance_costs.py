import pandas as pd

def calculate_maintenance_costs(final_csv):
    YEARLY_COST = 100

    df = pd.read_csv(final_csv)
    years = []
    maintenance_costs = []
    
    for i in range(2020,2026):
        years.append(i)
        i_df = df[df['year'] == i]
        i_count = i_df['bike_id'].nunique()
        maintenance_costs.append(YEARLY_COST * i_count)

    maintenance_costs_df = pd.DataFrame({'year': years, 'Maintenance Costs': maintenance_costs})

    maintenance_costs_df.to_csv('maintenance_costs.csv', index=False)