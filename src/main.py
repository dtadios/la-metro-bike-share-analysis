import process
import s3_import
import export_to_s3

to_python = 'to_python.csv'
final = 'final.csv'

s3_import.import_data()
process.process_data(to_python)
export_to_s3.upload_to_s3(final)