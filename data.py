import random

# Competences candidate for cybersecurity exercises

competences = [
    "blockchain",
    "crypto",
    "forensics",
    "gamepwn",
    "hardware",
    "web",
]

# Knowledge components candidate for cybersecurity exercises
kcs = [
    "nmap",
    "wireshark",
    "metasploit",
    "jacktheripper",
    "hashcat",
    "netcat",
    "fluxion",
    "aircrack",
    "sqlmap",
    "burpsuite",
    "hydra",
    "john",
    "gdb",
    "radare2",
    "ida",
    "ollydbg",
    "lynis",
    "chkrootkit",
    "clamav",
    "tripwire",
    "snort",
    "volatility",
    "autopsy",
    "sleuthkit",
    "strings",
    "binwalk",
]

# TODO: SI SE TE DA MAL UNA COMPETENCIA, TIENEN QUE DÁRSETE MAL SUS KCS!!
competence_kcs = {
    "blockchain": random.sample(kcs, 6),
    "crypto": random.sample(kcs, 6),
    "forensics": random.sample(kcs, 6),
    "gamepwn": random.sample(kcs, 6),
    "hardware": random.sample(kcs, 6),
    "web": random.sample(kcs, 6),
}
