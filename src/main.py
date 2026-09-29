import process
import s3_import
import export_to_s3
import maintenance_costs

to_python = 'to_python.csv'
final = 'final.csv'
maintenance_costs_csv = 'maintenance_costs.csv'


s3_import.import_data()
process.process_data(to_python)
maintenance_costs.calculate_maintenance_costs(final)

export_to_s3.upload_to_s3(final)
export_to_s3.upload_to_s3(maintenance_costs_csv)