from sys import argv

JAS = 1
SATURACE = 1

# Obarveni retezce pomoci terminalove escape sekvence
# RGB: \x1b[38;2;R;G;BmTEXT\x1b[0m 
def rgb_term_string(r,g,b, value, underline=False, bold=False):
    term_bold = ""
    term_underline = ""
    if bold: term_bold = "1;"
    if underline: term_underline = "4;"
    return f"\x1b[{term_bold}{term_underline}38;2;{r};{g};{b}m{value}\x1b[0m"

# HSV na RGB
def hsv_to_rgb(h, s, v):
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h*6.)
    f = (h*6.)-i
    p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f))))
    v*=255; i%=6
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)


if len(argv) >= 2: txt = argv[1]
else: txt = "█"

print(f"Kreslím odstíny HSV 0° až 360° při saturaci {int(SATURACE * 100)} % a jasu {int(JAS * 100)} %")
print("")

# Vykresleni HSV duhy 0-360
for hue in range(0, 360):
    r, g, b = hsv_to_rgb(hue/360, SATURACE, JAS)
    print(rgb_term_string(r, g, b, txt), end="", flush=True)
    if (hue+1) % 20 == 0: print("")

print("")
