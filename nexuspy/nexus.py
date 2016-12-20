import os

import requests


class Nexus(object):
  upload_path = 'service/local/artifact/maven/content'


  def __init__(self, url, username=None, password=None):
    self.url = url
    self.username = username
    self.password = password


  def upload_artifact(self, localFilePath, repository, groupId, artifactId, version, packaging=None,
      remoteFilePath=None, classifier=None, extension=None):
    if not self.username or not self.password:
      raise Exception('Username or password was not set, cannot upload artifacts')
    if not remoteFilePath:
      remoteFilePath = os.path.basename(localFilePath)
    if not extension:
      _, extension = os.path.splitext(localFilePath)
    if not packaging:
      packaging = extension
    parameters = {
      'r'     : repository,
      'hasPom': 'false',
      'g'     : groupId,
      'a'     : artifactId,
      'v'     : version,
      'p'     : packaging,
      'c'     : classifier,
      'e'     : extension,
      'file'  : remoteFilePath,
    }
    with open(localFilePath, "rb") as file:
      remotePath = '{}/{}/{}/{}/{}'.format(repository, groupId, artifactId, version, remoteFilePath)
      print('Uploading file {} to {}'.format(localFilePath, remotePath))
      response = requests.post('{}/{}'.format(self.url, Nexus.upload_path), auth=(self.username, self.password),
        params=parameters, files={'file': file})
      if response.status_code != 201:
        raise Exception('Failed to upload file: {0}\n{1}'.format(response.status_code, response.text))
    print('Uploaded successfully')
