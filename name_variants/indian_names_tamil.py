"""
Indian names — Tamil lookup.
South Indian names: Tamil Nadu, Sri Lanka Tamil, Singapore/Malaysia Tamil diaspora.

Romanization variant problem:
  Subramaniam / Subramanian / Subramanyam / Subrahmanyam — all the same name
  Ramasamy / Ramaswami / Ramamurthy — related but distinct
  Murugan / Murukan / Murugesan — same deity name base, different suffixes

Sources:
  - ISO 15919 Tamil romanization
  - Madras colloquial transliteration (dominant in Sri Lanka and diaspora)
  - Singapore/Malaysia Tamil community spellings
"""

INDIAN_NAMES_TAMIL: dict[str, list[str]] = {
    # ── Common Tamil surnames / family name components ──────────────────────
    "சுப்பிரமணியம்": ["subramaniam", "subramanian", "subramanyam", "subrahmanyam", "suppiramaniyam"],
    "வேலுசாமி": ["velusamy", "velaswamy", "veluchamy"],
    "முருகன்": ["murugan", "murukan", "murughan"],
    "முருகேசன்": ["murugesan", "murugason", "murughesan"],
    "ராமசாமி": ["ramasamy", "ramaswamy", "ramasami"],
    "கிருஷ்ணசாமி": ["krishnaswamy", "krishnaswami", "krushnaswamy"],
    "விஜயராகவன்": ["vijayaraghavan", "vijayarghavan"],
    "சிவசுப்பிரமணியன்": ["sivasubramaniam", "sivasubramanian"],
    "சந்திரசேகர்": ["chandrasekhar", "chandrasekar", "chandrasekaran"],
    "பாலசுப்பிரமணியம்": ["balasubramaniam", "balasubramanian"],
    "வெங்கடேசன்": ["venkatesan", "venkitesan", "venkadesh"],
    "நடராஜன்": ["natarajan", "natarajen"],
    "கண்ணன்": ["kannan", "kannen"],
    "குமாரசாமி": ["kumaraswamy", "kumarasamy"],
    "அருணாசலம்": ["arunachalam", "arunasalam"],
    "கார்த்திகேயன்": ["karthikeyan", "karthigeyan", "kartikeyan"],
    "பழனிசாமி": ["palanisamy", "palaniswamy", "palani"],
    "சாமிநாதன்": ["saminathan", "swaminathan", "swaminathen"],
    "ஆனந்தகிருஷ்ணன்": ["ananthakrishnan", "anandakrishnan"],
    "தங்கவேல்": ["thangavel", "thangavelu"],
    "ராஜேந்திரன்": ["rajendran", "rajindran"],
    # ── Common Tamil given name components ─────────────────────────────────
    "முரளி": ["murali", "muralee"],
    "கார்த்திக்": ["karthik", "kartik", "karthick"],
    "பிரசாத்": ["prasath", "prasad"],
    "ஆனந்த்": ["anand", "ananth", "anandh"],
    "விக்னேஷ்": ["vikneswaran", "vigneswaran", "vignesh"],
    "ஸ்ரீனிவாஸ்": ["srinivas", "sreenivas", "sreenivaas"],
    "பரமேஸ்வரன்": ["parameswaran", "parameshwaran"],
    "லட்சுமி": ["lakshmi", "laxmi", "luxmi"],
    "மீனாட்சி": ["meenakshi", "minakshi", "meenachee"],
    "சரஸ்வதி": ["saraswati", "saraswathy", "sarasvati"],
    "அம்பாள்": ["ambal"],
    "தேவி": ["devi", "thevi"],
    "கமலா": ["kamala", "kamla"],
    "ரேவதி": ["revathi", "revati"],
    "மாலதி": ["malathi", "malati"],
    "ஷோபா": ["shoba", "shobha"],
    "ஸ்ரீதேவி": ["sridevi", "sreedevi"],
    "நிர்மலா": ["nirmala", "nirmalla"],
    "கல்பனா": ["kalpana", "kalpna"],
    "ஷாந்தி": ["shanthi", "shanti"],
    "கீர்த்தனா": ["keerthana", "keertana", "kirtana"],
    "தர்ஷினி": ["dharshini", "darshini"],
    "பிரியா": ["priya", "preya"],
    "ஸ்ரீதர்": ["sridhar", "sreedhar"],
    "ஹரி": ["hari", "hary"],
    "குமார்": ["kumar", "koomar"],
    "ஆதித்யா": ["aditya", "aaditya"],
    "விஜய்": ["vijay", "vijei"],
    "அஜித்": ["ajith", "ajit"],
    "விஷால்": ["vishal"],
    "சிம்பு": ["simbu", "stmbu"],
    "தனுஷ்": ["dhanush", "danus"],
}
