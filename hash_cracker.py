import hashlib

def hash_word(word, algo):
    """Hash a word using the selected algorithm."""
    if algo == "md5":
        return hashlib.md5(word.encode()).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(word.encode()).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(word.encode()).hexdigest()
    elif algo == "sha224":
        return hashlib.sha224(word.encode()).hexdigest()
    elif algo == "sha384":
        return hashlib.sha384(word.encode()).hexdigest()
    elif algo == "sha512":
        return hashlib.sha512(word.encode()).hexdigest()
    elif algo == "blake2b":
        return hashlib.blake2b(word.encode()).hexdigest()
    elif algo == "blake2s":
        return hashlib.blake2s(word.encode()).hexdigest()
    elif algo == "sha3_224":
        return hashlib.sha3_224(word.encode()).hexdigest()
    elif algo == "sha3_256":
        return hashlib.sha3_256(word.encode()).hexdigest()
    elif algo == "sha3_384":
        return hashlib.sha3_384(word.encode()).hexdigest()
    elif algo == "sha3_512":
        return hashlib.sha3_512(word.encode()).hexdigest()
    else:
        return None

def main():
    print("=== HASH CRACKER ===")
    mode = input("Choose mode: 1) Wordlist  2) Brute Force (no wordlist)\nChoice: ").strip()
    hash_input = input("Enter the hash to crack: ").strip().lower()

    algorithms = ["md5", "sha1",
                  "sha224", "sha256", "sha384", "sha512",
                  "sha3_224", "sha3_256", "sha3_384", "sha3_512",
                  "blake2b", "blake2s"]

    if mode == "1":
        default_wordlist = "ethical-hacking-toolkit/long_wordlist.txt"
        wordlist_path = input(f"Enter wordlist path (press Enter to use default: {default_wordlist}): ").strip()
        if wordlist_path == "":
            wordlist_path = default_wordlist
        try:
            with open(wordlist_path, "r") as f:
                words = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print("Wordlist file not found.")
            return
    else:
        words = None

    import itertools
    charset = "abcdefghijklmnopqrstuvwxyz0123456789"

    def brute_force_generator(max_len=8):
        for length in range(1, max_len + 1):
            for combo in itertools.product(charset, repeat=length):
                yield "".join(combo)

    if mode == "2":
        print("\nBrute forcing (length 1–8)... This will take significant time.\n")
        words = brute_force_generator()

    print("\nCracking...\n")

    for word in words:
        for algo in algorithms:
            hashed = hash_word(word, algo)
            if hashed.lower() == hash_input:
                print(f"🔥 Match Found! → {word}  (Type: {algo.upper()})")
                return

    print("❌ No match found in the provided wordlist.")

if __name__ == "__main__":
    main()