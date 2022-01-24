import dropbox

class TransferData:
  def __init__(self, access_token):
    self.access_token = access_token

  def upload_file(self, file_from, file_to):
    """upload a file to Dropbox using API v2
    """
    dbx = dropbox.Dropbox(self.access_token)

    with open(file_from, 'rb') as f:
      dbx.files_upload(f.read(), file_to)

def main():
  access_token = 'sl.A_o044c3CjbfZfjQ_CPq2JY9ctjebwYlwthGs1Z0THWGw_t9Wm3OmIPiDg99AEot9iinO1iCfxd5C6IWQYbPywSbWFss-b9PXmVObMTj7VF39y6vRIdjY6KZrhrADvZiQ-h--MWRD5Td'
  transferData = TransferData(access_token)

  file_from = 'PLERNERT.png'
  file_to = '/Photos/PLERNERT.pngq'  # The full path to upload the file to, including the file name

  # API v2
  transferData.upload_file(file_from, file_to)
  print("file uploaded!")



main()