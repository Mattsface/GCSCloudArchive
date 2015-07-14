from setuptools import setup, find_packages


setup(name='GCSCloudArchive',
      version='0.1.0',
      description='New project to replace the current zuGCSCloudArchive.sh shell script for Google bucket storage transfers.',
      author='Matthew Spah',
      author_email='spahmatther@gmail.com',
      scripts=[''],
      packages=find_packages(),
      install_requires=[
          'nose',
          'gcs-oauth2-boto-plugin'
      ],
      zip_safe=False)


