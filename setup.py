from setuptools import setup, find_namespace_packages

setup(name='personal_assistant',
      version='0.0.1',
      author='Rodion Tiutiunyk, Ihor Moroz, Vladimir Grebeniuk, Andrii Siryi',
      license='MIT',
      install_requires=['pyowm', 'requests'],
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['personal_assistant = personal_assistant.functions:main']})
