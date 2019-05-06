# SociaList

What is social engineering?
---------------------------

Social engineering is the term used for a broad range of malicious activities accomplished through human interactions. It uses psychological manipulation to trick users into making security mistakes or giving away sensitive information.

Attacks happen in one or more steps. A perpetrator first investigates the intended victim to gather necessary background information, such as potential points of entry and weak security protocols, needed to proceed with the attack. Then, the attacker moves to gain the victim’s trust and provide stimuli for subsequent actions that break security practices, such as revealing sensitive information or granting access to critical resources. What makes social engineering especially dangerous is that it relies on human error, rather than vulnerabilities in software and operating systems. Mistakes made by legitimate users are much less predictable, making them harder to identify and thwart than a malware-based intrusion.

For more information about social engineering attacks check [social engineering attacks].

Requirements
-------------------
  - python 3

Usage
---------

At the beginning of the execution of this script, you will be asked for a series of personal information about which you intend to create the list of passwords. From the personal data entered by keyboard, combinations and permutations will be made according to those entered in the arguments.

**Note:** In order to display the wordlist generation progress percentage we would need a progress bar, so:

 ```sudo pip install tqdm```
 
**Run:**

```
usage: socialist.py [-h] -o OUTPUT [-c COMBINATIONS]

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        path to output wordlist
  -c COMBINATIONS, --combinations COMBINATIONS
                        maximum number of words combinations -- default 2
```

Contributing
---------------
If you would like to contribute code, please **fork** this repository, make your changes, and then submit a pull-request.

[social engineering attacks]: https://www.incapsula.com/web-application-security/social-engineering-attack.html
