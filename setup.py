import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PACKAGE_DIR = {"": "."}
PACKAGES = setuptools.find_packages()
setuptools.setup(
    name="tesseract_reader",
    version="0.0.1",
    author="Dunn Kopylov",
    author_email="38dunn@gmail.com",
    description="tesseract reader",
    long_description=long_description,
    long_description_content_type="text/markdown",

    package_dir=PACKAGE_DIR,
    packages=PACKAGES,

    python_requires=">=3.10"
)
