import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Quandoo",
    version="1.2.3",
    author="Fraser Langton",
    author_email="fraserbasil@gmail.com",
    description="This is a fairly lightwieght SDK for interacting with the Quandoo API, it is a work in progress.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fraser-langton/Quandoo",
    packages=setuptools.find_packages(),
    scripts=["quandoo/Customer.py", "quandoo/ErrorResponse.py", "quandoo/Merchant.py", "quandoo/QuandooModel.py", "quandoo/Reservation.py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
