from setuptools import setup, find_packages

setup(
    name='stfsclient',
    version='1.1.0',
    url='https://github.com/jagans94/stfsclient',
    
    author='Jagan Seshadri',
    author_email='jagans94@gmail.com',

    packages=find_packages(),
    include_package_data=True,
    install_requires=['numpy', 'protobuf', 'grpcio'],
    extras_require={
        'dev':  ["tensorflow>=1.13.1, <=2.0",
                 "jupyterlab==1.0.5"],
        'vis':  ["matplotlib"],
    },
    python_requires='>=3.5, <3.8',

    license='MIT',
    description='A simple, consolidated gRPC-based client implementation \
        for querying a hosted `tensorflow_model_server`.',
    # TODO: Change long_description/[_type]
    #long_description=open('README.md').read(),
    #long_description_content_type='text/markdown',
    keywords = 'grpc, protobuf, tensorflow serving, client',

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
