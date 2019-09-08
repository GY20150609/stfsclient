from setuptools import setup

setup(
    name='stfsclient',
    version='1.0.0.a1',
    url='https://github.com/jagans94/stfsclient',
    
    author='Jagan Seshadri',
    author_email='jagans94@gmail.com',

    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['numpy', 'protobuf', 'grpcio'],
    extras_require={
        'dev':  ["tensorflow>=1.13.1, <=2.0",
                 "jupyterlab==1.0.5"],
    }
    python_requires='>=3.6',

    license='MIT',
    description='A simple, consolidated, extensible gRPC-based client implementation \
        for querying a hosted `tensorflow_model_server`.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords = 'grpc, protobuf, tensorflow serving, client',

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
