from setuptools import find_packages, setup
from typing import List



def get_requirments()->List[str]:
    requirments_lst:List[str] = []
    try:
        with open('requirments.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirments = line.strip()
                if requirments and requirments != '-e .':
                    requirments_lst.append (requirments)
    except FileNotFoundError:
        print("Requirment.txt File not found ")

    return requirments_lst

print(get_requirments())

setup(
    name= "NetworkSecurity",
    version='0.0.1',
    author="Srujan_Kinj",
    author_email="srujankinjawadekar1@gmail.com",
    packages=find_packages(),
    install_requires =get_requirments()
)

