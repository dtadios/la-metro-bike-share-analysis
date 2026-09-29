import process
import s3_import
import export_to_s3

s3_import.import_data()
final_bike_data = process.process_data('rental_bike_data.csv')
export_to_s3.upload_to_s3('final_bike_data.csv')
