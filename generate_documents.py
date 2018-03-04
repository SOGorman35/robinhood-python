#!/usr/bin/env python3

import csv

from robinhood.RobinhoodCachedClient import RobinhoodCachedClient

# Set up the client
client = RobinhoodCachedClient()
client.login()

def generate_documents():
  with open('documents.csv', 'w', newline='') as documents_csv_file:
    fieldnames = ['document_id', 'date', 'type', 'path']
    documents_csv_writer = csv.DictWriter(documents_csv_file, fieldnames=fieldnames)
    documents_csv_writer.writeheader()

    for document in client.get_documents():
      document_id = document['id']
      document_type = document['type']
      document_date = document['date']

      contents = client.download_document_by_id(document_id)
      pdf_path = 'document_{}.pdf'.format(document_id)
      with open(pdf_path, 'wb') as document_pdf_file:
        document_pdf_file.write(contents)

      documents_csv_writer.writerow({
        'document_id': document_id,
        'date': document_date,
        'type': document_type,
        'path': pdf_path,
      })

if __name__ == '__main__':
  generate_documents()

