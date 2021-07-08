# BayesianOntology

Installation instructions:
https://test.pypi.org/project/BayesOnt/#description

`pip install twine wheel`

`python3 setup.py sdist bdist_wheel`

`python3 -m twine upload -r testpypi dist/*`

`pip install -i https://test.pypi.org/simple/ BayesOnt==1.0.4`


https://dev.to/arnu515/create-a-pypi-pip-package-test-it-and-publish-it-using-github-actions-part-1-3cp8
