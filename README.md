# 🔐 **Hash Cracker – Python Toolkit**

A multi-algorithm hash-cracking tool supporting wordlist attacks and brute-force attacks, with automatic detection across MD5, SHA-1, SHA-2, SHA-3, and BLAKE2 families.

This tool is designed for ethical hacking, CTF challenges, and security research.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 **Features**
	•	Supports the following hash algorithms:
	•	MD5
	•	SHA-1
	•	SHA-224 / 256 / 384 / 512
	•	SHA3-224 / 256 / 384 / 512
	•	BLAKE2b / BLAKE2s
	•	Wordlist mode with default long wordlist (long_wordlist.txt)
	•	Brute-force mode (charset: a–z + 0–9)
	•	Automatic hash comparison (lowercased)
	•	Clean, readable Python code


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🛠️ **Installation**

Make sure you have Python 3 installed.
```
python3 --version
```
Clone or download the repo:
```
git clone <your-repo-url>
cd ethical-hacking-toolkit
```


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📌 **Usage**

Run the script:
```
python3 hash_cracker.py
```
You will be prompted with:

=== HASH CRACKER ===
Choose mode: 1) Wordlist  2) Brute Force (no wordlist)



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🔍 **Mode 1: Wordlist Attack**
	1.	Enter the hash you want to crack:
	2.	Press Enter to use the default wordlist

long_wordlist.txt

The program will try every word in the wordlist across all supported algorithms.


## 💣 **Mode 2: Brute Force Attack**

Brute-forces all combinations from length 1 to 8 using:

a–z
0–9

⚠️ Warning: Brute forcing up to 8 characters in Python is extremely slow and only recommended for short/simple hashes.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## **📁 File Structure**
```
ethical-hacking-toolkit/
│
├── hash_cracker.py        # Main tool
├── long_wordlist.txt      # Default wordlist
└── README.md              # Documentation
```


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ⚖️ **Legal Disclaimer**

This tool is for educational and ethical security testing only.
Do not use it on systems or hashes you do not own or have explicit permission to test.

Unauthorized cracking is illegal.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🤝 **Contributing**

Feel free to extend the wordlist, add algorithms, or improve brute-force performance.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📬 **Support**

If you want extra features like:
	•	GPU acceleration (Hashcat integration)
	•	Mask-based brute forcing
	•	Multi-processing speed-ups
	•	Rainbow table support

Ask anytime — I’ll build it for you.
